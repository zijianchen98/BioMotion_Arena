
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
NUM_LIGHTS = 15
POINT_RADIUS = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")
clock = pygame.time.Clock()

# Function to calculate positions for point lights
def calculate_positions(angle):
    positions = []
    for i in range(NUM_LIGHTS):
        # Simple example: arrange lights in a circle
        theta = (2 * math.pi / NUM_LIGHTS) * i + angle
        x = WIDTH // 2 + 100 * math.cos(theta)  # Adjust radius as needed
        y = HEIGHT // 2 + 100 * math.sin(theta)  # Adjust radius as needed
        positions.append((x, y))
    return positions

# Main loop
def main():
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update angle for rotation
        angle += 0.1  # Adjust speed of rotation
        
        # Clear screen
        screen.fill((0, 0, 0))

        # Calculate positions and draw point lights
        positions = calculate_positions(angle)
        for pos in positions:
            pygame.draw.circle(screen, (255, 255, 255), (int(pos[0]), int(pos[1])), POINT_RADIUS)

        # Refresh display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
