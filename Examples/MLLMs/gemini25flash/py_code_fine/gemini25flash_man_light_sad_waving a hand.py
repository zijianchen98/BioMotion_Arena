
import pygame
import math

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DOT_RADIUS = 5
FPS = 60

# Scaling factor for the figure size, making it larger or smaller
SCALE_FACTOR = 1.5

# Define approximate lengths for body segments (in arbitrary units, will be scaled)
neck_length_base = 15
head_radius_base = 15 # Head is represented by a single point, this is its 'length' from neck
torso_height_base = 80 # From chest to hips
shoulder_width_base = 60 # Full width from shoulder to shoulder
upper_arm_length_base = 50
forearm_length_base = 40
thigh_length_base = 60
shin_length_base = 60

# Scaled lengths
neck_length_scaled = neck_length_base * SCALE_FACTOR
head_radius_scaled = head_radius_base * SCALE_FACTOR
torso_height_scaled = torso_height_base * SCALE_FACTOR
shoulder_width_scaled = shoulder_width_base * SCALE_FACTOR
upper_arm_length_scaled = upper_arm_length_base * SCALE_FACTOR
forearm_length_scaled = forearm_length_base * SCALE_FACTOR
thigh_length_scaled = thigh_length_base * SCALE_FACTOR
shin_length_scaled = shin_length_base * SCALE_FACTOR

# Joint mapping (total 15 points as per example image)
# These are symbolic names mapped to their numerical index for a consistent order.
JOINT_NAMES = [
    'head',          # 0
    'neck',          # 1 (base of neck, top of torso)
    'shoulder_L',    # 2
    'shoulder_R',    # 3
    'elbow_L',       # 4
    'elbow_R',       # 5
    'wrist_L',       # 6
    'wrist_R',       # 7
    'chest',         # 8 (mid-torso/sternum)
    'hip_L',         # 9
    'hip_R',         # 10
    'knee_L',        # 11
    'knee_R',        # 12
    'ankle_L',       # 13
    'ankle_R'        # 14
]
JOINT_MAP = {name: i for i, name in enumerate(JOINT_NAMES)}

# Dictionary to store the current (x, y) coordinates of each joint.
# Initialized with dummy values, will be updated each frame.
current_positions = {name: [0.0, 0.0] for name in JOINT_NAMES}

# Animation parameters for the "waving a hand" motion
WAVE_SPEED = 0.08  # Controls the speed of the waving cycle (radians per frame)
# Upper arm motion: small up/down swing
UPPER_ARM_SWING_AMPLITUDE = math.radians(5) 
UPPER_ARM_BASE_ANGLE = math.radians(70) # Angle of upper arm from horizontal right (70 degrees is slightly forward and down)

# Elbow motion: primary hand waving (flexion/extension)
ELBOW_WAVE_AMPLITUDE = math.radians(40) # How much the elbow opens/closes during the wave
ELBOW_BASE_BEND_ANGLE = math.radians(70) # Base bend angle of the elbow (from straight arm configuration)

