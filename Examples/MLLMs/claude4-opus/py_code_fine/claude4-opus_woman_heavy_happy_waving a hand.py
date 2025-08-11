
import pygame
import numpy as np
import sys

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 30

# Function to draw the point lights based on positions
def draw_point_lights(screen, positions):
    for pos in positions:
        pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

# Function to get the positions of the point lights
def get_positions(frame):
    # Define the base positions of the point lights for a waving motion
    joint_positions = np.array([
        [400, 100],   # Head
        [370, 150],   # Left shoulder
        [430, 150],   # Right shoulder
        [350, 250],   # Left elbow
        [450, 250],   # Right elbow
        [300, 350],   # Left hand
        [500, 350],   # Right hand
        [370, 300],   # Left hip
        [430, 300],   # Right hip
        [350, 450],   # Left knee
        [450, 450],   # Right knee
        [320, 550],   # Left foot
        [480, 550],   # Right foot
        [370, 250 + int(20 * np.sin(frame * 0.2))],  # Left Elbow animated position
        [430, 250 + int(20 * np.sin(frame * 0.2))],  # Right Elbow animated position
    ])
    
    # Add a waving motion to the hand
    joint_positions[-2, 0] += 20 * np.sin(frame * 0.2)  # Move left hand
    joint_positions[-1, 0] -= 20 * np.sin(frame * 0.2)  # Move right hand
    
    return joint_positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Animation - Happy Waving Woman')
    clock = pygame.time.Clock()
    
    frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        
        # Get current positions of the point lights
        positions = get_positions(frame)
        draw_point_lights(screen, positions)
        
        pygame.display.flip()
        frame += 1
        clock.tick(FPS)

if __name__ == "__main__":
    main()
