
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point light properties
NUM_LIGHTS = 15
lights = [{'x': WIDTH // 2, 'y': HEIGHT // 2, 'radius': 3, 'angle': 0} for _ in range(NUM_LIGHTS)]

# Sadman and hand properties
sadman_x, sadman_y = WIDTH // 4, HEIGHT * 3 // 4
hand_length = 100
hand_angle = math.pi / 6  # Initial angle for the hand

# Animation parameters
frame_count = 0
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update hand position
    frame_count += 1
    hand_angle = math.sin(frame_count * 0.1) * math.pi / 6  # Sine wave for smooth motion

    # Calculate new positions for point lights
    for i, light in enumerate(lights):
        angle_offset = (i / NUM_LIGHTS) * 2 * math.pi
        light['x'] = sadman_x + hand_length * math.cos(hand_angle + angle_offset)
        light['y'] = sadman_y + hand_length * math.sin(hand_angle + angle_offset)

    # Clear screen
    screen.fill(BLACK)

    # Draw point lights
    for light in lights:
        pygame.draw.circle(screen, WHITE, (int(light['x']), int(light['y'])), light['radius'])

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
