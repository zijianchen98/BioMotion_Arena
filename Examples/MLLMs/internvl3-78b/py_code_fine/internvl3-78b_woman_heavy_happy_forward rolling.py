
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the display window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sadman Forward Rolling Animation")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the frame rate
clock = pygame.time.Clock()
frame_rate = 60

# Position and radius of the point-lights
positions = [
    [150, 50], [180, 50], [210, 50], [240, 50], [270, 50],
    [145, 130], [185, 130], [220, 130], [255, 130], [285, 130],
    [155, 210], [195, 210], [225, 210], [255, 210], [295, 210],
]
radius = 5

def animate_screen(positions):
    for pos in positions:
        pygame.draw.circle(screen, white, pos, radius)

def update_positions(positions):
    for pos in positions:
        pos[0] += 1  # Move horizontally to simulate the backward motion
        pos[1] += 1  # Move vertically to simulate the forward motion

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        animate_screen(positions)
        update_positions(positions)
        pygame.display.flip()
        clock.tick(frame_rate)

if __name__ == '__main__':
    main()
