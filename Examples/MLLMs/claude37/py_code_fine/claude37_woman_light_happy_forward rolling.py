
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)
FPS = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Stimulus Animation')

# Function to draw the point lights
def draw_point_lights(frame):
    points = []

    # Calculate the positions of the point lights based on a forward roll
    for i in range(15):
        angle = (math.pi / 15) * (i + frame)  # Creating a rolling motion
        x = WIDTH // 2 + 50 * math.sin(angle)
        y = HEIGHT // 2 + 50 * (i - 7)  # Adjust the vertical position
        points.append((x, y))
    
    # Draw the lights on the screen
    for point in points:
        pygame.draw.circle(screen, LIGHT_COLOR, (int(point[0]), int(point[1])), 5)

# Main loop
running = True
frame = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw point lights
    draw_point_lights(frame)

    # Update the display
    pygame.display.flip()
    
    # Update frame count
    frame += 1
    
    # Maintain the desired frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
