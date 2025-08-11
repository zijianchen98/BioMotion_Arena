
import pygame
import math
import numpy as np

# --- Pygame Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
POINT_RADIUS = 5  # Size of the white point-lights
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down (Heavy Weight)")
clock = pygame.time.Clock()

# --- Point Definitions (15 points based on typical human skeleton representation and image analysis) ---
# These names help map to specific body joints for clarity.
POINTS = [
    "HEAD",
    "L_SHOULDER", "R_SHOULDER",
    "UPPER_SPINE",  # Mid-thoracic spine, roughly level with armpits
    "L_ELBOW", "R_ELBOW",
    "L_WRIST", "R_WRIST",
    "LOWER_SPINE",  # Lumbar spine/pelvis center
    "L_HIP", "R_HIP",
    "L_KNEE", "R_KNEE",
    "L_ANKLE", "R_ANKLE"
]
NUM_POINTS = len(POINTS)  # Ensure it's exactly 15

# --- Relative Coordinates for Key Poses ---
# Coordinates are (x, y) tuples. Y values are positive upwards from assumed ground (0.0).
# X values are positive to the right, negative to the left, 0.0 being the body's midline.
# These units are arbitrary and will be scaled to screen pixels.

# Initial Standing Pose: Upright, arms slightly out, feet shoulder-width apart.
initial_pose_relative = {
    "HEAD": (0.0, 1.80),
    "L_SHOULDER": (-0.18, 1.55),
    "R_SHOULDER": (0.18, 1.55),
    "UPPER_SPINE": (0.0, 1.45),
    "L_ELBOW": (-0.25, 1.0),
    "R_ELBOW": (0.25, 1.0),
    "L_WRIST": (-0.20, 0.5),
    "R_WRIST": (0.20, 0.5),
    "LOWER_SPINE": (0.0, 0.90),
    "L_HIP": (-0.08, 0.90),
    "R_HIP": (0.08, 0.90),
    "L_KNEE": (-0.08, 0.45),
    "R_KNEE": (0.08, 0.45),
    "L_ANKLE": (-0.08, 0.0),
    "R_ANKLE": (0.08, 0.0),
}

# Final Sitting Pose: Body lowered, hips back, knees bent and forward, torso slightly leaned.
# This pose is designed to be biomechanically plausible for sitting with "heavy weight",
# implying a controlled, stable final position.
final_pose_relative = {
    "HEAD": (0.02, 1.15),  # Slight forward lean for balance
    "L_SHOULDER": (-0.16, 0.85),  # Shoulders lower, arms slightly more inward
    "R_SHOULDER": (0.16, 0.85),
    "UPPER_SPINE": (0.02, 0.80),  # Torso lowers and slightly leans
    "L_ELBOW": (-0.18, 0.60),  # Arms resting, elbows forward
    "R_ELBOW": (0.18, 0.60),
    "L_WRIST": (-0.10, 0.45),  # Wrists closer to body, as if resting on thighs
    "R_WRIST": (0.10, 0.45),
    "LOWER_SPINE": (0.0, 0.50),  # Hips/pelvis significantly lowered to sitting height
    "L_HIP": (-0.08, 0.50),  # Hips are now at the lowest point of the sit
    "R_HIP": (0.08, 0.50),
    "L_KNEE": (-0.18, 0.75),  # Knees significantly bent, forward, and slightly wider than hips
    "R_KNEE": (0.18, 0.75),
    "L_ANKLE": (-0.08, 0.0),  # Feet flat on ground, slightly forward to support bent knees
    "R_ANKLE": (0.08, 0.0),
}

# Convert pose dictionaries to NumPy arrays for efficient interpolation.
# The order is crucial and must match the `POINTS` list.
start_coords = np.array([initial_pose_relative[p] for p in POINTS])
end_coords = np.array([final_pose_relative[p] for p in POINTS])

# --- Animation Parameters ---
ANIMATION_DURATION_SECONDS = 2.5  # Time for one full sit-down or stand-up motion.
TOTAL_FRAMES = int(ANIMATION_DURATION_SECONDS * FPS)
CURRENT_FRAME = 0
# Controls the animation flow: 1 for sitting down, -1 for standing up.
# The animation will cycle by sitting down then standing up repeatedly, which ensures smoothness
# and a continuous natural loop for a biological motion stimulus.
animation_direction = 1

# --- Coordinate Transformation Parameters ---
# Calculate the person's height in relative units from initial pose.
PERSON_HEIGHT_UNITS = initial_pose_relative["HEAD"][1] - initial_pose_relative["L_ANKLE"][1]
# Target the person to occupy a certain percentage of the screen height.
TARGET_PERSON_HEIGHT_PIXELS = SCREEN_HEIGHT * 0.7
SCALE = TARGET_PERSON_HEIGHT_PIXELS / PERSON_HEIGHT_UNITS

# Offset to center the person horizontally and place feet near the bottom of the screen.
OFFSET_X = SCREEN_WIDTH // 2
OFFSET_Y = SCREEN_HEIGHT - 50


def transform_coords_to_pixels(relative_coords, scale, offset_x, offset_y):
    """
    Transforms relative (x, y) coordinates to screen (pixel_x, pixel_y) coordinates.
    Pygame's Y-axis is inverted (0 at top), so we subtract from offset_y to make y increase upwards.
    """
    pixel_coords = []
    for x_rel, y_rel in relative_coords:
        pixel_x = int(offset_x + x_rel * scale)
        pixel_y = int(offset_y - y_rel * scale)
        pixel_coords.append((pixel_x, pixel_y))
    return np.array(pixel_coords)


# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Clear screen with black background

    # Calculate raw animation progress (0.0 to 1.0)
    progress_raw = CURRENT_FRAME / TOTAL_FRAMES

    # Apply an ease-in-out (smootherstep) easing function to the progress.
    # This makes the motion start and end slowly, accelerating in the middle,
    # which is characteristic of natural human movement and contributes to
    # the "realistic, coherent, and biomechanically plausible" requirement,
    # especially for "heavy weight" where movements might be more controlled and deliberate.
    progress_eased = 0.5 - 0.5 * math.cos(math.pi * min(1.0, max(0.0, progress_raw)))

    # Interpolate current joint positions based on the animation direction.
    # If animation_direction is 1, it's sitting down (interpolating from start_coords to end_coords).
    # If animation_direction is -1, it's standing up (interpolating from end_coords to start_coords).
    if animation_direction == 1:  # Sitting down
        current_relative_coords = start_coords * \
            (1 - progress_eased)[:, np.newaxis] + end_coords * progress_eased[:, np.newaxis]
    else:  # Standing up
        current_relative_coords = end_coords * \
            (1 - progress_eased)[:, np.newaxis] + start_coords * progress_eased[:, np.newaxis]

    # Transform relative coordinates to screen pixel coordinates
    current_pixel_coords = transform_coords_to_pixels(current_relative_coords, SCALE, OFFSET_X, OFFSET_Y)

    # Draw each point light as a white circle
    for (px, py) in current_pixel_coords:
        pygame.draw.circle(screen, WHITE, (px, py), POINT_RADIUS)

    pygame.display.flip()  # Update the full display Surface to the screen

    # Advance frame counter and manage animation loop
    CURRENT_FRAME += 1
    if CURRENT_FRAME > TOTAL_FRAMES:
        CURRENT_FRAME = 0  # Reset frame counter
        animation_direction *= -1  # Reverse direction for next cycle (sit down <-> stand up)

    clock.tick(FPS)  # Control the frame rate

pygame.quit()
