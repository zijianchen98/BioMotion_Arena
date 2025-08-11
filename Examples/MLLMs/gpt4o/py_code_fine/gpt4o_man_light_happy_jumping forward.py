
import pygame
import math
from itertools import cycle

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Stimulus Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Frame rate
clock = pygame.time.Clock()
fps = 30

# Point-light structure for a jumping figure
# Coordinates define relative anatomy - adjust to move the object
# List defines x, y positions of key body joints of a stickman
jump_cycle = [
    [[300, 350], [280, 370], [320, 370], [280, 390], [320, 390], [300, 400], [300, 430], [280, 460], [320, 460], [260, 410], [340, 410], [300, 370], [270, 350], [330, 350], [300, 300]],

    [[300, 340], [280, 360], [320, 360], [280, 380], [320, 380], [300, 390], [300, 420], [290, 450], [310, 450], [270, 400], [330, 400], [300, 350], [270, 340], [330, 340], [300, 290]],

    [[300, 330], [290, 350], [310, 350], [300, 370], [300, 370], [300, 380], [300, 410], [290, 440], [310, 440], [280, 390], [320, 390], [300, 340], [280, 330], [320, 330], [300, 280]],

    [[300, 320], [290, 340], [310, 340], [300, 360], [300, 360], [300, 370], [300, 400], [290, 430], [310, 430], [280, 380], [320, 380], [300, 330], [280, 320], [320, 320], [300, 270]],

    [[300, 350], [280, 370], [320, 370], [280, 390], [320, 390], [300, 400], [300, 430], [280, 460], [320, 460], [260, 410], [340, 410], [300, 370], [270, 350], [330, 350], [300, 300]],
]

# Cycle through jumps
jump_positions = cycle(jump_cycle)

def draw_figure(points):
    """ Function to draw point-light figure on screen """
    for point in points:
        pygame.draw.circle(screen, white, point, 5)

running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the next frame of jump position
    points = next(jump_positions)

    # Draw the figure
    draw_figure(points)

    # Update the display
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
