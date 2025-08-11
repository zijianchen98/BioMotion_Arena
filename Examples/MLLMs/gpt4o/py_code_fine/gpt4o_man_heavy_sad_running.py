
import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Sadman Running")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions relative to the sadman skeleton (normalized coordinates)
# The arrangement below is biomechanically plausible and corresponds to joints on the human body.
JOINTS = {
    "head": [0, -0.4],
    "torso_top": [0, -0.3],
    "torso_bottom": [0, -0.2],
    "left_shoulder": [-0.1, -0.3],
    "right_shoulder": [0.1, -0.3],
    "left_elbow": [-0.2, -0.2],
    "right_elbow": [0.2, -0.2],
    "left_hand": [-0.3, -0.1],
    "right_hand": [0.3, -0.1],
    "left_hip": [-0.1, -0.1],
    "right_hip": [0.1, -0.1],
    "left_knee": [-0.15, 0],
    "right_knee": [0.15, 0],
    "left_foot": [-0.15, 0.1],
    "right_foot": [0.15, 0.1]
}

# Scale and center the skeleton in the animation space
SCALE_FACTOR = 400
CENTER = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
def scale_and_center(position):
    return (
        CENTER[0] + position[0] * SCALE_FACTOR,
        CENTER[1] + position[1] * SCALE_FACTOR
    )

# Generate running motion using sine wave patterns for biomechanical plausibility
def generate_motion(time):
    angle = np.pi / 4  # Phase offset for limbs to create realistic running motion
    motion = {}
    motion["head"] = [JOINTS["head"][0], JOINTS["head"][1] + np.sin(time) * 0.02]
    motion["torso_top"] = JOINTS["torso_top"]
    motion["torso_bottom"] = JOINTS["torso_bottom"]
    motion["left_shoulder"] = [JOINTS["left_shoulder"][0], JOINTS["left_shoulder"][1] + np.sin(time - angle) * 0.05]
    motion["right_shoulder"] = [JOINTS["right_shoulder"][0], JOINTS["right_shoulder"][1] + np.sin(time + angle) * 0.05]
    motion["left_elbow"] = [JOINTS["left_elbow"][0], JOINTS["left_elbow"][1] + np.sin(time - angle) * 0.08]
    motion["right_elbow"] = [JOINTS["right_elbow"][0], JOINTS["right_elbow"][1] + np.sin(time + angle) * 0.08]
    motion["left_hand"] = [JOINTS["left_hand"][0], JOINTS["left_hand"][1] + np.sin(time - angle) * 0.1]
    motion["right_hand"] = [JOINTS["right_hand"][0], JOINTS["right_hand"][1] + np.sin(time + angle) * 0.1]
    motion["left_hip"] = [JOINTS["left_hip"][0], JOINTS["left_hip"][1] + np.sin(time + angle) * 0.04]
    motion["right_hip"] = [JOINTS["right_hip"][0], JOINTS["right_hip"][1] + np.sin(time - angle) * 0.04]
    motion["left_knee"] = [JOINTS["left_knee"][0], JOINTS["left_knee"][1] + np.sin(time + angle) * 0.07]
    motion["right_knee"] = [JOINTS["right_knee"][0], JOINTS["right_knee"][1] + np.sin(time - angle) * 0.07]
    motion["left_foot"] = [JOINTS["left_foot"][0], JOINTS["left_foot"][1] + np.sin(time + angle) * 0.1]
    motion["right_foot"] = [JOINTS["right_foot"][0], JOINTS["right_foot"][1] + np.sin(time - angle) * 0.1]
    return motion

# Main animation loop
running = True
start_time = pygame.time.get_ticks()
while running:
    screen.fill(BLACK)

    # Calculate simulation time
    current_time = (pygame.time.get_ticks() - start_time) / 1000  # Time in seconds

    # Generate motion at the current time
    joint_positions = generate_motion(current_time)

    # Draw point-lights to represent biological motion
    for joint, position in joint_positions.items():
        pygame.draw.circle(screen, WHITE, scale_and_center(position), 5)

    # Handle events and updates
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
