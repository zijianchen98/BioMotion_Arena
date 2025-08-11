
import pygame
import math

# Easing function for smoother transitions (Quadratic ease-in-out)
def ease_in_out_quad(t):
    """
    Applies a quadratic ease-in-out effect to a normalized time value t.
    t: A float from 0.0 to 1.0 representing normalized time.
    Returns: A float representing the eased value.
    """
    if t < 0.5:
        return 2 * t * t
    return -1 + (4 - 2 * t) * t

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sadman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point settings
POINT_RADIUS = 5 # Radius of each white point

# Joint names for the 15-point figure, based on standard biomechanical models
# and interpreting the example image.
JOINT_NAMES = [
    "Head", "Neck",
    "R_Shoulder", "L_Shoulder",
    "R_Elbow", "L_Elbow",
    "R_Wrist", "L_Wrist",
    "Torso", # This will be the root/reference point for the figure's global position and relative poses
    "R_Hip", "L_Hip",
    "R_Knee", "L_Knee",
    "R_Ankle", "L_Ankle"
]

class HumanFigure:
    def __init__(self, x_start, y_start):
        self.initial_x = x_start # Starting X position for the figure's root
        self.initial_y = y_start # Starting Y position for the figure's root (ground level reference)
        
        self.x = x_start # Current global X position of the Torso
        self.y = y_start # Current global Y position of the Torso

        # Neutral stand pose: define offsets for each joint relative to the Torso (0,0)
        # These proportions define the base shape of the stick figure.
        self.neutral_offsets = {
            "Head":       (0, -60),
            "Neck":       (0, -30),
            "R_Shoulder": (25, -15),
            "L_Shoulder": (-25, -15),
            "R_Elbow":    (45, 10),
            "L_Elbow":    (-45, 10),
            "R_Wrist":    (55, 40),
            "L_Wrist":    (-55, 40),
            "Torso":      (0, 0), # Torso is the origin of the local coordinate system
            "R_Hip":      (15, 50),
            "L_Hip":      (-15, 50),
            "R_Knee":     (15, 100),
            "L_Knee":     (-15, 100),
            "R_Ankle":    (15, 150),
            "L_Ankle":    (-15, 150)
        }

        # Dictionary to store current global screen coordinates of all joints
        self.current_joints = {}
        self._update_joint_positions_from_offsets(self.neutral_offsets)

        # Animation parameters specific to the "sadman jumping forward" action
        self.MAX_JUMP_HEIGHT = 80  # Max vertical displacement upwards from standing (for Torso)
        self.MAX_CROUCH_DEPTH = 50 # Max vertical displacement downwards from standing (for Torso)
        self.FORWARD_SPEED = 2     # Pixels per frame for continuous forward movement

        # Define keyframe poses for the jump cycle.
        # Each pose is a dictionary of {joint_name: (x_offset, y_offset) from Torso}.
        # These poses are designed to represent a "sadman" jump (less energetic, slightly hunched).

        # Keyframe 0: Standard standing pose (same as neutral offsets)
        self.pose_stand = self.neutral_offsets

        # Keyframe 1: Deep Crouch - preparing for jump
        self.pose_crouch = self.neutral_offsets.copy()
        self.pose_crouch["Torso"] = (0, self.MAX_CROUCH_DEPTH) # Torso lowers
        # Legs bend more deeply
        self.pose_crouch["R_Hip"] = (self.neutral_offsets["R_Hip"][0], self.neutral_offsets["R_Hip"][1] + self.MAX_CROUCH_DEPTH - 10)
        self.pose_crouch["L_Hip"] = (self.neutral_offsets["L_Hip"][0], self.neutral_offsets["L_Hip"][1] + self.MAX_CROUCH_DEPTH - 10)
        self.pose_crouch["R_Knee"] = (self.neutral_offsets["R_Knee"][0] + 5, self.neutral_offsets["R_Knee"][1] + self.MAX_CROUCH_DEPTH + 10)
        self.pose_crouch["L_Knee"] = (self.neutral_offsets["L_Knee"][0] - 5, self.neutral_offsets["L_Knee"][1] + self.MAX_CROUCH_DEPTH + 10)
        self.pose_crouch["R_Ankle"] = (self.neutral_offsets["R_Ankle"][0] + 10, self.neutral_offsets["R_Ankle"][1] + self.MAX_CROUCH_DEPTH + 20)
        self.pose_crouch["L_Ankle"] = (self.neutral_offsets["L_Ankle"][0] - 10, self.neutral_offsets["L_Ankle"][1] + self.MAX_CROUCH_DEPTH + 20)
        # Arms swing back slightly (characteristic of jump prep and "sadman" lack of vigor)
        self.pose_crouch["R_Shoulder"] = (self.neutral_offsets["R_Shoulder"][0] + 5, self.neutral_offsets["R_Shoulder"][1] + 10)
        self.pose_crouch["L_Shoulder"] = (self.neutral_offsets["L_Shoulder"][0] - 5, self.neutral_offsets["L_Shoulder"][1] + 10)
        self.pose_crouch["R_Elbow"] = (self.neutral_offsets["R_Elbow"][0] - 10, self.neutral_offsets["R_Elbow"][1] + 10)
        self.pose_crouch["L_Elbow"] = (self.neutral_offsets["L_Elbow"][0] + 10, self.neutral_offsets["L_Elbow"][1] + 10)
        self.pose_crouch["R_Wrist"] = (self.neutral_offsets["R_Wrist"][0] - 15, self.neutral_offsets["R_Wrist"][1] + 10)
        self.pose_crouch["L_Wrist"] = (self.neutral_offsets["L_Wrist"][0] + 15, self.neutral_offsets["L_Wrist"][1] + 10)
        self.pose_crouch["Head"] = (self.neutral_offsets["Head"][0], self.neutral_offsets["Head"][1] + self.MAX_CROUCH_DEPTH)
        self.pose_crouch["Neck"] = (self.neutral_offsets["Neck"][0], self.neutral_offsets["Neck"][1] + self.MAX_CROUCH_DEPTH)

        # Keyframe 2: Launch - extending upwards
        self.pose_launch = self.neutral_offsets.copy()
        self.pose_launch["Torso"] = (0, -self.MAX_JUMP_HEIGHT / 4) # Torso moving up past neutral height
        # Legs are extending, ankles pushing off
        self.pose_launch["R_Hip"] = (self.neutral_offsets["R_Hip"][0], self.neutral_offsets["R_Hip"][1] - self.MAX_CROUCH_DEPTH / 2)
        self.pose_launch["L_Hip"] = (self.neutral_offsets["L_Hip"][0], self.neutral_offsets["L_Hip"][1] - self.MAX_CROUCH_DEPTH / 2)
        self.pose_launch["R_Knee"] = (self.neutral_offsets["R_Knee"][0] - 5, self.neutral_offsets["R_Knee"][1] - self.MAX_CROUCH_DEPTH)
        self.pose_launch["L_Knee"] = (self.neutral_offsets["L_Knee"][0] + 5, self.neutral_offsets["L_Knee"][1] - self.MAX_CROUCH_DEPTH)
        self.pose_launch["R_Ankle"] = (self.neutral_offsets["R_Ankle"][0] - 10, self.neutral_offsets["R_Ankle"][1] - self.MAX_CROUCH_DEPTH - 20)
        self.pose_launch["L_Ankle"] = (self.neutral_offsets["L_Ankle"][0] + 10, self.neutral_offsets["L_Ankle"][1] - self.MAX_CROUCH_DEPTH - 20)
        # Arms swinging forward
        self.pose_launch["R_Shoulder"] = (self.neutral_offsets["R_Shoulder"][0] - 5, self.neutral_offsets["R_Shoulder"][1] - 10)
        self.pose_launch["L_Shoulder"] = (self.neutral_offsets["L_Shoulder"][0] + 5, self.neutral_offsets["L_Shoulder"][1] - 10)
        self.pose_launch["R_Elbow"] = (self.neutral_offsets["R_Elbow"][0] + 10, self.neutral_offsets["R_Elbow"][1] - 10)
        self.pose_launch["L_Elbow"] = (self.neutral_offsets["L_Elbow"][0] - 10, self.neutral_offsets["L_Elbow"][1] - 10)
        self.pose_launch["R_Wrist"] = (self.neutral_offsets["R_Wrist"][0] + 15, self.neutral_offsets["R_Wrist"][1] - 10)
        self.pose_launch["L_Wrist"] = (self.neutral_offsets["L_Wrist"][0] - 15, self.neutral_offsets["L_Wrist"][1] - 10)
        self.pose_launch["Head"] = (self.neutral_offsets["Head"][0], self.neutral_offsets["Head"][1] - self.MAX_JUMP_HEIGHT / 4)
        self.pose_launch["Neck"] = (self.neutral_offsets["Neck"][0], self.neutral_offsets["Neck"][1] - self.MAX_JUMP_HEIGHT / 4)

        # Keyframe 3: Peak Airborne - highest point in the air
        self.pose_peak = self.neutral_offsets.copy()
        self.pose_peak["Torso"] = (0, -self.MAX_JUMP_HEIGHT) # Torso at maximum height
        # Legs are slightly tucked/relaxed in air. Arms slightly forward, reflecting "sadman" (not high).
        self.pose_peak["R_Hip"] = (self.neutral_offsets["R_Hip"][0] + 10, self.neutral_offsets["R_Hip"][1] + 10)
        self.pose_peak["L_Hip"] = (self.neutral_offsets["L_Hip"][0] - 10, self.neutral_offsets["L_Hip"][1] + 10)
        self.pose_peak["R_Knee"] = (self.neutral_offsets["R_Knee"][0] + 20, self.neutral_offsets["R_Knee"][1] - 10)
        self.pose_peak["L_Knee"] = (self.neutral_offsets["L_Knee"][0] - 20, self.neutral_offsets["L_Knee"][1] - 10)
        self.pose_peak["R_Ankle"] = (self.neutral_offsets["R_Ankle"][0] + 30, self.neutral_offsets["R_Ankle"][1] - 30)
        self.pose_peak["L_Ankle"] = (self.neutral_offsets["L_Ankle"][0] - 30, self.neutral_offsets["L_Ankle"][1] - 30)
        # Arms slightly forward, relaxed
        self.pose_peak["R_Shoulder"] = (self.neutral_offsets["R_Shoulder"][0], self.neutral_offsets["R_Shoulder"][1] - 5)
        self.pose_peak["L_Shoulder"] = (self.neutral_offsets["L_Shoulder"][0], self.neutral_offsets["L_Shoulder"][1] - 5)
        self.pose_peak["R_Elbow"] = (self.neutral_offsets["R_Elbow"][0] + 5, self.neutral_offsets["R_Elbow"][1])
        self.pose_peak["L_Elbow"] = (self.neutral_offsets["L_Elbow"][0] - 5, self.neutral_offsets["L_Elbow"][1])
        self.pose_peak["R_Wrist"] = (self.neutral_offsets["R_Wrist"][0] + 10, self.neutral_offsets["R_Wrist"][1] + 5)
        self.pose_peak["L_Wrist"] = (self.neutral_offsets["L_Wrist"][0] - 10, self.neutral_offsets["L_Wrist"][1] + 5)
        self.pose_peak["Head"] = (self.neutral_offsets["Head"][0], self.neutral_offsets["Head"][1] - self.MAX_JUMP_HEIGHT)
        self.pose_peak["Neck"] = (self.neutral_offsets["Neck"][0], self.neutral_offsets["Neck"][1] - self.MAX_JUMP_HEIGHT)

        # Keyframe 4: Landing - absorbing impact
        self.pose_land = self.neutral_offsets.copy()
        self.pose_land["Torso"] = (0, self.MAX_CROUCH_DEPTH / 2) # Torso moving down to absorb
        # Legs are bending to absorb shock
        self.pose_land["R_Hip"] = (self.neutral_offsets["R_Hip"][0], self.neutral_offsets["R_Hip"][1] + self.MAX_CROUCH_DEPTH / 2 - 10)
        self.pose_land["L_Hip"] = (self.neutral_offsets["L_Hip"][0], self.neutral_offsets["L_Hip"][1] + self.MAX_CROUCH_DEPTH / 2 - 10)
        self.pose_land["R_Knee"] = (self.neutral_offsets["R_Knee"][0] + 5, self.neutral_offsets["R_Knee"][1] + self.MAX_CROUCH_DEPTH / 2 + 10)
        self.pose_land["L_Knee"] = (self.neutral_offsets["L_Knee"][0] - 5, self.neutral_offsets["L_Knee"][1] + self.MAX_CROUCH_DEPTH / 2 + 10)
        self.pose_land["R_Ankle"] = (self.neutral_offsets["R_Ankle"][0] + 10, self.neutral_offsets["R_Ankle"][1] + self.MAX_CROUCH_DEPTH / 2 + 20)
        self.pose_land["L_Ankle"] = (self.neutral_offsets["L_Ankle"][0] - 10, self.neutral_offsets["L_Ankle"][1] + self.MAX_CROUCH_DEPTH / 2 + 20)
        # Arms coming down
        self.pose_land["R_Shoulder"] = (self.neutral_offsets["R_Shoulder"][0] + 5, self.neutral_offsets["R_Shoulder"][1] + 5)
        self.pose_land["L_Shoulder"] = (self.neutral_offsets["L_Shoulder"][0] - 5, self.neutral_offsets["L_Shoulder"][1] + 5)
        self.pose_land["R_Elbow"] = (self.neutral_offsets["R_Elbow"][0] - 5, self.neutral_offsets["R_Elbow"][1] + 5)
        self.pose_land["L_Elbow"] = (self.neutral_offsets["L_Elbow"][0] + 5, self.neutral_offsets["L_Elbow"][1] + 5)
        self.pose_land["R_Wrist"] = (self.neutral_offsets["R_Wrist"][0] - 10, self.neutral_offsets["R_Wrist"][1] + 5)
        self.pose_land["L_Wrist"] = (self.neutral_offsets["L_Wrist"][0] + 10, self.neutral_offsets["L_Wrist"][1] + 5)
        self.pose_land["Head"] = (self.neutral_offsets["Head"][0], self.neutral_offsets["Head"][1] + self.MAX_CROUCH_DEPTH / 2)
        self.pose_land["Neck"] = (self.neutral_offsets["Neck"][0], self.neutral_offsets["Neck"][1] + self.MAX_CROUCH_DEPTH / 2)
        
        # Keyframe 5: Recovery - returning to standing pose
        self.pose_recover = self.neutral_offsets.copy() # Same as pose_stand for relative offsets

        # Define the sequence of keyframes and their normalized time segments [0.0, 1.0]
        # Each tuple: (keyframe_pose_dict, start_time_ratio, end_time_ratio)
        self.animation_sequence = [
            (self.pose_stand,     0.0,  0.05), # Brief initial stand
            (self.pose_crouch,    0.05, 0.25), # Crouch down
            (self.pose_launch,    0.25, 0.40), # Launch up
            (self.pose_peak,      0.40, 0.60), # Airborne peak
            (self.pose_land,      0.60, 0.75), # Land and absorb
            (self.pose_recover,   0.75, 0.95), # Recover to stand
            (self.pose_stand,     0.95, 1.00)  # Return to stand, completing the loop
        ]

        # Define the global Y-trajectory for the Torso root over the cycle
        # These values correspond to the Y-position relative to self.initial_y
        self.y_trajectory = [
            0, # 0.00: Stand height
            0, # 0.05: Still at stand height (start of crouch motion)
            self.MAX_CROUCH_DEPTH, # 0.25: Deepest crouch
            -self.MAX_JUMP_HEIGHT / 4, # 0.40: Launch phase (already moving up)
            -self.MAX_JUMP_HEIGHT, # 0.60: Peak airborne height
            self.MAX_CROUCH_DEPTH / 2, # 0.75: Landing absorption
            0, # 0.95: Recovery to stand height
            0  # 1.00: Back to stand height for loop
        ]
        # Normalized times corresponding to the y_trajectory points
        self.y_trajectory_times = [
            0.0, 0.05, 0.25, 0.40, 0.60, 0.75, 0.95, 1.0
        ]


    def _update_joint_positions_from_offsets(self, relative_offsets):
        """
        Calculates global screen coordinates for all joints based on the
        figure's current global root (Torso) position and joint offsets.
        """
        for name, offset in relative_offsets.items():
            self.current_joints[name] = (self.x + offset[0], self.y + offset[1])

    def get_joint_coords(self):
        """Returns the current global coordinates of all joints."""
        return self.current_joints

    def animate(self, frame_count, total_frames_per_cycle):
        """
        Updates the figure's position and pose based on the current frame
        in the animation cycle.
        """
        
        # Calculate normalized time within the animation cycle (loops from 0.0 to 1.0)
        t = (frame_count % total_frames_per_cycle) / total_frames_per_cycle 

        # 1. Update global X position (constant forward motion)
        self.x = self.initial_x + frame_count * self.FORWARD_SPEED

        # 2. Interpolate global Y position for the Torso root
        current_y_offset_from_base = 0
        for i in range(len(self.y_trajectory_times) - 1):
            if self.y_trajectory_times[i] <= t < self.y_trajectory_times[i+1]:
                t_segment_start = self.y_trajectory_times[i]
                t_segment_end = self.y_trajectory_times[i+1]
                y_segment_start = self.y_trajectory[i]
                y_segment_end = self.y_trajectory[i+1]

                segment_duration = t_segment_end - t_segment_start
                if segment_duration == 0: # Handle instantaneous segments to prevent division by zero
                    local_t_y = 0
                else:
                    local_t_y = (t - t_segment_start) / segment_duration
                
                # Apply easing for smoother Y motion transitions
                local_t_y_eased = ease_in_out_quad(local_t_y)
                current_y_offset_from_base = y_segment_start + (y_segment_end - y_segment_start) * local_t_y_eased
                break
        # Special handling for t exactly 1.0 to ensure loop closure
        if t == 1.0:
            current_y_offset_from_base = self.y_trajectory[-1]

        self.y = self.initial_y + current_y_offset_from_base

        # 3. Interpolate relative joint positions (body pose relative to Torso)
        interp_offsets = {}
        kf1 = None # First keyframe for interpolation
        kf2 = None # Second keyframe for interpolation
        local_t_pose = 0 # Normalized time within the current keyframe segment

        # Find the two keyframes that bracket the current normalized time 't'
        for i in range(len(self.animation_sequence)):
            current_kf_def = self.animation_sequence[i]
            # Get the next keyframe, wrapping around to the beginning for seamless looping
            next_kf_def = self.animation_sequence[(i + 1) % len(self.animation_sequence)] 

            start_t_ratio = current_kf_def[1]
            end_t_ratio = current_kf_def[2]

            # Check if 't' falls within the current segment
            # The last segment needs special handling for t=1.0 to ensure it transitions to the first
            if start_t_ratio <= t < end_t_ratio or (i == len(self.animation_sequence) - 1 and t >= start_t_ratio):
                kf1 = current_kf_def[0]
                kf2 = next_kf_def[0]
                
                segment_duration = end_t_ratio - start_t_ratio
                if segment_duration == 0:
                    local_t_pose = 0
                else:
                    local_t_pose = (t - start_t_ratio) / segment_duration
                
                # If at the very end of the cycle, adjust local_t_pose to ensure smooth transition to start
                if i == len(self.animation_sequence) - 1 and t >= start_t_ratio:
                    segment_duration = 1.0 - start_t_ratio
                    local_t_pose = (t - start_t_ratio) / segment_duration if segment_duration > 0 else 0

                break

        # Fallback if no segment matched (should ideally not happen with a well-defined sequence)
        if kf1 is None:
            kf1 = self.pose_stand 
            kf2 = self.pose_stand
            local_t_pose = 0

        # Apply easing for smoother pose transitions
        local_t_pose_eased = ease_in_out_quad(local_t_pose)

        # Interpolate positions for each joint
        for joint_name in JOINT_NAMES:
            # Use .get with default (0,0) in case a joint is somehow missing from a keyframe
            x1, y1 = kf1.get(joint_name, (0,0)) 
            x2, y2 = kf2.get(joint_name, (0,0))
            
            interp_x = x1 + (x2 - x1) * local_t_pose_eased
            interp_y = y1 + (y2 - y1) * local_t_pose_eased
            interp_offsets[joint_name] = (interp_x, interp_y)
        
        self._update_joint_positions_from_offsets(interp_offsets)


# Setup the HumanFigure instance
# Start the figure on the left side of the screen, centered vertically
figure = HumanFigure(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

# Animation parameters
FPS = 30 # Frames per second
clock = pygame.time.Clock() # Pygame clock to control frame rate
TOTAL_FRAMES_PER_CYCLE = FPS * 2 # One complete jump cycle lasts 2 seconds

frame_counter = 0 # Tracks the current frame number

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Allow quitting with ESC key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Update animation state for the current frame
    figure.animate(frame_counter, TOTAL_FRAMES_PER_CYCLE)
    frame_counter += 1

    # Drawing section
    screen.fill(BLACK) # Fill the background with solid black

    # Get the current global positions of all joints
    current_joint_coords = figure.get_joint_coords()
    
    # Draw each point as a white circle
    for name, pos in current_joint_coords.items():
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), POINT_RADIUS)

    pygame.display.flip() # Update the full display surface to show the drawn frame

    clock.tick(FPS) # Cap the frame rate to the specified FPS

pygame.quit() # Uninitialize Pygame and exit
