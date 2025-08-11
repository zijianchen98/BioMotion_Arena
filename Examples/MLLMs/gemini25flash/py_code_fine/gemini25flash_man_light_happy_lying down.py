
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Lying Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5
NUM_POINTS = 15

# Animation parameters
ANIMATION_DURATION = 3000  # milliseconds for one full cycle (e.g., 3 seconds)
FPS = 60
clock = pygame.time.Clock()

# --- Define the 15 points and their relative configurations ---
# Mapping of 15 points (0-14), based on the provided image and common biological motion models:
# 0: Head
# 1: Left Shoulder, 2: Right Shoulder
# 3: Left Elbow, 4: Right Elbow
# 5: Left Wrist, 6: Right Wrist
# 7: Sternum (Center Chest)
# 8: Left Hip, 9: Right Hip
# 10: Left Knee, 11: Right Knee
# 12: Left Ankle, 13: Right Ankle
# 14: Pelvis (Lower torso center, serves as the kinematic root/pivot)

# Proportional scaling for the human figure relative to screen dimensions.
# These values determine the overall size of the person on screen.
FIGURE_HEIGHT_SCREEN_PROPORTION = 0.7  # Figure's height is 70% of screen height when standing
FIGURE_WIDTH_SCREEN_PROPORTION = 0.2   # Figure's width is 20% of screen width when standing

