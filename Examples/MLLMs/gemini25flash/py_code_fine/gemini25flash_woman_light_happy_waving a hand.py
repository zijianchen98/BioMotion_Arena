
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus - Waving Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Biomechanical Model - Joint Definitions
# These indices correspond to the 15 points in the example image
JOINT_HEAD = 0
JOINT_NECK = 1
JOINT_L_SHOULDER = 2
JOINT_R_SHOULDER = 3
JOINT_L_ELBOW = 4
JOINT_R_ELBOW = 5
JOINT_L_WRIST = 6
JOINT_R_WRIST = 7
JOINT_MID_TORSO = 8 # This is the central point between shoulders and hips
JOINT_L_HIP = 9
JOINT_R_HIP = 10
JOINT_L_KNEE = 11
JOINT_R_KNEE = 12
JOINT_L_ANKLE = 13
JOINT_R_ANKLE = 14

# This class represents a joint point in the skeleton for forward kinematics
class KinematicJoint:
    def __init__(self, name, parent_name=None, length=0.0, initial_relative_angle_deg=0.0):
        self.name = name
        self.parent_name = parent_name # Name (or index) of parent joint
        self.length = float(length) # Length of the segment from parent to this joint
        # Angle of this segment relative to its parent's segment orientation (in radians)
        # 0 deg means straight, positive is clockwise, negative is counter-clockwise.
        self.relative_angle_rad = math.radians(float(initial_relative_angle_deg))
        
        self.absolute_angle_rad = 0.0 # Absolute orientation of this segment with respect to global X-axis
        self.pos = [0.0, 0.0] # Current (x, y) position

    def update_position_and_angle(self, parent_joint=None):
        if parent_joint is None: # This is the root joint
            # Root's relative angle defines its absolute orientation (e.g., body upright)
            self.absolute_angle_rad = self.relative_angle_rad 
            # Root's position is set externally (e.g., initial_mid_torso_x, initial_mid_torso_y)
        else:
            # Child's absolute angle is parent's absolute angle plus child's relative angle
            self.absolute_angle_rad = parent_joint.absolute_angle_rad + self.relative_angle_rad
            # Calculate position based on parent's position, segment length, and absolute angle
            self.pos[0] = parent_joint.pos[0] + self.length * math.cos(self.absolute_angle_rad)
            self.pos[1] = parent_joint.pos[1] + self.length * math.sin(self.absolute_angle_rad)

