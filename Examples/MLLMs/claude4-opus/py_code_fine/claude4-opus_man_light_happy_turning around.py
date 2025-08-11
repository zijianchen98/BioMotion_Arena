
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
NUM_LIGHTS = 15
RADIUS = 10  # Radius of the point lights.
FPS = 60  # Frames per second

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation - Happy Man Turning Around")
clock = pygame.time.Clock()

def draw_point_lights(angle):
    # Calculate the positions of the point lights to simulate a happy man turning around
    positions = []
    for i in range(NUM_LIGHTS):
        x = WIDTH // 2 + 100 * math.cos(angle + i * (2 * math.pi / NUM_LIGHTS))
        y = HEIGHT // 2 + 100 * math.sin(angle + i * (2 * math.pi / NUM_LIGHTS))
        positions.append((x, y))

    # Draw the point lights
    for pos in positions:
        pygame.draw.circle(screen, POINT_LIGHT_COLOR, (int(pos[0]), int(pos[1])), RADIUS)

def main():
    angle = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Update the angle to simulate turning
        angle += 0.05  # Adjust speed of rotation
        if angle > 2 * math.pi:  # Reset angle after a full rotation
            angle -= 2 * math.pi

        # Draw point lights
        draw_point_lights(angle)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