def update_skeleton_positions(frame_count):
    """
    Updates the absolute (x,y) positions of all 15 joints for the current frame.
    Applies the "waving a hand" motion to the right arm.
    """
    global current_positions

    # Fixed base point for the figure: the 'chest' joint.
    # This point acts as the anchor for the upper body and determines the overall position on screen.
    chest_x_anchor = SCREEN_WIDTH // 2
    chest_y_anchor = SCREEN_HEIGHT // 2 - 50 # Slightly above center to allow for legs below

    current_positions[JOINT_MAP['chest']] = [chest_x_anchor, chest_y_anchor]

    # --- Calculate positions for static body parts (torso, head, left arm, legs) ---
    # These parts maintain a fixed relative pose to the 'chest' anchor point.

    # Neck and Head: Vertically above the chest
    current_positions[JOINT_MAP['neck']][0] = chest_x_anchor
    current_positions[JOINT_MAP['neck']][1] = chest_y_anchor - neck_length_scaled
    current_positions[JOINT_MAP['head']][0] = current_positions[JOINT_MAP['neck']][0]
    current_positions[JOINT_MAP['head']][1] = current_positions[JOINT_MAP['neck']][1] - head_radius_scaled

    # Hips: Vertically below the chest and spread horizontally
    # Approx y-offset for hips from chest.
    hip_y_offset_from_chest = (torso_height_scaled / 2) # Hips are below mid-torso
    current_positions[JOINT_MAP['hip_L']][0] = chest_x_anchor - shoulder_width_scaled / 2
    current_positions[JOINT_MAP['hip_L']][1] = chest_y_anchor + hip_y_offset_from_chest
    current_positions[JOINT_MAP['hip_R']][0] = chest_x_anchor + shoulder_width_scaled / 2
    current_positions[JOINT_MAP['hip_R']][1] = chest_y_anchor + hip_y_offset_from_chest
    
    # Legs: Straight down from hips
    # Left Leg
    current_positions[JOINT_MAP['knee_L']][0] = current_positions[JOINT_MAP['hip_L']][0]
    current_positions[JOINT_MAP['knee_L']][1] = current_positions[JOINT_MAP['hip_L']][1] + thigh_length_scaled
    current_positions[JOINT_MAP['ankle_L']][0] = current_positions[JOINT_MAP['knee_L']][0]
    current_positions[JOINT_MAP['ankle_L']][1] = current_positions[JOINT_MAP['knee_L']][1] + shin_length_scaled

    # Right Leg
    current_positions[JOINT_MAP['knee_R']][0] = current_positions[JOINT_MAP['hip_R']][0]
    current_positions[JOINT_MAP['knee_R']][1] = current_positions[JOINT_MAP['hip_R']][1] + thigh_length_scaled
    current_positions[JOINT_MAP['ankle_R']][0] = current_positions[JOINT_MAP['knee_R']][0]
    current_positions[JOINT_MAP['ankle_R']][1] = current_positions[JOINT_MAP['knee_R']][1] + shin_length_scaled

    # Left Arm: Hanging straight down from shoulder
    shoulder_y_offset_from_chest = -10 * SCALE_FACTOR # Shoulders slightly above chest anchor
    current_positions[JOINT_MAP['shoulder_L']][0] = chest_x_anchor - shoulder_width_scaled / 2
    current_positions[JOINT_MAP['shoulder_L']][1] = chest_y_anchor + shoulder_y_offset_from_chest
    current_positions[JOINT_MAP['elbow_L']][0] = current_positions[JOINT_MAP['shoulder_L']][0]
    current_positions[JOINT_MAP['elbow_L']][1] = current_positions[JOINT_MAP['shoulder_L']][1] + upper_arm_length_scaled
    current_positions[JOINT_MAP['wrist_L']][0] = current_positions[JOINT_MAP['elbow_L']][0]
    current_positions[JOINT_MAP['wrist_L']][1] = current_positions[JOINT_MAP['elbow_L']][1] + forearm_length_scaled

    # --- Calculate positions for the waving Right Arm (dynamic part) ---
    # The right shoulder is also positioned relative to the chest.
    shoulder_R_x = chest_x_anchor + shoulder_width_scaled / 2
    shoulder_R_y = chest_y_anchor + shoulder_y_offset_from_chest # Same level as left shoulder
    current_positions[JOINT_MAP['shoulder_R']] = [shoulder_R_x, shoulder_R_y]

    # Time parameter for smooth sinusoidal animation
    t = (frame_count * WAVE_SPEED) % (2 * math.pi)

    # 1. Upper Arm (shoulder_R to elbow_R): Subtle up/down swing
    # The angle is relative to the global X-axis (0: right, 90: down, 180: left, 270: up).
    upper_arm_angle_current = UPPER_ARM_BASE_ANGLE + UPPER_ARM_SWING_AMPLITUDE * math.sin(t / 2) # Slower swing

    # Calculate elbow position based on shoulder and upper arm angle/length
    elbow_R_x = shoulder_R_x + upper_arm_length_scaled * math.cos(upper_arm_angle_current)
    elbow_R_y = shoulder_R_y + upper_arm_length_scaled * math.sin(upper_arm_angle_current)
    current_positions[JOINT_MAP['elbow_R']] = [elbow_R_x, elbow_R_y]

    # 2. Forearm (elbow_R to wrist_R): Main "waving" motion via elbow flexion/extension
    # The angle of the forearm is relative to the upper arm.
    # Base bend + sinusoidal oscillation. (1 + sin(t*2)) ensures movement from 0 to max_bend.
    elbow_bend_oscillation = (ELBOW_WAVE_AMPLITUDE / 2) * (1 + math.sin(t * 2)) # Faster oscillation
    forearm_relative_angle_from_upper_arm = ELBOW_BASE_BEND_ANGLE + elbow_bend_oscillation

    # Calculate the absolute angle of the forearm. It's the upper arm's angle plus the relative bend.
    forearm_absolute_angle = upper_arm_angle_current + forearm_relative_angle_from_upper_arm

    # Calculate wrist position based on elbow and forearm angle/length
    wrist_R_x = elbow_R_x + forearm_length_scaled * math.cos(forearm_absolute_angle)
    wrist_R_y = elbow_R_y + forearm_length_scaled * math.sin(forearm_absolute_angle)
    current_positions[JOINT_MAP['wrist_R']] = [wrist_R_x, wrist_R_y]

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion Stimulus: Waving Hand")
clock = pygame.time.Clock()

# --- Main animation loop ---
running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear screen with black background

    # Update point positions for the current frame
    update_skeleton_positions(frame_count)

    # Draw all 15 white point-lights
    for joint_name in JOINT_NAMES:
        pos = current_positions[joint_name]
        pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), DOT_RADIUS)

    pygame.display.flip() # Update the full display Surface to the screen

    frame_count += 1
    clock.tick(FPS) # Control the frame rate

pygame.quit()