# Define relative coordinates for a 'canonical' standing figure.
# Pelvis (point 14) is at (0,0) in this relative system.
# Y-axis is positive downwards (as in Pygame), so 'up' is negative Y.
STANDING_RELATIVE_POSE = [
    # (x, y) coordinates, scaled by proportions later
    # Head (0)
    (0.0, -0.45 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Shoulders (1, 2)
    (-0.08 * FIGURE_WIDTH_SCREEN_PROPORTION, -0.35 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    (0.08 * FIGURE_WIDTH_SCREEN_PROPORTION, -0.35 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Elbows (3, 4)
    (-0.10 * FIGURE_WIDTH_SCREEN_PROPORTION, -0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    (0.10 * FIGURE_WIDTH_SCREEN_PROPORTION, -0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Wrists (5, 6)
    (-0.12 * FIGURE_WIDTH_SCREEN_PROPORTION, -0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    (0.12 * FIGURE_WIDTH_SCREEN_PROPORTION, -0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Sternum (7)
    (0.0, -0.25 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Hips (8, 9)
    (-0.06 * FIGURE_WIDTH_SCREEN_PROPORTION, 0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    (0.06 * FIGURE_WIDTH_SCREEN_PROPORTION, 0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Knees (10, 11)
    (-0.08 * FIGURE_WIDTH_SCREEN_PROPORTION, 0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    (0.08 * FIGURE_WIDTH_SCREEN_PROPORTION, 0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Ankles (12, 13)
    (-0.10 * FIGURE_WIDTH_SCREEN_PROPORTION, 0.40 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    (0.10 * FIGURE_WIDTH_SCREEN_PROPORTION, 0.40 * FIGURE_HEIGHT_SCREEN_PROPORTION),
    # Pelvis (14) - Our reference point, relative (0,0)
    (0.0, 0.0)
]

# Define relative coordinates for a 'canonical' lying figure (on back, head to the left, feet to the right).
# Pelvis (point 14) is at (0,0) in this relative system.
# X-axis now represents the length of the body, Y-axis represents the width/thickness.
LYING_RELATIVE_POSE = [
    # (x, y) coordinates, scaled by proportions
    # Head (0)
    (-0.45 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.0), # Head is to the left (negative X)
    # Shoulders (1, 2)
    (-0.35 * FIGURE_HEIGHT_SCREEN_PROPORTION, -0.08 * FIGURE_WIDTH_SCREEN_PROPORTION),
    (-0.35 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.08 * FIGURE_WIDTH_SCREEN_PROPORTION),
    # Elbows (3, 4) - arms extended alongside body
    (-0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION, -0.10 * FIGURE_WIDTH_SCREEN_PROPORTION),
    (-0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.10 * FIGURE_WIDTH_SCREEN_PROPORTION),
    # Wrists (5, 6)
    (-0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION, -0.12 * FIGURE_WIDTH_SCREEN_PROPORTION),
    (-0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.12 * FIGURE_WIDTH_SCREEN_PROPORTION),
    # Sternum (7)
    (-0.25 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.0),
    # Hips (8, 9) - legs extended
    (0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION, -0.06 * FIGURE_WIDTH_SCREEN_PROPORTION),
    (0.05 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.06 * FIGURE_WIDTH_SCREEN_PROPORTION),
    # Knees (10, 11)
    (0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION, -0.08 * FIGURE_WIDTH_SCREEN_PROPORTION),
    (0.20 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.08 * FIGURE_WIDTH_SCREEN_PROPORTION),
    # Ankles (12, 13)
    (0.40 * FIGURE_HEIGHT_SCREEN_PROPORTION, -0.10 * FIGURE_WIDTH_SCREEN_PROPORTION),
    (0.40 * FIGURE_HEIGHT_SCREEN_PROPORTION, 0.10 * FIGURE_WIDTH_SCREEN_PROPORTION),
    # Pelvis (14) - Reference point
    (0.0, 0.0)
]

# Absolute screen position for the 'pelvis' point (our root) at start and end of animation.
# This defines where the whole figure is placed on the screen.
PELVIS_START_ABS_POS = (WIDTH // 2, HEIGHT * 0.75) # Pelvis is 75% down the screen when standing
PELVIS_END_ABS_POS = (WIDTH // 2, HEIGHT * 0.75)   # Pelvis remains at approximately the same 'ground' level when lying


# Easing function for smoother animation (smooth start and end)
def ease_in_out_sine(t):
    return 0.5 - 0.5 * math.cos(t * math.pi)

# Main function to calculate all 15 point positions for a given animation progress `t`
def get_current_animation_points(t):
    current_points_abs = []

    # Apply easing to the raw time progress `t` (0.0 to 1.0)
    # This makes the animation accelerate and decelerate smoothly.
    t_eased = ease_in_out_sine(t)

    # 1. Interpolate overall Pelvis position (global translation of the figure's root)
    current_pelvis_x = PELVIS_START_ABS_POS[0] * (1 - t_eased) + PELVIS_END_ABS_POS[0] * t_eased
    current_pelvis_y = PELVIS_START_ABS_POS[1] * (1 - t_eased) + PELVIS_END_ABS_POS[1] * t_eased

    # 2. Interpolate Torso Rotation (for head, sternum, shoulders)
    # The torso rotates from 0 degrees (vertical) to 90 degrees (horizontal) relative to the screen.
    torso_angle_rad = t_eased * (math.pi / 2) # Angle from 0 to pi/2 radians

    # 3. Calculate each point's position based on interpolated state
    for i in range(NUM_POINTS):
        # Get relative position from Pelvis in STANDING pose (sx_rel, sy_rel)
        sx_rel, sy_rel = STANDING_RELATIVE_POSE[i]
        # Get relative position from Pelvis in LYING pose (lx_rel, ly_rel)
        lx_rel, ly_rel = LYING_RELATIVE_POSE[i]

        current_x_rel, current_y_rel = 0.0, 0.0

        if i == 14: # Pelvis: its relative position is always (0,0) as it's our kinematic root
            current_x_rel, current_y_rel = 0.0, 0.0
        else:
            # Apply rotation of the initial (standing) relative coordinates
            # This simulates the main body rotation around the pelvis.
            rotated_x_from_stand = sx_rel * math.cos(torso_angle_rad) - sy_rel * math.sin(torso_angle_rad)
            rotated_y_from_stand = sx_rel * math.sin(torso_angle_rad) + sy_rel * math.cos(torso_angle_rad)

            # Blend this rotated position with the final lying position.
            # This blending allows for limbs to adjust their specific orientation
            # (e.g., arms extending alongside body, legs straightening)
            # which is not fully captured by just rotating the initial pose.
            current_x_rel = rotated_x_from_stand * (1 - t_eased) + lx_rel * t_eased
            current_y_rel = rotated_y_from_stand * (1 - t_eased) + ly_rel * t_eased

            # Add specific bending/straightening effects for legs to enhance realism.
            # Legs might bend slightly during the lowering phase and then straighten.
            if i in [10, 11, 12, 13]: # Knees and Ankles
                # `bend_factor` peaks in the middle of the animation (t_eased = 0.5), then reduces.
                # This simulates bending during descent and then straightening.
                bend_factor = math.sin(t_eased * math.pi) 

                # Adjust Y coordinate to simulate bending then straightening.
                # When bending, the knee/ankle moves slightly 'up' relative to its straight position.
                # In Pygame, positive Y is down, so subtracting moves points 'up'.
                bend_offset_y = -bend_factor * 0.03 * FIGURE_HEIGHT_SCREEN_PROPORTION # Small vertical adjustment

                current_y_rel += bend_offset_y
                
                # Optional: Slight horizontal adjustment for leg spread during bend/straighten
                # side_multiplier = -1 if i % 2 == 0 else 1 # Left points (even index) vs Right points (odd index)
                # current_x_rel += side_multiplier * bend_factor * 0.01 * FIGURE_WIDTH_SCREEN_PROPORTION

        # Add the calculated relative position to the absolute pelvis position
        # to get the final absolute screen coordinates for each point.
        current_abs_x = current_pelvis_x + current_x_rel
        current_abs_y = current_pelvis_y + current_y_rel

        current_points_abs.append((int(current_abs_x), int(current_abs_y)))
        
    return current_points_abs


# Game loop
running = True
animation_start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate animation progress `t` (from 0.0 to 1.0).
    # Uses modulo operator to loop the animation continuously.
    elapsed_time = pygame.time.get_ticks() - animation_start_time
    t = (elapsed_time / ANIMATION_DURATION) % 1.0

    # Get current positions of all 15 points
    current_points = get_current_animation_points(t)

    # Drawing
    SCREEN.fill(BLACK) # Solid black background

    # Draw each point as a white circle
    for point_pos in current_points:
        pygame.draw.circle(SCREEN, WHITE, point_pos, POINT_RADIUS)

    pygame.display.flip() # Update the full display

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
