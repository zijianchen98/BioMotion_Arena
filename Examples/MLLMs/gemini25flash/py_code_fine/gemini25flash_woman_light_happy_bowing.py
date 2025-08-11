
import pygame
import math

# Pygame Initialization
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800  # Portrait orientation like the example image
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing Woman")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point properties
POINT_RADIUS = 5

# Animation parameters
FPS = 30
ANIMATION_DURATION_SECONDS = 3  # Total duration for one bow down and one straighten up cycle
TOTAL_FRAMES = FPS * ANIMATION_DURATION_SECONDS
# Half for bowing down, half for straightening up
FRAMES_PER_PHASE = TOTAL_FRAMES // 2

# Clock for controlling frame rate
clock = pygame.time.Clock()

# --- Point Definitions ---
# 15 points representing a human figure (approximate standard setup)
# These points correspond to common joint locations for biological motion:
# 0: Head, 1: Neck, 2: L_Shoulder, 3: R_Shoulder, 4: L_Elbow, 5: R_Elbow,
# 6: Torso_Center (roughly mid-chest/upper abdomen), 7: L_Wrist, 8: R_Wrist,
# 9: L_Hip, 10: R_Hip, 11: L_Knee, 12: R_Knee, 13: L_Ankle, 14: R_Ankle

# Base scaling for the figure on screen
FIGURE_HEIGHT_PIXELS = 300  # Desired height from ankle to head in the initial pose
FIGURE_CENTER_X = SCREEN_WIDTH // 2
FIGURE_BOTTOM_Y = SCREEN_HEIGHT - 100  # Y coordinate for the figure's base (ankles)

# Initial Standing Pose (defined using relative proportions, then scaled and translated)
# (x, y) coordinates are relative to the figure's base (mid-ankles), with Y-axis pointing upwards
# These proportions are chosen to broadly resemble a human figure in the provided example image.
initial_relative_points = [
    (0.0, 0.95),  # 0: Head (top of the figure)
    (0.0, 0.80),  # 1: Neck
    (-0.15, 0.75), # 2: L_Shoulder
    (0.15, 0.75),  # 3: R_Shoulder
    (-0.20, 0.50), # 4: L_Elbow (slightly bent in standing pose)
    (0.20, 0.50),  # 5: R_Elbow
    (0.0, 0.45),   # 6: Torso_Center
    (-0.25, 0.25), # 7: L_Wrist
    (0.25, 0.25),  # 8: R_Wrist
    (-0.12, 0.35), # 9: L_Hip
    (0.12, 0.35),  # 10: R_Hip
    (-0.12, 0.15), # 11: L_Knee
    (0.12, 0.15),  # 12: R_Knee
    (-0.12, 0.00), # 13: L_Ankle (base of the figure)
    (0.12, 0.00)   # 14: R_Ankle
]

# Convert relative coordinates to absolute screen coordinates for the initial pose
P_initial_static = []
for x_rel, y_rel in initial_relative_points:
    # Scale X coordinates by adjusting for potential screen width differences
    # The (SCREEN_WIDTH / 600) factor is a fine-tuning for aspect ratio consistency
    screen_x = FIGURE_CENTER_X + x_rel * FIGURE_HEIGHT_PIXELS * (SCREEN_WIDTH / 600)
    # Invert Y-axis for Pygame (Y increases downwards) and position relative to FIGURE_BOTTOM_Y
    screen_y = FIGURE_BOTTOM_Y - y_rel * FIGURE_HEIGHT_PIXELS
    P_initial_static.append((screen_x, screen_y))

# Utility function to rotate a point around an arbitrary origin
def rotate_point(point, origin, angle_rad):
    ox, oy = origin
    px, py = point
    # Apply rotation formula: (x', y') = (ox + cos(a)*(px-ox) - sin(a)*(py-oy), oy + sin(a)*(px-ox) + cos(a)*(py-oy))
    qx = ox + math.cos(angle_rad) * (px - ox) - math.sin(angle_rad) * (py - oy)
    qy = oy + math.sin(angle_rad) * (px - ox) + math.cos(angle_rad) * (py - oy)
    return qx, qy

