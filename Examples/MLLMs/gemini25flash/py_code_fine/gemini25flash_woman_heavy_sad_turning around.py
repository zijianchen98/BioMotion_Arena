
import pygame
import math

# --- Pygame Initialization ---
pygame.init()

# --- Screen Dimensions and Colors ---
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Turning Around")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Point Properties ---
POINT_RADIUS = 5  # Size of the white dots

# --- Animation Parameters ---
FPS = 30  # Frames per second
DURATION_SECONDS = 6  # How long the 360-degree turn takes (slower for 'heavy weight')
TOTAL_FRAMES = FPS * DURATION_SECONDS
TURN_ANGLE = 2 * math.pi  # Full 360-degree turn in radians

# --- Human Model Definition (15 Points) ---
# Joint names for clarity and indexing
JOINT_NAMES = [
    "head", "neck", "r_shoulder", "l_shoulder", "r_elbow", "l_elbow",
    "r_wrist", "l_wrist", "torso_mid", "r_hip", "l_hip", "r_knee",
    "l_knee", "r_ankle", "l_ankle"
]

# Base 3D coordinates (x, y, z) for a "sad woman with heavy weight" standing pose.
# Origin (0,0,0) is approximately at the pelvis/hip level.
# Y is the vertical axis (positive is up).
# X is the horizontal axis (positive is right).
# Z is the depth axis (positive is forward, negative is backward).
# Values are in abstract units; they will be scaled to pixels later.
# Posture adjustments for "sad" (slight slump, head down) and "heavy weight" (wider stance, arms closer).
BASE_POSE_3D = {
    "head":        (0.0,  0.80, 0.0),  # Head slightly lowered
    "neck":        (0.0,  0.70, 0.0),
    "r_shoulder":  (0.20, 0.65, -0.05), # Shoulders slightly hunched forward
    "l_shoulder":  (-0.20, 0.65, -0.05),
    "r_elbow":     (0.25, 0.35, -0.10), # Arms slightly bent and closer to body
    "l_elbow":     (-0.25, 0.35, -0.10),
    "r_wrist":     (0.28, 0.10, -0.10), # Hands slightly forward, not swinging out
    "l_wrist":     (-0.28, 0.10, -0.10),
    "torso_mid":   (0.0,  0.45, -0.02), # Upper torso slightly hunched
    "r_hip":       (0.15, 0.0, 0.0),   # Wider hip stance for 'heavy'
    "l_hip":       (-0.15, 0.0, 0.0),
    "r_knee":      (0.18, -0.40, 0.0), # Knees slightly outward
    "l_knee":      (-0.18, -0.40, 0.0),
    "r_ankle":     (0.18, -0.80, 0.0), # Ankles slightly outward, reflecting wider stance
    "l_ankle":     (-0.18, -0.80, 0.0)
}

# Verify that we have exactly 15 points as required
assert len(BASE_POSE_3D) == 15, "Error: The human model must consist of exactly 15 points."

# --- Scaling and Translation for Screen Display ---
# Calculate the approximate height of the figure in abstract units
figure_height_units = BASE_POSE_3D["head"][1] - BASE_POSE_3D["l_ankle"][1] # Approx 0.8 - (-0.8) = 1.6 units

# Scale the figure to be about 450 pixels tall on the screen
SCALE_FACTOR = 450 / figure_height_units

# Center the figure horizontally and vertically on the screen
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2 + 100 # Shift down slightly so feet are not at the bottom edge

# --- Utility Functions ---
def rotate_y(x, y, z, angle):
    """
    Rotates a 3D point (x, y, z) around the Y-axis (vertical axis).
    The Y-coordinate remains unchanged during Y-axis rotation.
    """
    new_x = x * math.cos(angle) - z * math.sin(angle)
    new_z = x * math.sin(angle) + z * math.cos(angle)
    return new_x, y, new_z

def project_to_2d(x, y, scale, center_x, center_y):
    """
    Projects a 3D point's (x, y) coordinates to 2D screen coordinates using orthographic projection.
    Orthographic projection is typically used for point-light displays to focus on motion kinematics
    without perspective distortions (objects don't change size with depth).
    """
    screen_x = int(x * scale + center_x)
    # Pygame's Y-axis is inverted (0 at top), so we invert our 3D Y before scaling.
    screen_y = int(-y * scale + center_y)
    return screen_x, screen_y

# --- Animation Loop ---
running = True
frame_count = 0
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    SCREEN.fill(BLACK)

    # Calculate current animation progress (normalized time from 0 to 1)
    t = frame_count / TOTAL_FRAMES

    # Calculate the current rotation angle.
    # Using a cosine easing function to make the turn start and end smoothly (acceleration/deceleration),
    # which contributes to the "heavy" and "natural" feel.
    current_angle = TURN_ANGLE * (0.5 - 0.5 * math.cos(math.pi * t))

    # Add a subtle vertical sway to imply weight shift during the turn.
    # The sine function creates a gentle up-down motion, completing two cycles per full turn,
    # mimicking the shift of weight between feet.
    SWAY_AMPLITUDE = 0.015  # Max vertical sway (in abstract units)
    vertical_sway = SWAY_AMPLITUDE * math.sin(current_angle * 2) # Two up/down cycles per 360 turn

    # Calculate the 2D positions of all points for the current frame
    current_points_2d = []
    for joint_name in JOINT_NAMES:
        x, y, z = BASE_POSE_3D[joint_name]

        # Apply Y-axis rotation to the 3D point
        rotated_x, rotated_y, rotated_z = rotate_y(x, y, z, current_angle)

        # Apply the subtle vertical sway to the rotated Y coordinate
        rotated_y += vertical_sway

        # Project the 3D point (now rotated and swayed) to 2D screen coordinates
        px, py = project_to_2d(rotated_x, rotated_y, SCALE_FACTOR, CENTER_X, CENTER_Y)
        current_points_2d.append((px, py))

    # Draw all the white points on the screen
    for px, py in current_points_2d:
        pygame.draw.circle(SCREEN, WHITE, (px, py), POINT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Advance the frame count and loop the animation
    frame_count += 1
    if frame_count >= TOTAL_FRAMES:
        frame_count = 0

    # Cap the frame rate
    clock.tick(FPS)

# --- Quit Pygame ---
pygame.quit()
