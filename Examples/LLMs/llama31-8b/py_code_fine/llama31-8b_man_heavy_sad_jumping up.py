
import pygame
import numpy as np

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
LIGHT_RADIUS = 5
LIGHT_SPEED = 5

# Sadman's joint positions (in pixels)
JOINTS = np.array([
    [WIDTH // 2, HEIGHT // 2],  # Center
    [WIDTH // 2 - 100, HEIGHT // 2 + 50],  # Left hip
    [WIDTH // 2 + 100, HEIGHT // 2 + 50],  # Right hip
    [WIDTH // 2 - 50, HEIGHT // 2 - 50],  # Left knee
    [WIDTH // 2 + 50, HEIGHT // 2 - 50],  # Right knee
    [WIDTH // 2 - 100, HEIGHT // 2 - 100],  # Left ankle
    [WIDTH // 2 + 100, HEIGHT // 2 - 100],  # Right ankle
    [WIDTH // 2 - 150, HEIGHT // 2 + 100],  # Left foot
    [WIDTH // 2 + 150, HEIGHT // 2 + 100],  # Right foot
    [WIDTH // 2 - 50, HEIGHT // 2 - 150],  # Left hand
    [WIDTH // 2 + 50, HEIGHT // 2 - 150],  # Right hand
    [WIDTH // 2 - 150, HEIGHT // 2 + 150],  # Left shoulder
    [WIDTH // 2 + 150, HEIGHT // 2 + 150],  # Right shoulder
    [WIDTH // 2 - 200, HEIGHT // 2],  # Left head
    [WIDTH // 2 + 200, HEIGHT // 2],  # Right head
])

# Animation loop
def animate():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Initial joint positions
    joints = JOINTS.copy()

    # Animation loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)

        # Draw point lights
        for i in range(len(joints)):
            pygame.draw.circle(screen, WHITE, (int(joints[i][0]), int(joints[i][1])), LIGHT_RADIUS)

        # Update joint positions
        joints[0][1] -= LIGHT_SPEED  # Center
        joints[1][0] -= LIGHT_SPEED  # Left hip
        joints[2][0] += LIGHT_SPEED  # Right hip
        joints[3][0] -= LIGHT_SPEED  # Left knee
        joints[4][0] += LIGHT_SPEED  # Right knee
        joints[5][0] -= LIGHT_SPEED  # Left ankle
        joints[6][0] += LIGHT_SPEED  # Right ankle
        joints[7][0] -= LIGHT_SPEED  # Left foot
        joints[8][0] += LIGHT_SPEED  # Right foot
        joints[9][0] -= LIGHT_SPEED  # Left hand
        joints[10][0] += LIGHT_SPEED  # Right hand
        joints[11][0] -= LIGHT_SPEED  # Left shoulder
        joints[12][0] += LIGHT_SPEED  # Right shoulder
        joints[13][0] -= LIGHT_SPEED  # Left head
        joints[14][0] += LIGHT_SPEED  # Right head

        # Boundary checking
        for i in range(len(joints)):
            if joints[i][0] < 0:
                joints[i][0] = 0
            elif joints[i][0] > WIDTH:
                joints[i][0] = WIDTH
            if joints[i][1] < 0:
                joints[i][1] = 0
            elif joints[i][1] > HEIGHT:
                joints[i][1] = HEIGHT

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)

    pygame.quit()

animate()