# Function to calculate the pose for a given animation progress
# This function applies hierarchical rotations to simulate a natural bowing motion.
def calculate_current_pose(bow_progress, initial_pose):
    # bow_progress: 0.0 (standing) to 1.0 (full bow)

    # Start with a deep copy of the initial pose to avoid modifying the original
    current_pose_points = [list(p) for p in initial_pose]

    # 1. Global shift of the entire figure for balance
    # As the person bows, they might subtly shift their weight forward and
    # slightly lower their center of gravity (e.g., a slight knee bend).
    global_shift_x = bow_progress * 25  # Shift figure forward (right on screen)
    global_shift_y = bow_progress * 10   # Shift figure slightly down
    for i in range(15):
        current_pose_points[i] = (current_pose_points[i][0] + global_shift_x, current_pose_points[i][1] + global_shift_y)

    # Now, perform rotations based on these globally shifted initial positions
    # The primary pivot for the bowing motion is around the hips.
    hip_pivot_x = (current_pose_points[9][0] + current_pose_points[10][0]) / 2
    hip_pivot_y = (current_pose_points[9][1] + current_pose_points[10][1]) / 2

    # 2. Torso (main body) rotation around the hip pivot
    # This is the most significant part of the bowing action.
    main_bow_angle = bow_progress * math.radians(75)  # Max 75 degrees forward tilt
    # Points affected by this rotation include the entire upper body and arms
    # Indices: Head(0), Neck(1), L/R Shoulder(2,3), L/R Elbow(4,5), Torso_Center(6), L/R Wrist(7,8)
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        current_pose_points[i] = rotate_point(current_pose_points[i], (hip_pivot_x, hip_pivot_y), main_bow_angle)

    # 3. Head tuck: Head (0) rotates additionally around Neck (1)
    # This makes the head look down more naturally as the person bows deeply.
    head_tuck_angle = bow_progress * math.radians(20)  # Additional 20 degrees tuck
    # The Neck point (1) has already been rotated with the torso, so use its current position as pivot.
    current_pose_points[0] = rotate_point(current_pose_points[0], current_pose_points[1], head_tuck_angle)

    # 4. Arm adjustments: Elbows and Wrists rotate around their respective shoulders/elbows
    # This simulates arms hanging more naturally due to gravity, swinging slightly forward.
    arm_swing_angle = bow_progress * math.radians(20)  # How much arms swing forward relative to torso's main rotation

    # Left Arm: L_Elbow(4) rotates around L_Shoulder(2), L_Wrist(7) rotates around L_Elbow(4)
    # The shoulder point (2) is already in its rotated position from the torso rotation.
    l_shoulder_pos = current_pose_points[2]
    current_pose_points[4] = rotate_point(current_pose_points[4], l_shoulder_pos, arm_swing_angle)
    # The elbow point (4) is now in its adjusted position.
    current_pose_points[7] = rotate_point(current_pose_points[7], current_pose_points[4], arm_swing_angle)

    # Right Arm: R_Elbow(5) rotates around R_Shoulder(3), R_Wrist(8) rotates around R_Elbow(5)
    # Note: angles for the right arm's independent swing are negative to ensure symmetrical movement.
    r_shoulder_pos = current_pose_points[3]
    current_pose_points[5] = rotate_point(current_pose_points[5], r_shoulder_pos, -arm_swing_angle)
    current_pose_points[8] = rotate_point(current_pose_points[8], current_pose_points[5], -arm_swing_angle)

    return current_pose_points

# Main animation loop
running = True
frame_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate animation progress (0.0 to 1.0 for bowing down, then back up)
    # We use a cosine interpolation (ease-in/ease-out) for smooth, natural motion.
    # phase_progress: 0.0 to 1.0 within a single bowing (down or up) phase.
    phase_progress = (frame_count % FRAMES_PER_PHASE) / (FRAMES_PER_PHASE - 1)
    eased_progress = 0.5 - 0.5 * math.cos(math.pi * phase_progress)

    # Determine if we are in the bowing down phase or straightening up phase
    if (frame_count // FRAMES_PER_PHASE) % 2 == 0:  # First half: Bowing down
        bow_progress = eased_progress
    else:  # Second half: Straightening up
        bow_progress = 1.0 - eased_progress

    # Get the current point positions for the animation frame
    current_points = calculate_current_pose(bow_progress, P_initial_static)

    # Drawing
    screen.fill(BLACK)  # Solid black background as required

    # Draw each point as a white circle
    for x, y in current_points:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

    pygame.display.flip()  # Update the full display surface

    # Advance frame count and loop animation if a full cycle is complete
    frame_count += 1
    if frame_count >= TOTAL_FRAMES:
        frame_count = 0  # Reset to loop the animation continuously

    clock.tick(FPS)  # Control frame rate to ensure smooth animation

pygame.quit()
