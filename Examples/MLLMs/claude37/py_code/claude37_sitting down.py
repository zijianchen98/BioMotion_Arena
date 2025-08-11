
import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30

# Define point-light positions for sitting down
# Each point corresponds to a joint position in a simplified human model
points_initial = np.array([
    [400, 100],  # Head
    [380, 160],  # Left shoulder
    [420, 160],  # Right shoulder
    [360, 220],  # Left elbow
    [440, 220],  # Right elbow
    [370, 280],  # Left wrist
    [430, 280],  # Right wrist
    [400, 300],  # Spine
    [360, 400],  # Left hip
    [440, 400],  # Right hip
    [380, 500],  # Left knee
    [420, 500],  # Right knee
    [380, 550],  # Left ankle
    [420, 550],  # Right ankle
    [400, 600],  # Feet
    [400, 450]   # Torso center (to show stability)
])

# Define the animation frames for sitting down
def get_sitting_down_animation_frames():
    frames = []
    for t in np.linspace(0, 1, 30):  # 30 frames for the sitting motion
        interpolated_points = points_initial + np.array([
            [0, -80 * t],  # Head moves down
            [0, -80 * t],  # Both shoulders move down
            [0, -80 * t],
            [0, -60 * t],  # Elbows move down slightly
            [0, -60 * t],
            [0, -40 * t],  # Wrists follow
            [0, -40 * t],
            [0, 0],        # Spine remains in place initially
            [0, -20 * t],  # Hips move down
            [0, -20 * t],
            [0, -20 * t],  # Knees move down
            [0, -20 * t],
            [0, 0],  
            [0, 0],
            [0, 0],  
            [0, -50 * t]   # Torso center moves down
        ])
        frames.append(interpolated_points)
    return frames

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Sitting Down")

# Main loop
running = True
clock = pygame.time.Clock()
frames = get_sitting_down_animation_frames()
index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen to black

    # Draw point-lights
    for point in frames[index]:
        pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    clock.tick(FPS)

    index += 1
    if index >= len(frames):
        index = 0  # Loop back to the start

pygame.quit()
