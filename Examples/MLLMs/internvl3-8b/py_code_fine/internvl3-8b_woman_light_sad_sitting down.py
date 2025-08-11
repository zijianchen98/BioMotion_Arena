
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color to black for the sad woman figure
pygame.display.set_caption('Sad Woman Sitting Down Animation')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Helper function to draw the figure
def draw_sad_woman_figure():
    for i in range(15):
        x = random.randint(50, screen_width - 50)
        y = random.randint(50, screen_height - 50)
        screen.fill(black)
        pygame.draw.circle(screen, white, (x, y), 10)  # 10 is the size of the circle
        pygame.display.flip()  # Update the display

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the figure position
    draw_sad_woman_figure()

    # Clear the screen before the next frame
    screen.fill(black)

    # Frame rate cap
    pygame.time.Clock().tick(60)

pygame.quit()
