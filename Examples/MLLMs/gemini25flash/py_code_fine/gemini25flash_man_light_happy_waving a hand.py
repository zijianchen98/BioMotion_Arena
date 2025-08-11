
import pygame
import math
import numpy as np

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Human body proportions (relative to a fixed total height for consistency)
UNIT_SCALE = 150  # Represents the approximate total height of the figure in pixels

# Define bone lengths and segment offsets based on UNIT_SCALE
# These proportions are rough estimates to create a human-like figure
PROPORTIONS = {
    "head_radius": 0.05,
    "neck_length": 0.05,  # From upper torso (neck base) to head center
    "shoulder_width": 0.25,
    "hip_width": 0.2,
    "torso_upper": 0.15,  # From mid torso (pelvis) to upper torso (neck base)
    "upper_arm": 0.15,
    "forearm": 0.15,
    "thigh": 0.2,
    "shin": 0.2,
}

bone_lengths = {k: v * UNIT_SCALE for k, v in PROPORTIONS.items()}

# Point indices mapping to logical body parts based on the example image:
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Wrist
# 6: Right Wrist
# 7: Upper Torso (Neck Base, just below head, between shoulders)
# 8: Mid Torso (Pelvis/Waist, between elbows/wrists and hips)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

# Base position for the figure: centered horizontally, ankles near the bottom
figure_center_x = SCREEN_WIDTH // 2
figure_base_y = SCREEN_HEIGHT * 0.85  # Y-coordinate for the ankles

# Calculate the initial static positions for the human figure (rest pose)
def get_static_pose_points():
    points = {}

    # Mid Torso (8) is our central anchor for the lower body (pelvis/waist)
    # Its Y-coordinate is determined by pushing it up from the desired ankle position
    mid_torso_y = figure_base_y - bone_lengths["shin"] - bone_lengths["thigh"]
    points[8] = np.array([figure_center_x, mid_torso_y])

    # Upper Torso (7) (neck base)
    points[7] = points[8] - np.array([0, bone_lengths["torso_upper"]])

    # Head (0)
    points[0] = points[7] - np.array([0, bone_lengths["neck_length"]])

    # Shoulders (1, 2) - placed horizontally relative to Upper Torso (7)
    points[1] = points[7] - np.array([bone_lengths["shoulder_width"] / 2, 0])
    points[2] = points[7] + np.array([bone_lengths["shoulder_width"] / 2, 0])

    # Hips (9, 10) - placed horizontally relative to Mid Torso (8)
    points[9] = points[8] - np.array([bone_lengths["hip_width"] / 2, 0])
    points[10] = points[8] + np.array([bone_lengths["hip_width"] / 2, 0])

    # Initial arm positions (straight down from shoulders)
    # The default orientation for bone segments is assumed to be straight down from their parent joint.
    points[3] = points[1] + np.array([0, bone_lengths["upper_arm"]])  # Left Elbow
    points[5] = points[3] + np.array([0, bone_lengths["forearm"]])  # Left Wrist
    points[4] = points[2] + np.array([0, bone_lengths["upper_arm"]])  # Right Elbow
    points[6] = points[4] + np.array([0, bone_lengths["forearm"]])  # Right Wrist

    # Initial leg positions (straight down from hips)
    points[11] = points[9] + np.array([0, bone_lengths["thigh"]])  # Left Knee
    points[13] = points[11] + np.array([0, bone_lengths["shin"]])  # Left Ankle
    points[12] = points[10] + np.array([0, bone_lengths["thigh"]])  # Right Knee
    points[14] = points[12] + np.array([0, bone_lengths["shin"]])  # Right Ankle

    return points

# Store the static rest pose to calculate animated positions relative to it
static_points_ref = get_static_pose_points()

