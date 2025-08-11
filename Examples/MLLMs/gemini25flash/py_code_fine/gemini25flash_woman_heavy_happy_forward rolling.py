
import pygame
import math
import numpy as np
import os # For checking if BVH file exists

# --- BVH Parsing Classes and Functions ---
class Joint:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.offset = np.array([0.0, 0.0, 0.0])
        self.channels = [] # List of strings like 'Xposition', 'Yrotation'
        self.channel_indices = {} # Map channel name to index in frame data
        self.motion_data = [] # List of lists/arrays of channel values per frame

        # For FK:
        self.local_transform = np.identity(4) # Transform relative to parent
        self.global_transform = np.identity(4) # Transform relative to root (Hips)
        self.position = np.array([0.0, 0.0, 0.0]) # Global 3D position

    def add_child(self, child_joint):
        self.children.append(child_joint)

def parse_bvh(filename):
    """
    Parses a BVH file to extract skeleton hierarchy and motion data.
    Returns the root joint, a dictionary of all joints, number of frames, and frame time.
    """
    joints = {}
    root_joint = None
    current_joint = None # Tracks the joint being currently processed in the hierarchy
    
    with open(filename, 'r') as f:
        lines = f.readlines()

    line_idx = 0
    while line_idx < len(lines):
        line = lines[line_idx].strip()

        if line == 'HIERARCHY':
            line_idx += 1
            continue
        elif line.startswith('ROOT') or line.startswith('JOINT'):
            parts = line.split()
            joint_name = parts[1]
            new_joint = Joint(joint_name, parent=current_joint)
            joints[joint_name] = new_joint

            if current_joint:
                current_joint.add_child(new_joint)
            else:
                root_joint = new_joint
            current_joint = new_joint
            
            line_idx += 1 # Expects '{'
            line_idx += 1 # Expects 'OFFSET' line
            offset_line = lines[line_idx].strip()
            new_joint.offset = np.array(list(map(float, offset_line.split()[1:])))
            
            line_idx += 1 # Expects 'CHANNELS' line
            channels_line = lines[line_idx].strip()
            channel_parts = channels_line.split()
            num_channels_declared = int(channel_parts[1])
            new_joint.channels = channel_parts[2:]
            
            if len(new_joint.channels) != num_channels_declared:
                raise ValueError(f"Channel count mismatch for joint {joint_name}: declared {num_channels_declared}, found {len(new_joint.channels)}")

            for i, ch_name in enumerate(new_joint.channels):
                new_joint.channel_indices[ch_name] = i

            line_idx += 1 # Move to next line (can be JOINT, END SITE, or '}')
            
        elif line.startswith('END SITE'):
            # This is a leaf node, often represents an end effector position
            end_site_name = current_joint.name + "_EndSite" # Naming convention for end sites
            end_site_joint = Joint(end_site_name, parent=current_joint)
            current_joint.add_child(end_site_joint)
            joints[end_site_name] = end_site_joint # Add to global joints dict

            line_idx += 1 # Expects '{'
            line_idx += 1 # Expects 'OFFSET'
            offset_line = lines[line_idx].strip()
            end_site_joint.offset = np.array(list(map(float, offset_line.split()[1:])))
            line_idx += 1 # Expects '}'
            
        elif line == '}':
            if current_joint and current_joint.parent: # Move up the hierarchy
                current_joint = current_joint.parent
            line_idx += 1
        elif line == 'MOTION':
            # Finished HIERARCHY, now parse MOTION data
            line_idx += 1
            
            num_frames_line = lines[line_idx].strip()
            num_frames = int(num_frames_line.split()[1])
            line_idx += 1
            
            frame_time_line = lines[line_idx].strip()
            frame_time = float(frame_time_line.split()[2])
            
            line_idx += 1 # Start of raw motion data values
            
            all_motion_data = []
            for _ in range(num_frames):
                frame_data_line = lines[line_idx].strip()
                all_motion_data.append(list(map(float, frame_data_line.split())))
                line_idx += 1
            
            # Distribute motion data to respective joint's motion_data list
            # Iterate through joints in the order they were parsed to match flat motion data
            parsed_joint_names_ordered = list(joints.keys())
            for frame_data_row in all_motion_data:
                current_data_offset = 0
                for joint_name in parsed_joint_names_ordered:
                    joint = joints[joint_name]
                    num_channels = len(joint.channels)
                    
                    if current_data_offset + num_channels > len(frame_data_row):
                        raise ValueError(f"Motion data row too short for frame. Expected {current_data_offset + num_channels}, got {len(frame_data_row)}. Frame data: {frame_data_row}")
                        
                    joint_frame_data = frame_data_row[current_data_offset : current_data_offset + num_channels]
                    joint.motion_data.append(joint_frame_data)
                    current_data_offset += num_channels
            
            break # Finished parsing BVH after motion data
        else:
            line_idx += 1 # Skip any other unhandled lines (e.g., blank lines, comments)

    return root_joint, joints, num_frames, frame_time

