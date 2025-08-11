
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINT_LIGHTS_COUNT = 15
POINT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation")
clock = pygame.time.Clock()

# Function to draw point-lights
def draw_point_lights(positions):
    for pos in positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), POINT_RADIUS)

# Calculate positions based on a sine wave to simulate walking
def calculate_positions(time):
    positions = []
    # Define the base position
    base_x = WIDTH // 2
    base_y = HEIGHT // 2
    # Calculate the positions of point-lights
    for i in range(POINT_LIGHTS_COUNT):
        angle = math.radians((i/POINT_LIGHTS_COUNT) * 180)  # Spread the points around
        x = base_x + 50 * math.sin(time + i)  # Simulate walking motion
        y = base_y + 30 * math.sin(angle + time)  # Vertical spread
        positions.append((x, y))
    return positions

# Main loop
def main():
    time = 0  # Time variable for animation
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)  # Fill background

        # Update positions
        positions = calculate_positions(time)
        draw_point_lights(positions)

        # Update time for smooth animation
        time += 0.1

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Maintain the frame rate

# Run the program
if __name__ == "__main__":
    main()
