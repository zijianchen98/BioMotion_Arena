
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# --- Screen and Display Settings ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Waving Hand")
clock = pygame.time.Clock()

# --- Visual and Animation Constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 6
FPS = 60

# --- Skeleton Definition ---
# A 15-point model is used to represent the human figure.
# The coordinates are defined in a local 3D space:
# - X-axis: horizontal (positive is right)
# - Y-axis: vertical (positive is down, to match Pygame's screen coordinates)
# - Z-axis: depth (positive is away from the viewer)
# The origin (0,0,0) is conceptually at the figure's center on the ground plane.
BASE_POSE = np.array([
    # 0: Head
    [0., -160., 0.],
    # 1: Sternum (upper torso)
    [0., -100., 0.],
    # 2: Pelvis (lower torso/hips center)
    [0., -20., 0.],

    # Left Arm (from the figure's perspective, viewer's right)
    # 3: L Shoulder
    [-40., -100., 0.],
    # 4: L Elbow
    [-40., -30., 0.],
    # 5: L Wrist
    [-40., 40., 0.],

    # Right Arm (the waving arm, viewer's left)
    # 6: R Shoulder
    [40., -100., 0.],
    # 7: R Elbow
    [40., -30., 0.],
    # 8: R Wrist
    [40., 40., 0.],

    # Left Leg
    # 9: L Hip
    [-30., -20., 0.],
    # 10: L Knee
    [-30., 50., 0.],
    # 11: L Ankle
    [-30., 120., 0.],

    # Right Leg
    # 12: R Hip
    [30., -20., 0.],
    # 13: R Knee
    [30., 50., 0.],
    # 14: R Ankle
    [30., 120., 0.]
], dtype=float)

# --- Kinematic Information ---
# Indices for joints of interest
R_SHOULDER, R_ELBOW, R_WRIST = 6, 7, 8
L_SHOULDER, L_ELBOW, L_WRIST = 3, 4, 5

# Limb lengths are pre-calculated for the inverse kinematics solver.
UPPER_ARM_LEN = np.linalg.norm(BASE_POSE[R_ELBOW] - BASE_POSE[R_SHOULDER])
FOREARM_LEN = np.linalg.norm(BASE_POSE[R_WRIST] - BASE_POSE[R_ELBOW])

def solve_ik_2d(p1, p3, l1, l2):
    """
    Solves the 2D inverse kinematics for a 2-link chain (e.g., an arm).
    Given the positions of the shoulder (p1) and wrist (p3), and the lengths
    of the upper arm (l1) and forearm (l2), it calculates the position of the
    elbow (p2).
    """
    p1 = np.asarray(p1)
    p3 = np.asarray(p3)
    d = np.linalg.norm(p3 - p1)

    # Handle cases where the target is out of reach
    if d > l1 + l2:
        p2 = p1 + l1 * (p3 - p1) / d
        return p2
    if d < abs(l1 - l2):
        p2 = p1 - l1 * (p3 - p1) / d
        return p2

    # Use the law of cosines to find the elbow position
    a = (l1**2 - l2**2 + d**2) / (2 * d)
    h = np.sqrt(max(0, l1**2 - a**2))

    p2_mid = p1 + a * (p3 - p1) / d
    
    # Calculate the final elbow position, choosing the "outward" bend
    p2_x = p2_mid[0] - h * (p3[1] - p1[1]) / d
    p2_y = p2_mid[1] + h * (p3[0] - p1[0]) / d

    return np.array([p2_x, p2_y])

def animate_points(t):
    """
    Calculates the 3D positions of all 15 points for a given time t.
    This function procedurally generates the motion.
    """
    points = BASE_POSE.copy()

    # Animation parameters are tuned for a "happy" and natural waving motion
    wave_speed = 4.0
    wave_horiz_amp = 65
    wave_vert_amp = 10
    bob_speed = 2.0  # Synced to be half the wave speed for a natural bounce
    bob_amp = 4
    sway_speed = 2.0
    sway_amp = 3

    # 1. Add overall body motion (bob and sway) for realism and energy
    y_offset = bob_amp * np.sin(t * bob_speed)
    x_offset = sway_amp * np.cos(t * sway_speed)
    points[:, 1] += y_offset
    points[:, 0] += x_offset

    # 2. Animate the primary action: the waving right arm
    r_shoulder_pos = points[R_SHOULDER]
    
    # The wrist follows a parametric elliptical path to create the wave
    wrist_center_x = 90 + x_offset
    wrist_center_y = -90 + y_offset
    r_wrist_x = wrist_center_x + wave_horiz_amp * np.cos(t * wave_speed)
    r_wrist_y = wrist_center_y + wave_vert_amp * np.sin(t * wave_speed * 2)
    r_wrist_pos_2d = np.array([r_wrist_x, r_wrist_y])
    
    # Use the IK solver to find the corresponding natural elbow position
    r_shoulder_pos_2d = r_shoulder_pos[:2]
    r_elbow_pos_2d = solve_ik_2d(r_shoulder_pos_2d, r_wrist_pos_2d, UPPER_ARM_LEN, FOREARM_LEN)
    
    points[R_WRIST, :2] = r_wrist_pos_2d
    points[R_ELBOW, :2] = r_elbow_pos_2d
    
    # Add Z-depth variation to the waving arm for a subtle 3D effect
    z_wave = 25 * np.sin(t * wave_speed)
    points[R_WRIST, 2] = z_wave
    points[R_ELBOW, 2] = z_wave * 0.5

    # 3. Add subtle secondary motion to the non-waving arm for balance
    l_arm_sway_amp_x = 8
    l_wrist_sway_x = l_arm_sway_amp_x * np.sin(t * sway_speed + np.pi)
    points[L_WRIST, 0] += l_wrist_sway_x
    points[L_ELBOW, 0] += l_wrist_sway_x * 0.5

    return points

def project_and_draw(points_3d):
    """
    Projects the 3D points to 2D screen space and draws them.
    """
    viewer_distance = 500
    # Center the figure on the screen, with a slight vertical offset
    center_x, center_y = WIDTH / 2, HEIGHT / 2 + 50

    screen.fill(BLACK)
    
    # A simple perspective projection formula is used
    for p in points_3d:
        x, y, z = p
        # Avoid division by zero if a point is at the camera's Z position
        scale = viewer_distance / (viewer_distance - z if viewer_distance > z else 0.1)
        
        px = int(x * scale + center_x)
        py = int(y * scale + center_y)
        
        pygame.draw.circle(screen, WHITE, (px, py), POINT_RADIUS)

# --- Main Application Loop ---
running = True
start_time = pygame.time.get_ticks()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the elapsed time for the animation function
    current_time = (pygame.time.get_ticks() - start_time) / 1000.0
    
    # Update the positions of all points
    animated_3d_points = animate_points(current_time)
    
    # Project the 3D points to 2D and draw them on the screen
    project_and_draw(animated_3d_points)
    
    # Refresh the display
    pygame.display.flip()
    
    # Maintain a consistent frame rate
    clock.tick(FPS)
    
pygame.quit()
