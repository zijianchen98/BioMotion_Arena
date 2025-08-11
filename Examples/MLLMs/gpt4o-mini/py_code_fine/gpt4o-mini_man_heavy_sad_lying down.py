
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-light Stimulus Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions for a sadman lying down
# Representing major joints with a simple configuration
joint_positions = np.array([
    [300, 100],  # Head
    [270, 130],  # Left shoulder
    [330, 130],  # Right shoulder
    [260, 180],  # Left elbow
    [340, 180],  # Right elbow
    [250, 220],  # Left wrist
    [350, 220],  # Right wrist
    [300, 250],  # Chest
    [280, 280],  # Left hip
    [320, 280],  # Right hip
    [270, 320],  # Left knee
    [330, 320],  # Right knee
    [250, 360],  # Left ankle
    [350, 360],  # Right ankle
])

# Function to update positions for realistic motion
def update_positions(joint_positions, t):
    # Simple downward motion to simulate the sadman's weight as he lies down
    displacement = np.array([0, 0.5 * np.sin(t / 10)])  # Vertical oscillation
    return joint_positions + displacement

# Main loop
clock = pygame.time.Clock()
running = True
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Update positions
    current_positions = update_positions(joint_positions, t)

    # Fill background
    screen.fill(BLACK)

    # Draw point-lights
    for pos in current_positions:
        pygame.draw.circle(screen, WHITE, pos.astype(int), 5)

    # Update display
    pygame.display.flip()

    # Increment time variable
    t += 1

    # Control the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
