
import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
POINT_LIGHTS = 15
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-Light Animation: Jumping Forward')
clock = pygame.time.Clock()

# Function to draw point lights
def draw_point_lights(y_offset):
    for i in range(POINT_LIGHTS):
        # Calculate the x position based on the current frame
        x = WIDTH // 2 + (i - POINT_LIGHTS // 2) * 20
        # y position for jumping effect
        y = HEIGHT // 2 - (20 * math.sin(y_offset + i * 0.5))  # Smooth jumping effect
        # Draw the point light
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

# Main loop
if __name__ == "__main__":
    y_offset = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill((0, 0, 0))
        # Draw point lights
        draw_point_lights(y_offset)
        
        # Update display
        pygame.display.flip()
        # Increment the y_offset for smooth animation
        y_offset += 0.1
        
        # Frame rate
        clock.tick(FPS)
