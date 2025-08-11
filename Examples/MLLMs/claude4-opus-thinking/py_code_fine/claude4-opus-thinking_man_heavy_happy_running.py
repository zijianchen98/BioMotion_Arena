
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
NUM_LIGHTS = 15
POINT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation")

# Generate initial positions for the point lights
def generate_positions():
    # Positions are centered and adjusted for animation
    return [(WIDTH // 2 + math.sin(i * 2 * math.pi / NUM_LIGHTS) * 50,
             HEIGHT // 2 + math.cos(i * 2 * math.pi / NUM_LIGHTS) * 50) for i in range(NUM_LIGHTS)]

# Update positions based on running motion
def update_positions(positions, frame):
    angle = frame * 0.1  # Speed of running
    for i in range(len(positions)):
        x_offset = 30 * math.sin(angle + i * (2 * math.pi / NUM_LIGHTS))
        y_offset = 20 * math.cos(angle + i * (2 * math.pi / NUM_LIGHTS))
        positions[i] = (WIDTH // 2 + x_offset, HEIGHT // 2 + y_offset)

# Main loop
def main():
    clock = pygame.time.Clock()
    positions = generate_positions()
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update positions for the next frame
        update_positions(positions, frame)
        frame += 1

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

# Run the program
if __name__ == "__main__":
    main()
