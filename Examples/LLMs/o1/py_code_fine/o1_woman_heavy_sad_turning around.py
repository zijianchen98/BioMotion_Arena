import pygame
import math
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sad Woman with Heavy Weight Turning Around")

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 30

# Center point for drawing
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Number of points
NUM_POINTS = 15

# Define a base skeleton in 3D (x, y, z) for a sad posture with heavy weight in right hand
# The figure is somewhat slumped, right hand lowered holding object
# These coordinates assume y is "up" and z is depth. Base orientation is in the x=0 plane.
# We'll rotate around the y-axis to simulate turning.
base_skeleton_3d = [
    (0, 35, 0),   # 0: head
    (-6, 28, 0),  # 1: left shoulder
    (6, 28, 0),   # 2: right shoulder
    (-8, 18, 0),  # 3: left elbow
    (8, 18, 0),   # 4: right elbow
    (-6,  8, 0),  # 5: left wrist
    (10,  7, 0),  # 6: right wrist
    (-4, 10, 0),  # 7: left hip
    (4,  10, 0),  # 8: right hip
    (-4,  0, 0),  # 9: left knee
    (4,   0, 0),  # 10: right knee
    (-4, -10, 0), # 11: left ankle
    (4,  -10, 0), # 12: right ankle
    (0,  23, 0),  # 13: chest center
    (12,  6, 0)   # 14: heavy object in right hand
]

# Rotation parameters
n_frames = 120  # total frames for turning motion
frame_count = 0
angle_start = -math.pi / 2  # start facing left
angle_end =  math.pi / 2    # end facing right

# Scale factor to draw the points larger on screen
SCALE = 4.0

def rotate_point_around_y(point, angle):
    """
    Rotate a 3D point (x, y, z) around the y-axis by 'angle' radians.
    Returns the rotated point (x', y', z').
    """
    x, y, z = point
    # Rotation around y-axis
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x_new = x * cos_a + z * sin_a
    z_new = -x * sin_a + z * cos_a
    return (x_new, y, z_new)

def project_to_2d(point3d):
    """
    Projects (x, y, z) onto the 2D screen.
    We use a simple orthographic projection here.
    """
    x3, y3, _ = point3d
    screen_x = center_x + int(SCALE * x3)
    screen_y = center_y - int(SCALE * y3)
    return (screen_x, screen_y)

def main():
    global frame_count
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute progress (0 to 1) in the turning motion
        u = frame_count / (n_frames - 1)
        # Interpolate angle from start to end
        angle = angle_start + (angle_end - angle_start) * u

        screen.fill((0, 0, 0))  # Black background

        # Rotate and draw each of the 15 points
        for i in range(NUM_POINTS):
            rotated_3d = rotate_point_around_y(base_skeleton_3d[i], angle)
            screen_pos = project_to_2d(rotated_3d)
            pygame.draw.circle(screen, (255, 255, 255), screen_pos, 4)  # White point-lights

        pygame.display.flip()

        frame_count += 1
        if frame_count >= n_frames:
            # Loop back to start
            frame_count = 0

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()