
import pygame
import numpy as np
import sys

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5
FPS = 60
# Duration in seconds for one full 360-degree turn
ANIMATION_DURATION_S = 7

# --- 3D Projection Configuration ---
# Field of View: Affects the intensity of the perspective effect.
FOV = 400
# Viewer Distance: Simulates the camera's distance from the subject.
VIEWER_DISTANCE = 300


def project(point_3d):
    """
    Projects a 3D point (x, y, z) to a 2D screen coordinate (sx, sy).
    Uses a simple perspective projection formula.
    """
    # Perspective scaling factor, depends on the z-coordinate
    factor = FOV / (VIEWER_DISTANCE + point_3d[2])
    # Project x and y coordinates
    sx = point_3d[0] * factor + SCREEN_WIDTH / 2
    # Pygame's y-axis is inverted, so we negate the y-coordinate.
    # An offset is added to vertically center the animation.
    sy = -point_3d[1] * factor + SCREEN_HEIGHT * 0.8
    return int(sx), int(sy)

# --- Skeleton Definition ---
# A 15-point model representing the human body.
# Coordinates are in a 3D space where Y is up.
# The base pose is designed to look like a person standing sadly (slumped).
BASE_POSE_3D = {
    # Joint Name: np.array([x, y, z])
    # Central column
    'head':       np.array([0.0, 165.0, 5.0]),   # Head tilted slightly forward
    'neck':       np.array([0.0, 150.0, 4.0]),   # Neck forward
    'torso':      np.array([0.0, 120.0, 2.0]),   # Torso center
    # Shoulders and Arms (slumped forward)
    'l_shoulder': np.array([20.0, 145.0, 3.0]),
    'r_shoulder': np.array([-20.0, 145.0, 3.0]),
    'l_elbow':    np.array([22.0, 115.0, 5.0]),
    'r_elbow':    np.array([-22.0, 115.0, 5.0]),
    'l_wrist':    np.array([24.0, 90.0, 6.0]),
    'r_wrist':    np.array([-24.0, 90.0, 6.0]),
    # Hips and Legs
    'l_hip':      np.array([10.0, 90.0, 0.0]),
    'r_hip':      np.array([-10.0, 90.0, 0.0]),
    'l_knee':     np.array([12.0, 50.0, 1.0]),
    'r_knee':     np.array([-12.0, 50.0, 1.0]),
    'l_ankle':    np.array([10.0, 5.0, -2.0]),
    'r_ankle':    np.array([-10.0, 5.0, -2.0]),
}


def get_animated_skeleton(t, base_pose):
    """
    Calculates the 3D coordinates of the skeleton at a given time t.
    t is the animation progress from 0.0 to 1.0.
    The animation is a 360-degree turn with a natural stepping motion.
    """
    animated_pose = {}

    # 1. Calculate overall body rotation around the vertical Y-axis
    turn_angle = t * 2 * np.pi
    c, s = np.cos(turn_angle), np.sin(turn_angle)
    # Rotation matrix for rotating around the Y-axis
    R_y = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

    # 2. Define a central pivot point for the turn on the ground
    pivot_point = np.array([0.0, 0.0, 0.0])

    # 3. Apply the main rotation to all points of the base pose
    for key, p in base_pose.items():
        # Rotate the point around the pivot
        animated_pose[key] = R_y @ (p - pivot_point) + pivot_point

    # 4. Add secondary motion for stepping to make the turn realistic
    # The turn is divided into two 180-degree phases with alternating steps.
    step_height = 25.0
    knee_bend_height = 15.0

    if t < 0.5:
        # Phase 1 (0 to 180 deg): The right foot takes a step.
        phase_t = t * 2.0  # Normalize time for this phase (0 to 1)
        # Lift the right foot off the ground in a sinusoidal arc
        vertical_lift = step_height * np.sin(phase_t * np.pi)
        animated_pose['r_ankle'][1] += vertical_lift
        # Bend the right knee as the foot lifts
        animated_pose['r_knee'][1] += knee_bend_height * np.sin(phase_t * np.pi)
    else:
        # Phase 2 (180 to 360 deg): The left foot takes a step.
        phase_t = (t - 0.5) * 2.0  # Normalize time for this phase (0 to 1)
        # Lift the left foot off the ground in a sinusoidal arc
        vertical_lift = step_height * np.sin(phase_t * np.pi)
        animated_pose['l_ankle'][1] += vertical_lift
        # Bend the left knee as the foot lifts
        animated_pose['l_knee'][1] += knee_bend_height * np.sin(phase_t * np.pi)

    return animated_pose


def main():
    """
    Main function to initialize Pygame, run the animation loop, and handle events.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Biological Motion: Sad Man Turning Around")
    clock = pygame.time.Clock()

    start_time = pygame.time.get_ticks()
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # --- Animation Timing ---
        # Calculate animation progress 't' from 0.0 to 1.0, which loops indefinitely
        elapsed_time_ms = pygame.time.get_ticks() - start_time
        t = (elapsed_time_ms / (ANIMATION_DURATION_S * 1000.0)) % 1.0

        # --- Update State ---
        # Get the current 3D coordinates for all 15 points
        current_pose_3d = get_animated_skeleton(t, BASE_POSE_3D)

        # --- Drawing ---
        screen.fill(BLACK)

        # Sort points by z-depth to handle occlusion correctly,
        # drawing farther points first.
        sorted_points = sorted(
            current_pose_3d.values(), key=lambda p: p[2], reverse=True
        )

        for point_3d in sorted_points:
            # Project the 3D point to 2D screen coordinates
            sx, sy = project(point_3d)
            # Draw the point as a white circle
            pygame.draw.circle(screen, WHITE, (sx, sy), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
