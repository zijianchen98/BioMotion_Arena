
import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
RADIUS = 5
FPS = 30

# Positions of point lights representing a figure
# Customize these values to create a bowing motion
INITIAL_POSITIONS = np.array([
    [400, 150],  # Head
    [375, 175],  # Shoulder Left
    [425, 175],  # Shoulder Right
    [350, 250],  # Elbow Left
    [450, 250],  # Elbow Right
    [300, 350],  # Hand Left
    [500, 350],  # Hand Right
    [375, 300],  # Hip Left
    [425, 300],  # Hip Right
    [350, 500],  # Knee Left
    [450, 500],  # Knee Right
    [325, 600],  # Foot Left
    [475, 600],  # Foot Right
    [400, 250],  # Center for bowing
    [400, 300],  # Weight Center
    [400, 350]   # Additional weighted point for depth
])

def calculate_bowing_motion(frame):
    """ Calculate positions for bowing action. """
    bow_angle = np.pi / 4 * np.sin(frame / 20)  # Sine wave for smooth oscillation
    bow_offset = 10 * np.sin(frame / 15)  # Offset for the bowing movement
    positions = INITIAL_POSITIONS.copy()
    
    # Modify positions for bowing
    positions[0][1] += bow_offset  # Head
    positions[1][1] += bow_offset / 2  # Shoulder Left
    positions[2][1] += bow_offset / 2  # Shoulder Right
    positions[3][1] += bow_offset / 2  # Elbow Left
    positions[4][1] += bow_offset / 2  # Elbow Right
    positions[5][1] += bow_offset  # Hand Left
    positions[6][1] += bow_offset  # Hand Right
    # Adjust knees and feet to be more realistic
    positions[9][1] += bow_offset / 2  # Knee Left
    positions[10][1] += bow_offset / 2  # Knee Right
    return positions

def main():
    """ Main function to run the animation. """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    frame = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Get updated positions
        positions = calculate_bowing_motion(frame)

        # Draw point lights
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), RADIUS)

        pygame.display.flip()
        clock.tick(FPS)
        frame += 1

    pygame.quit()

if __name__ == "__main__":
    main()
