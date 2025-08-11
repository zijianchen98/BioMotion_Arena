
import pygame
import math
import sys

# Constants
WIDTH, HEIGHT = 800, 600
POINT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Point-light Stimulus Animation')
clock = pygame.time.Clock()

# Define positions of point-lights
# 15 points arranged to resemble a happy woman's body
points = [
    (400, 100),   # Head
    (385, 130),   # Left Shoulder
    (415, 130),   # Right Shoulder
    (380, 170),   # Left Elbow
    (420, 170),   # Right Elbow
    (350, 200),   # Left Hand
    (450, 200),   # Right Hand
    (400, 250),   # Torso
    (370, 370),   # Left Knee
    (430, 370),   # Right Knee
    (360, 500),   # Left Foot
    (440, 500),   # Right Foot
    (405, 270),   # Center Back
    (385, 300),   # Left Side
    (415, 300),   # Right Side
    (400, 400)    # Center Base
]

# Function to update point positions for bowing motion
def update_positions(angle):
    # Calculate new positions based on bowing motion
    for i in range(len(points)):
        if i == 0:  # Head doesn't move much
            points[i] = (400, 100)
        elif i < 3:  # Shoulders
            points[i] = (points[i][0] - 5 * math.sin(angle), points[i][1] + 5 * math.cos(angle))
        elif i < 5:  # Elbows
            points[i] = (points[i][0] - 10 * math.sin(angle), points[i][1] + 10 * math.cos(angle))
        elif i < 7:  # Hands
            points[i] = (points[i][0] - 15 * math.sin(angle), points[i][1] + 15 * math.cos(angle))
        elif i == 8:  # Torso moves a bit
            points[i] = (400, 250 + 10 * math.cos(angle))
        # Legs and feet will remain more fixed but simulate minor movement
        elif i >= 9:
            points[i] = (points[i][0], points[i][1] + 5 * math.sin(angle / 2))

def main():
    angle = 0
    while True:
        screen.fill(BACKGROUND_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        update_positions(angle)
        
        # Draw the points
        for point in points:
            pygame.draw.circle(screen, POINT_COLOR, (int(point[0]), int(point[1])), POINT_RADIUS)
        
        pygame.display.flip()
        angle += 0.1
        clock.tick(FPS)

if __name__ == '__main__':
    main()
