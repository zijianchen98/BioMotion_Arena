
import pygame
import time
import math

# Constants
WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
POINT_RADIUS = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Sad Man Sitting Down")

# Define the positions of the point lights
# These positions correspond to the joints in the sitting action
point_lights = [
    (300, 50),   # Head
    (280, 80),   # Shoulder Left
    (320, 80),   # Shoulder Right
    (260, 120),  # Elbow Left
    (300, 130),  # Hand Left
    (320, 120),  # Elbow Right
    (340, 130),  # Hand Right
    (280, 180),  # Hip Left
    (320, 180),  # Hip Right
    (280, 260),  # Knee Left
    (300, 300),  # Ankle Left
    (320, 260),  # Knee Right
    (340, 300),  # Ankle Right
    (290, 250),  # Foot Left
    (310, 250),  # Foot Right
]

# Function to animate the sitting action
def animate_sitting():
    for i in range(40):  # Number of frames
        screen.fill(BACKGROUND_COLOR)

        # Update the vertical position to simulate sitting
        for j in range(len(point_lights)):
            x, y = point_lights[j]
            # For the sitting motion, we will lower the y-coordinate of certain points
            if j in [0, 1, 2]:  # Head and shoulders stay relatively high
                new_y = y
            elif j in [3, 4, 5, 9, 10]:  # Elbows and hands lower a bit
                new_y = y + i * 2
            else:  # Hips, knees, and feet lower significantly
                new_y = y + i * 4
            
            pygame.draw.circle(screen, POINT_COLOR, (x, new_y), POINT_RADIUS)

        pygame.display.flip()
        time.sleep(0.05)  # Control the speed of the animation

# Run the animation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    animate_sitting()

pygame.quit()
