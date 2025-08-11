
import pygame
import time

# Initialize the pygame library
pygame.init()

# Get info on monitor resolution
screen_info = pygame.display.Info()
# Set display screen dimensions
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set screen size
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title of the window
pygame.display.set_caption('A man is lying down')

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)

# Coordinates of points
coordinates = [(screen_width//2, screen_height//4 - i) for i in range(15)]

# Define movement directions (left, right, both directions)
directions = []

for i in range(15):
    if i % 2 == 0:
        directions.append(1)  # move right
    else:
        directions.append(-1)  # move left

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(15):
        screen.fill(black)  # Fill the screen with black at each frame

        # Draw each dot on the screen
        for j, (x, y) in enumerate(coordinates):
            pygame.draw.circle(screen, white, (x, y), 5)

        # Move points
        coordinates[i] = coordinates[i][0] + directions[i]*2, coordinates[i][1]

        if coordinates[i][0] + directions[i] > screen_width:
            directions[i] = -1
        elif coordinates[i][0] + directions[i] < 0:
            directions[i] = 1

        # Update the display
        pygame.display.flip()
        time.sleep(0.04)  # Delay of 0.1 sec

# End of the program
pygame.quit()
