
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Animation: Sad Man Sitting Down")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light positions for the human figure
points = [
    (400, 100),  # head
    (370, 150), (430, 150),  # shoulders
    (350, 250), (450, 250),  # arms
    (380, 300), (420, 300),  # elbows
    (350, 400), (450, 400),  # hands
    (400, 400),  # torso
    (370, 500), (430, 500),  # thighs
    (350, 550), (450, 550),  # knees
    (400, 550)   # feet
]

# Function to simulate the motion of sitting down
def sit_down_animation(screen, points):
    for i in range(25):  # Number of animation frames
        screen.fill(BLACK)  # Clear the screen
        offset_y = i * 4   # Incrementally lower the points for "sitting down"
        
        # Draw points
        for j, (x, y) in enumerate(points):
            if j == 0:  # Head
                pygame.draw.circle(screen, WHITE, (x, y - offset_y), 10)
            else:
                pygame.draw.circle(screen, WHITE, (x, y + offset_y), 5)
        
        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Delay to control animation speed

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        sit_down_animation(screen, points)
        break  # Exit after one loop for demo purposes

if __name__ == "__main__":
    main()
