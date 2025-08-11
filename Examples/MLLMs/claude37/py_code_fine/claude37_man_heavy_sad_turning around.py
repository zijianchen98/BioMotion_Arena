
import pygame
import sys
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
NUM_POINTS = 15
POINT_RADIUS = 5

# Function to create point-light positions for a "turning around" motion
def get_point_positions(angle):
    positions = []
    # Initial fixed positions for simulating a sad man holding a weight
    base_positions = [(400, 200), (380, 250), (420, 250), (390, 300), (410, 300),
                      (370, 350), (430, 350), (350, 400), (450, 400),
                      (380, 450), (420, 450), (400, 500), (400, 550), (400, 600)]
    
    for pos in base_positions:
        x, y = pos
        # Rotate points around the center (400, 300)
        new_x = 400 + (x - 400) * np.cos(angle) - (y - 300) * np.sin(angle)
        new_y = 300 + (x - 400) * np.sin(angle) + (y - 300) * np.cos(angle)
        positions.append((new_x, new_y))
    
    return positions

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Stimulus Animation')
    clock = pygame.time.Clock()
    
    angle = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Fill background
        screen.fill((0, 0, 0))
        
        # Get the updated point positions
        point_positions = get_point_positions(angle)
        
        # Draw the points
        for x, y in point_positions:
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), POINT_RADIUS)
        
        # Update the angle to create the turning effect
        angle += 0.05
        if angle >= 2 * np.pi:  # Reset angle after one full rotation
            angle = 0
        
        # Refresh the screen
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
