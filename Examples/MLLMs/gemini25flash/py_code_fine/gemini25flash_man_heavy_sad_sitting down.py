
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Animation parameters
FPS = 30  # Frames per second
DURATION_SECONDS = 4  # Total duration of the animation for a "heavy" feeling
TOTAL_FRAMES = DURATION_SECONDS * FPS

# Define joint points. There are exactly 15 points.
# Mapping based on common point-light display structure and the example image:
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Chest (Upper Spine/Torso)
# 6: Left Wrist
# 7: Right Wrist
# 8: Pelvis (Lower Spine/Torso, the main reference point)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

# Define the "ground" level for the animation
GROUND_Y = SCREEN_HEIGHT - 50

# --- Standing Pose (Initial) ---
# Relative coordinates with Pelvis (point 8) at (0,0) for easier calculation.
# Y-values are negative for points above the pelvis, positive for points below.
# X-values are negative for left side, positive for right side.
standing_points_rel = {
    0: (0, -180),  # Head
    1: (-30, -130), # Left Shoulder
    2: (30, -130),  # Right Shoulder
    3: (-40, -80),  # Left Elbow
    4: (40, -80),   # Right Elbow
    5: (0, -110),   # Chest (Upper Torso)
    6: (-30, -30),  # Left Wrist
    7: (30, -30),   # Right Wrist
    8: (0, 0),      # Pelvis (Reference point)
    9: (-20, 0),    # Left Hip
    10: (20, 0),    # Right Hip
    11: (-20, 90),  # Left Knee
    12: (20, 90),   # Right Knee
    13: (-20, 180), # Left Ankle
    14: (20, 180)   # Right Ankle
}

# Calculate the absolute Y position of the pelvis in the standing pose
# such that ankles (point 13 and 14) are on the ground.
STANDING_PELVIS_ABS_Y = GROUND_Y - standing_points_rel[13][1]

# Construct the initial absolute pose
initial_pose = []
for i in range(15):
    x_rel, y_rel = standing_points_rel[i]
    x_abs = SCREEN_WIDTH // 2 + x_rel
    y_abs = STANDING_PELVIS_ABS_Y + y_rel
    initial_pose.append((x_abs, y_abs))

# --- Sitting Pose (Final) ---
# Relative coordinates for the sitting pose.
# Torso slightly leans forward, knees are bent, arms resting on lap.
sitting_points_rel = {
    0: (10, -90),   # Head (Lower, slightly forward)
    1: (-25, -60),  # Left Shoulder (Lower, slightly forward)
    2: (35, -60),   # Right Shoulder (Lower, slightly forward)
    3: (-20, -20),  # Left Elbow (Bent, closer to body)
    4: (20, -20),   # Right Elbow (Bent, closer to body)
    5: (5, -50),    # Chest (Lower, slightly forward)
    6: (-20, 10),   # Left Wrist (Resting on lap, below pelvis Y)
    7: (20, 10),    # Right Wrist (Resting on lap, below pelvis Y)
    8: (0, 0),      # Pelvis (Still reference (0,0) in relative terms)
    9: (-20, 0),    # Left Hip
    10: (20, 0),    # Right Hip
    11: (40, 50),   # Left Knee (Bent, moved forward (positive x) and up (less positive y))
    12: (40, 50),   # Right Knee
    13: (30, 90),   # Left Ankle (Foot flat on ground, slightly forward)
    14: (30, 90)    # Right Ankle
}

# Calculate the absolute Y position of the pelvis in the sitting pose
# such that ankles (point 13 and 14) are on the ground.
SITTING_PELVIS_ABS_Y = GROUND_Y - sitting_points_rel[13][1]

# Construct the final absolute pose
final_pose = []
for i in range(15):
    x_rel, y_rel = sitting_points_rel[i]
    x_abs = SCREEN_WIDTH // 2 + x_rel
    y_abs = SITTING_PELVIS_ABS_Y + y_rel
    final_pose.append((x_abs, y_abs))

# Animation loop
current_frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK) # Clear screen to black background

    if current_frame <= TOTAL_FRAMES:
        # Calculate animation progress (0 to 1)
        t = current_frame / TOTAL_FRAMES
        
        # Using linear interpolation for a "heavy" and controlled movement
        # (No easing function applied for this effect)
        t_interp = t 

        # Interpolate between initial and final poses for each point
        current_pose = []
        for i in range(15):
            start_x, start_y = initial_pose[i]
            end_x, end_y = final_pose[i]

            interp_x = start_x + (end_x - start_x) * t_interp
            interp_y = start_y + (end_y - start_y) * t_interp
            current_pose.append((interp_x, interp_y))

        # Draw current pose
        for x, y in current_pose:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

        current_frame += 1
    else:
        # After animation ends, keep showing the final pose indefinitely
        for x, y in final_pose:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)
        
        # Optional: uncomment to loop the animation
        # current_frame = 0

    pygame.display.flip() # Update the full display surface to the screen
    clock.tick(FPS)       # Control frame rate

pygame.quit()
