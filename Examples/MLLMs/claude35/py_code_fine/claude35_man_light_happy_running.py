
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5
FPS = 60

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Motion Animation")

# Function to draw point lights
def draw_point_lights(points):
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)

# Main loop
def main():
    clock = pygame.time.Clock()
    time = 0
    points = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Calculate positions of point lights
        for i in range(15):
            angle = 2 * math.pi * (i / 15) + time * 0.5
            radius = 50 * (1 + 0.2 * math.cos(time * 0.1))
            x = WIDTH // 2 + radius * math.cos(angle)
            y = HEIGHT // 2 + radius * math.sin(angle)
            points.append((x, y))

        # Draw the point lights
        draw_point_lights(points)

        # Update the display
        pygame.display.flip()
        
        # Clear points for next frame
        points.clear()

        # Increment time
        time += 1 / FPS

        # Maintain frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