def create_skeleton(scale=70):
    joints = {}
    
    # Define segment lengths (proportional values, scaled to pixels)
    L_NECK_MID_TORSO = 0.5 * scale
    L_HEAD_NECK = 0.4 * scale
    L_SHOULDER_NECK = 0.3 * scale 
    L_UPPER_ARM = 0.7 * scale 
    L_FOREARM = 0.6 * scale 
    L_HIP_MID_TORSO = 0.3 * scale 
    L_THIGH = 0.8 * scale 
    L_SHIN = 0.7 * scale 

    # Root joint: Mid-Torso. Its absolute position will be set manually.
    # Its 'relative angle' defines the initial upright orientation of the spine segment from it.
    # -90 deg for relative angle means it points 'up' (relative to its own internal frame, which we orient globally).
    joints[JOINT_MID_TORSO] = KinematicJoint("Mid_Torso", length=0, initial_relative_angle_deg=-90) # Upright orientation

    # Torso and Head (relative to Mid-Torso, which points 'up')
    joints[JOINT_NECK] = KinematicJoint("Neck", JOINT_MID_TORSO, L_NECK_MID_TORSO, 0) # Straight up from Mid-Torso
    joints[JOINT_HEAD] = KinematicJoint("Head", JOINT_NECK, L_HEAD_NECK, 0) # Straight up from Neck

    # Shoulders (relative to Neck, which points 'up')
    # Shoulder segments extend sideways from the Neck joint.
    # Neck is up (-90 abs). To go left, relative angle is -90. To go right, relative angle is 90.
    joints[JOINT_L_SHOULDER] = KinematicJoint("L_Shoulder", JOINT_NECK, L_SHOULDER_NECK, -90) # Left from Neck
    joints[JOINT_R_SHOULDER] = KinematicJoint("R_Shoulder", JOINT_NECK, L_SHOULDER_NECK, 90) # Right from Neck

    # Arms (initially hanging down)
    # Shoulder segment is horizontal. To hang down, relative angle is 90.
    joints[JOINT_L_ELBOW] = KinematicJoint("L_Elbow", JOINT_L_SHOULDER, L_UPPER_ARM, 90) 
    joints[JOINT_R_ELBOW] = KinematicJoint("R_Elbow", JOINT_R_SHOULDER, L_UPPER_ARM, 90)
    
    # Forearm hangs straight from upper arm. Relative angle 0.
    joints[JOINT_L_WRIST] = KinematicJoint("L_Wrist", JOINT_L_ELBOW, L_FOREARM, 0)
    joints[JOINT_R_WRIST] = KinematicJoint("R_WRIST", JOINT_R_ELBOW, L_FOREARM, 0)

    # Hips (relative to Mid-Torso, which points 'up')
    # Hips extend down and out from the central torso point.
    # From an 'up' orientation, 90+45 (135) is down-left; 90-45 (45) is down-right.
    joints[JOINT_L_HIP] = KinematicJoint("L_Hip", JOINT_MID_TORSO, L_HIP_MID_TORSO, 90 + 45) 
    joints[JOINT_R_HIP] = KinematicJoint("R_Hip", JOINT_MID_TORSO, L_HIP_MID_TORSO, 90 - 45)

    # Legs (initially straight down from hips)
    # Hip segment is already pointing down-out. Legs extend straight from hip. Relative angle 0.
    joints[JOINT_L_KNEE] = KinematicJoint("L_Knee", JOINT_L_HIP, L_THIGH, 0) 
    joints[JOINT_R_KNEE] = KinematicJoint("R_KNEE", JOINT_R_HIP, L_THIGH, 0)
    
    joints[JOINT_L_ANKLE] = KinematicJoint("L_Ankle", JOINT_L_KNEE, L_SHIN, 0) 
    joints[JOINT_R_ANKLE] = KinematicJoint("R_Ankle", JOINT_R_KNEE, L_SHIN, 0)

    # Order for updating positions (children after parents to ensure correct kinematic chain calculation)
    update_order = [
        JOINT_MID_TORSO, # Root
        JOINT_NECK, JOINT_L_HIP, JOINT_R_HIP, # Children of Mid-Torso
        JOINT_HEAD, JOINT_L_SHOULDER, JOINT_R_SHOULDER, # Children of Neck
        JOINT_L_ELBOW, JOINT_R_ELBOW, # Children of Shoulders
        JOINT_L_WRIST, JOINT_R_WRIST, # Children of Elbows
        JOINT_L_KNEE, JOINT_R_KNEE, # Children of Hips
        JOINT_L_ANKLE, JOINT_R_ANKLE # Children of Knees
    ]
    
    return joints, update_order

# Create the skeleton once at startup
skeleton_joints, update_order = create_skeleton(scale=70) # Global scale factor for the figure size

# Initial absolute position for the root (Mid-Torso)
initial_mid_torso_x = WIDTH // 2
initial_mid_torso_y = HEIGHT // 2 + skeleton_joints[JOINT_MID_TORSO].length + 70 # Centered and slightly low

# Animation parameters
animation_speed = 0.05 # Controls overall animation speed
wave_frequency = 1.5 # How many full wave cycles per animation speed unit
# Wave amplitudes (in radians)
WAVE_AMPLITUDE_SHOULDER_LIFT = math.radians(110) # How high the arm lifts (from hanging 90 deg to 90-110 = -20)
WAVE_AMPLITUDE_SHOULDER_SWING = math.radians(40) # How much the arm swings forward/backward
WAVE_AMPLITUDE_ELBOW_BEND = math.radians(45) # How much the elbow bends (e.g., from 90 to 90 +/- 45)
WAVE_AMPLITUDE_WRIST_FLICK = math.radians(30) # Wrist flick amplitude

# Subtle body sway for naturalness
SWAY_AMPLITUDE_X = 0.01 * 70 # Small horizontal sway
SWAY_AMPLITUDE_Y = 0.005 * 70 # Small vertical bob
SWAY_SPEED_X = 0.02
SWAY_SPEED_Y = 0.04