def get_rotation_matrix_from_channels(joint, frame_data):
    """
    Builds a rotation matrix from channel data for a joint, applying rotations intrinsically
    based on the order listed in joint.channels (e.g., Z, then Y, then X for ZYX order).
    """
    current_rot_mat = np.identity(3)
    
    for channel_name in joint.channels:
        if 'rotation' in channel_name:
            angle_deg = frame_data[joint.channel_indices[channel_name]]
            angle_rad = np.radians(angle_deg)
            axis_char = channel_name[0].upper() # 'X', 'Y', or 'Z'
            
            if axis_char == 'X':
                R_axis = np.array([
                    [1, 0, 0],
                    [0, math.cos(angle_rad), -math.sin(angle_rad)],
                    [0, math.sin(angle_rad), math.cos(angle_rad)]
                ])
            elif axis_char == 'Y':
                R_axis = np.array([
                    [math.cos(angle_rad), 0, math.sin(angle_rad)],
                    [0, 1, 0],
                    [-math.sin(angle_rad), 0, math.cos(angle_rad)]
                ])
            elif axis_char == 'Z':
                R_axis = np.array([
                    [math.cos(angle_rad), -math.sin(angle_rad), 0],
                    [math.sin(angle_rad), math.cos(angle_rad), 0],
                    [0, 0, 1]
                ])
            else:
                R_axis = np.identity(3) # Should not happen for standard BVH
            
            current_rot_mat = np.dot(current_rot_mat, R_axis) # Intrinsic rotation: M = M_prev * R_axis
            
    return current_rot_mat

def forward_kinematics(joint, parent_global_transform, frame_idx):
    """
    Recursively calculates the global transformation matrix and position for a joint
    and its children for a given frame.
    """
    
    # Get frame-specific motion data for this joint
    joint_frame_data = joint.motion_data[frame_idx] if frame_idx < len(joint.motion_data) else [0.0] * len(joint.channels)

    # Determine local translation:
    local_translation_vec = np.array([0.0, 0.0, 0.0])
    if joint.parent is None: # This is the root joint (Hips)
        # Root can have position channels (Xposition, Yposition, Zposition)
        if 'Xposition' in joint.channels:
            local_translation_vec[0] = joint_frame_data[joint.channel_indices['Xposition']]
        if 'Yposition' in joint.channels:
            local_translation_vec[1] = joint_frame_data[joint.channel_indices['Yposition']]
        if 'Zposition' in joint.channels:
            local_translation_vec[2] = joint_frame_data[joint.channel_indices['Zposition']]
        local_translation_vec += joint.offset # Add the root's base offset (often [0,0,0])
    else:
        local_translation_vec = joint.offset # Child joint's position is its offset from parent

    # Determine local rotation matrix
    local_rotation_matrix = get_rotation_matrix_from_channels(joint, joint_frame_data)

    # Construct the local transformation matrix (rotation then translation)
    joint.local_transform = np.identity(4)
    joint.local_transform[:3, :3] = local_rotation_matrix # Set rotation part
    joint.local_transform[:3, 3] = local_translation_vec # Set translation part

    # Calculate global transform: parent's global transform * this joint's local transform
    joint.global_transform = np.dot(parent_global_transform, joint.local_transform)

    # Extract global position of the joint's origin (pivot point)
    joint.position = joint.global_transform[:3, 3]

    # Recursively call FK for all children of this joint
    for child in joint.children:
        forward_kinematics(child, joint.global_transform, frame_idx)

def get_joint_positions_for_frame(root_joint, frame_idx):
    """
    Initiates forward kinematics and collects the global 3D positions of all joints
    for a specific frame.
    """
    # Start FK from the root with an identity matrix as its parent's global transform
    forward_kinematics(root_joint, np.identity(4), frame_idx)

    # Collect positions of all joints in a dictionary
    positions = {}
    q = [root_joint] # Use a queue for breadth-first traversal
    while q:
        joint = q.pop(0)
        positions[joint.name] = joint.position
        for child in joint.children:
            q.append(child)
    return positions

# --- Pygame Animation Setup ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 30 # Frames per second for animation playback
POINT_RADIUS = 5 # Radius of the white point-lights
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Mapping BVH Joint Names to 15 Required Points ---
# This list specifies the exact 15 joint names from the BVH file that correspond
# to the desired points for the biological motion stimulus.
# These names are typical for CMU MoCap files.
TARGET_BVH_JOINT_NAMES = [
    'Head', 'Neck', 
    'RShoulder', 'LShoulder', 
    'RElbow', 'LElbow',
    'RWrist', 'LWrist', 
    'Spine1', # Represents the upper torso/chest center (often called 'Thorax' or 'Sternum' in other models)
    'RHipJoint', 'LHipJoint',
    'RTibia', # The 'RTibia' joint's position is the right knee joint
    'LTibia', # The 'LTibia' joint's position is the left knee joint
    'RFoot',  # The 'RFoot' joint's position is the right ankle joint
    'LFoot'   # The 'LFoot' joint's position is the left ankle joint
]

