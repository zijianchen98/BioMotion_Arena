
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINT_COLOR = (255, 255, 255)  # White color
BACKGROUND_COLOR = (0, 0, 0)  # Black background
FPS = 60

# Define the point light configuration
points = [
    (400, 100),  # Head
    (370, 150), (430, 150),  # Shoulders
    (350, 200), (450, 200),  # Elbows
    (325, 250), (475, 250),  # Wrists
    (300, 300), (500, 300),  # Hips
    (350, 350), (450, 350),  # Knees
    (320, 400), (480, 400),  # Ankles
    (350, 450), (450, 450),  # Feet
    (400, 500)   # Extra point for weight
]

# Function to render the point lights
def render_points(screen, points):
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, point, 5)

# Function to animate the object
def animate():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus - Sadman Lying Down")

    t = 0  # Time variable to control motion
    moving_down = True  # Control the downward motion of the weight point

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)
        
        # Update position based on time
        if moving_down:
            t += 1
            if t > 25:  # Switch direction after certain time
                moving_down = False
        else:
            t -= 1
            if t < 0:  # Reset once it goes back to initial position
                moving_down = True

        # Update the floating weight point
        weight_point = (400, 500 + t)
        updated_points = points + [weight_point]

        # Render all points
        render_points(screen, updated_points)

        # Refresh display
        pygame.display.flip()
        clock.tick(FPS)

# Run the animation
if __name__ == "__main__":
    animate()
