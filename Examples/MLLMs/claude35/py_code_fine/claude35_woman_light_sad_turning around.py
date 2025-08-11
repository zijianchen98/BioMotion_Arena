
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_LIGHTS = 15
RADIUS = 5
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
TURN_RADIUS = 100

# Function to calculate the position of the lights
def calculate_positions(angle):
    positions = []
    for i in range(NUM_LIGHTS):
        theta = (math.pi * 2 / NUM_LIGHTS) * i + angle
        x = CENTER_X + TURN_RADIUS * math.cos(theta)
        y = CENTER_Y + TURN_RADIUS * math.sin(theta)
        positions.append((x, y))
    return positions

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Animation")
    clock = pygame.time.Clock()

    # Main loop
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill((0, 0, 0))

        # Calculate light positions
        positions = calculate_positions(angle)

        # Draw point lights
        for pos in positions:
            pygame.draw.circle(screen, (255, 255, 255), (int(pos[0]), int(pos[1])), RADIUS)

        # Update angle for rotation
        angle += 0.05  # Adjust speed of rotation here
        if angle > 2 * math.pi:
            angle -= 2 * math.pi

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
