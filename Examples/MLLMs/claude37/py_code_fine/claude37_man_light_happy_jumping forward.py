
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)  # White
NUM_POINTS = 15
FPS = 60
JUMP_HEIGHT = 100
JUMP_DISTANCE = 300

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Jumping Forward")

# Point Light Positions (2D list to represent body segments)
points = [(WIDTH // 2, HEIGHT // 2)] * NUM_POINTS 

# Update point positions based on a sine wave for jumping motion
def update_points(frame):
    for i in range(NUM_POINTS):
        angle = (frame + i * (360 / NUM_POINTS)) * (math.pi / 180)
        # Simple jump trajectory
        x_offset = (frame / FPS) * (JUMP_DISTANCE / 60) 
        y_offset = -math.sin(angle) * JUMP_HEIGHT
        # Adjust position
        points[i] = (WIDTH // 2 + int(x_offset), HEIGHT // 2 + int(y_offset))

# Main loop
clock = pygame.time.Clock()
running = True
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    # Update points position
    update_points(frame)
    
    # Draw points
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), 5)

    pygame.display.flip()
    frame += 1
    clock.tick(FPS)

pygame.quit()