def get_15_point_coords(all_joint_positions):
    """
    Extracts the 3D coordinates for the specified 15 target points
    from the complete set of joint positions provided by FK.
    """
    coords = []
    for joint_name in TARGET_BVH_JOINT_NAMES:
        if joint_name in all_joint_positions:
            coords.append(all_joint_positions[joint_name])
        else:
            # Fallback for missing joints. This should ideally not happen with a standard BVH.
            # If it does, using a zero vector might cause points to appear at the origin.
            coords.append(np.array([0.0, 0.0, 0.0])) 
            # print(f"Warning: Joint '{joint_name}' not found in BVH data. Using [0.0,0.0,0.0].")
    
    if len(coords) != 15:
        raise ValueError(f"Expected exactly 15 points, but got {len(coords)} after mapping from BVH.")
        
    return coords

def project_3d_to_2d(point_3d, scale_factor, offset_x, offset_y):
    """
    Performs an orthographic projection of a 3D point onto a 2D plane
    and applies scaling and offset for display on the Pygame screen.
    """
    x = point_3d[0] * scale_factor + offset_x
    # Invert Y-axis: BVH typically uses Y-up, while Pygame's Y-axis increases downwards.
    y = -point_3d[1] * scale_factor + offset_y 
    return int(x), int(y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion Stimulus - Forward Rolling")
    clock = pygame.time.Clock()

    bvh_file = '66_11.bvh' # CMU MoCap 66_11 "Rolling on the ground"
    
    # Check if the required BVH file exists.
    # Users need to download this file manually as it's an external dependency.
    if not os.path.exists(bvh_file):
        print(f"Error: BVH file '{bvh_file}' not found.")
        print("Please download it from the CMU MoCap Database and place it in the same directory as this script.")
        print(f"Direct link: http://mocap.cs.cmu.edu/subjects/66/66_11.bvh")
        pygame.quit()
        return

    try:
        root_joint, all_joints_dict, num_frames, frame_time = parse_bvh(bvh_file)
        print(f"BVH loaded: {num_frames} frames, {frame_time:.4f}s per frame.")
    except Exception as e:
        print(f"Error parsing BVH file: {e}")
        pygame.quit()
        return

    # Pre-calculate all 15-point positions for all frames.
    # This is done once at the start for efficiency during animation playback
    # and to determine the necessary scaling and offset for fitting the animation to screen.
    all_frame_15_point_coords = []
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')

    for i in range(num_frames):
        all_current_joint_positions = get_joint_positions_for_frame(root_joint, i)
        coords_for_frame = get_15_point_coords(all_current_joint_positions)
        all_frame_15_point_coords.append(coords_for_frame)

        # Update min/max for scaling calculation, considering all points across all frames
        for p in coords_for_frame:
            min_x = min(min_x, p[0])
            max_x = max(max_x, p[0])
            min_y = min(min_y, p[1])
            max_y = max(max_y, p[1])

    # Determine optimal scaling factor and offset to center the animation
    padding = 50 # Pixels to ensure the animation doesn't touch the screen edges
    
    data_width = max_x - min_x
    data_height = max_y - min_y
    
    # Prevent division by zero if the motion data is flat along an axis
    if data_width == 0: data_width = 1.0 
    if data_height == 0: data_height = 1.0

    # Calculate scale factors based on the usable screen area (screen minus padding)
    screen_usable_width = SCREEN_WIDTH - 2 * padding
    screen_usable_height = SCREEN_HEIGHT - 2 * padding
    
    scale_x = screen_usable_width / data_width
    scale_y = screen_usable_height / data_height
    
    # Use the smaller of the two scale factors to maintain aspect ratio and ensure
    # the entire animation fits within the screen. An additional factor (0.9) adds a small margin.
    scale_factor = min(scale_x, scale_y) * 0.9 

    # Calculate offsets to center the scaled animation on the screen
    data_center_x = (min_x + max_x) / 2
    data_center_y = (min_y + max_y) / 2
    
    offset_x = SCREEN_WIDTH / 2 - (data_center_x * scale_factor)
    # For Y, since the Pygame Y-axis is inverted relative to BVH's typical Y-up,
    # we need to add the scaled data_center_y to the screen_height_center.
    offset_y = SCREEN_HEIGHT / 2 + (data_center_y * scale_factor) 

    current_frame = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # Clear the screen to black before drawing the next frame

        # Get the 15 point 3D coordinates for the current frame
        current_frame_coords_3d = all_frame_15_point_coords[current_frame]

        # Project each 3D point to 2D screen coordinates and draw it as a white circle
        for point_3d in current_frame_coords_3d:
            x, y = project_3d_to_2d(point_3d, scale_factor, offset_x, offset_y)
            pygame.draw.circle(screen, WHITE, (x, y), POINT_RADIUS)

        pygame.display.flip() # Update the full display Surface to the screen

        # Move to the next frame. Use modulo to loop back to the beginning of the animation.
        current_frame = (current_frame + 1) % num_frames
        
        # Control animation speed by limiting frames per second.
        # A fixed FPS (e.g., 30) ensures smooth playback.
        clock.tick(FPS) 

    pygame.quit() # Uninitialize Pygame modules

if __name__ == "__main__":
    main()