# Game loop
running = True
clock = pygame.time.Clock()
frame_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_time += 1
    time_factor = frame_time * animation_speed

    # Update root joint's absolute position for subtle body sway
    skeleton_joints[JOINT_MID_TORSO].pos[0] = initial_mid_torso_x + SWAY_AMPLITUDE_X * math.sin(time_factor * SWAY_SPEED_X)
    skeleton_joints[JOINT_MID_TORSO].pos[1] = initial_mid_torso_y + SWAY_AMPLITUDE_Y * math.cos(time_factor * SWAY_SPEED_Y)

    # --- Animate Waving Arm (Right Arm) ---
    # `cycle_value` goes from 0 to 2*pi over a wave cycle
    cycle_value = (time_factor * wave_frequency) % (2 * math.pi)

    # 1. Right Shoulder animation: Lifting the arm and swinging it
    # Initial R_SHOULDER relative angle to Neck: 90 deg (arm right).
    # To lift the arm: decrease the relative angle (e.g., from 90 to -20).
    # We want a smooth lift and then an oscillation around the lifted position.
    
    # Lift component: uses a cosine wave to go from 0 (arm down) to 1 (arm lifted) over half cycle.
    # This creates a smooth lift and lower effect.
    lift_progress = (0.5 - 0.5 * math.cos(cycle_value)) 
    # If using full cycle for wave motion, arm can be up during wave, then lower.
    # For a continuous wave, let arm stay mostly up.
    
    # Let's define the base arm lift relative angle. Arm starts at 90 (relative to neck, pointing right).
    # To lift, this angle should decrease. E.g., to -20 means 110 degrees of lift.
    base_lifted_angle_rel_shoulder = math.radians(-20) # Target lifted position (up-right)
    
    # Simple continuous wave: shoulder swings back and forth from the lifted position
    shoulder_swing = WAVE_AMPLITUDE_SHOULDER_SWING * math.sin(cycle_value)
    
    # Interpolate from initial hanging (90 deg) to lifted (-20 deg) over the first part of the cycle,
    # then maintain the lifted position and add the swing.
    # Let's simplify and make the arm just stay up and wave, for a clear continuous action.
    # The shoulder is lifted to `base_lifted_angle_rel_shoulder` and swings.
    skeleton_joints[JOINT_R_SHOULDER].relative_angle_rad = base_lifted_angle_rel_shoulder + shoulder_swing

    # 2. Right Elbow animation: Bending and extending
    # Initial R_ELBOW relative angle to R_SHOULDER: 90 deg (arm straight down from shoulder).
    # For waving, the elbow typically bends and extends rhythmically.
    # An angle of 0 is straight, 90 is L-shape, 180 is bent back.
    # Oscillate the elbow's relative angle around a slightly bent position (e.g., 90 deg for L-shape).
    elbow_bend_oscillation = WAVE_AMPLITUDE_ELBOW_BEND * math.sin(cycle_value + math.pi/2) # Phase shift for natural look
    skeleton_joints[JOINT_R_ELBOW].relative_angle_rad = math.radians(90) + elbow_bend_oscillation

    # 3. Right Wrist animation: Small flicking motion
    # Initial R_WRIST relative angle to R_ELBOW: 0 deg (straight from forearm).
    # Add a faster oscillation for a subtle wrist movement.
    wrist_flick_oscillation = WAVE_AMPLITUDE_WRIST_FLICK * math.sin(cycle_value * 2) # Faster movement
    skeleton_joints[JOINT_R_WRIST].relative_angle_rad = wrist_flick_oscillation

    # Subtle movements for other body parts for naturalness:
    # Head subtle bob/turn
    head_bob_offset = math.radians(3) * math.sin(time_factor * SWAY_SPEED_Y * 0.5)
    skeleton_joints[JOINT_HEAD].relative_angle_rad = head_bob_offset

    # Legs (slight knee bend, subtle weight shift)
    # Both knees slightly bend and extend in sync with body sway
    knee_bend_offset = math.radians(3) * (0.5 + 0.5 * math.cos(time_factor * SWAY_SPEED_Y * 1.5)) # Small bend always positive
    skeleton_joints[JOINT_L_KNEE].relative_angle_rad = knee_bend_offset
    skeleton_joints[JOINT_R_KNEE].relative_angle_rad = knee_bend_offset

    # --- Update all joint positions based on the new angles ---
    # The root joint's position is updated directly. Its update_position_and_angle call sets its own abs angle.
    skeleton_joints[JOINT_MID_TORSO].update_position_and_angle(None)
    
    # Update children joints based on their parents' new positions and orientations
    for joint_idx in update_order:
        joint = skeleton_joints[joint_idx]
        if joint.parent_name is not None:
            parent_joint = skeleton_joints[joint.parent_name]
            joint.update_position_and_angle(parent_joint)

    # --- Drawing ---
    SCREEN.fill(BLACK) # Black background
    
    # Draw white circles for each joint point
    for joint_idx in update_order:
        joint = skeleton_joints[joint_idx]
        pygame.draw.circle(SCREEN, WHITE, (int(joint.pos[0]), int(joint.pos[1])), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60) # Limit to 60 frames per second

pygame.quit()