# Function to calculate new point positions based on animation time
def calculate_animated_points(animation_time):
    # Start with a copy of the static rest pose
    animated_points = static_points_ref.copy()

    # --- Animate Right Arm (Waving) ---
    # Angles are defined relative to the parent segment, where 0 degrees is along the positive X-axis
    # (pointing right), and increasing angles are counter-clockwise.
    # A segment pointing straight down (its default rest position) corresponds to math.pi / 2 (90 degrees).

    # 1. Shoulder Angle (controls lifting and swinging of the entire arm)
    # The arm is first lifted to a base position (e.g., 45 degrees forward from straight down).
    # This base position corresponds to an angle of `math.pi/2 - math.radians(45) = math.pi/4`.
    base_shoulder_angle = math.pi / 2 - math.radians(45)

    # Then, oscillate the shoulder angle for the back-and-forth 'swinging' part of the wave.
    shoulder_swing_amplitude = math.radians(20)  # Max deviation from base angle
    shoulder_swing_frequency = 1.0  # Hz (1 full swing cycle per second)
    
    # Use sine wave for smooth oscillation
    current_shoulder_angle = base_shoulder_angle + shoulder_swing_amplitude * math.sin(animation_time * shoulder_swing_frequency * 2 * math.pi)

    # 2. Elbow Angle (controls bending and straightening of the forearm)
    # The elbow angle is relative to the upper arm. 0 degrees means a straight arm.
    # Positive angle bends the elbow (forearm moves towards the upper arm).
    
    # A wave typically involves the elbow bending and straightening, from mostly straight to moderately bent.
    base_elbow_angle = 0  # Start with elbow relatively straight
    elbow_bend_amplitude = math.radians(90)  # Max bend: 90 degrees
    elbow_bend_frequency = 2.0  # Hz (faster than shoulder swing for more prominent hand motion)
    
    # Use (1 - cos(x))/2 to get a value that goes from 0 to 1 and back smoothly (like a pulse).
    current_elbow_angle = base_elbow_angle + elbow_bend_amplitude * (1 - math.cos(animation_time * elbow_bend_frequency * 2 * math.pi)) / 2
    
    # Calculate Right Elbow (4) position:
    # Relative to Right Shoulder (2). The upper arm's orientation is `current_shoulder_angle`.
    arm_x = bone_lengths["upper_arm"] * math.cos(current_shoulder_angle)
    arm_y = bone_lengths["upper_arm"] * math.sin(current_shoulder_angle)
    animated_points[4] = animated_points[2] + np.array([arm_x, arm_y])

    # Calculate Right Wrist (6) position:
    # Relative to Right Elbow (4). The forearm's orientation is `current_shoulder_angle + current_elbow_angle`.
    forearm_x = bone_lengths["forearm"] * math.cos(current_shoulder_angle + current_elbow_angle)
    forearm_y = bone_lengths["forearm"] * math.sin(current_shoulder_angle + current_elbow_angle)
    animated_points[6] = animated_points[4] + np.array([forearm_x, forearm_y])

    # --- Subtle Body Sway (for "happyman" and naturalness) ---
    # Apply a slight horizontal and vertical sway to the entire figure.
    sway_amplitude_x = 3  # pixels
    sway_frequency_x = 0.7  # Hz
    sway_amplitude_y = 1  # pixels
    sway_frequency_y = 0.5  # Hz

    sway_x = sway_amplitude_x * math.sin(animation_time * sway_frequency_x * 2 * math.pi)
    sway_y = sway_amplitude_y * math.sin(animation_time * sway_frequency_y * 2 * math.pi)

    # Apply sway as a global translation to all points
    for i in range(15):
        if i in animated_points:
            animated_points[i] += np.array([sway_x, sway_y])

    # Convert all point coordinates to integer tuples, as required by pygame.draw.circle
    return {k: (int(v[0]), int(v[1])) for k, v in animated_points.items()}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion - Waving Man")

clock = pygame.time.Clock()
FPS = 60  # Frames per second for smooth animation

running = True
start_time = pygame.time.get_ticks()  # Get initial time for animation timing

while running:
    # Event handling (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current animation time in seconds
    current_time_ms = pygame.time.get_ticks() - start_time
    animation_time = current_time_ms / 1000.0

    # Get updated positions for all 15 points
    current_point_positions = calculate_animated_points(animation_time)

    # Drawing section
    screen.fill(BLACK)  # Clear the screen with a black background

    # Draw each point as a white circle
    for i in range(15):  # Iterate through point indices 0 to 14
        if i in current_point_positions:  # Ensure the point exists
            pygame.draw.circle(screen, WHITE, current_point_positions[i], POINT_RADIUS)

    pygame.display.flip()  # Update the full display surface to the screen
    clock.tick(FPS)  # Control the frame rate

pygame.quit()
