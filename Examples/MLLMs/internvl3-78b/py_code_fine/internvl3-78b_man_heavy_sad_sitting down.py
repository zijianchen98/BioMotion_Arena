
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants for screen dimensions and the number of points
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
NUM_POINTS = 15
BACKGROUND_COLOR = (0, 0, 0)  # Black background

# Display setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sadman Sitting Down Animation")

# Function to generate the initial positions of the points in a specific formation
def initialize_points():
    # Base positions are hardcoded to mimic a sad, heavy sitting motion
    base_positions = np.array([
        (SCREEN_WIDTH // 2, 200),  # Head
        (SCREEN_WIDTH // 2 - 30, 230),  # Neck
        (SCREEN_WIDTH // 2 - 40, 300),  # Left Shoulder
        (SCREEN_WIDTH // 2 + 40, 300),  # Right Shoulder
        (SCREEN_WIDTH // 2 - 70, 350),  # Left Upper Arm
        (SCREEN_WIDTH // 2 + 70, 350),  # Right Upper Arm
        (SCREEN_WIDTH // 2 - 100, 400),  # Left Lower Arm
        (SCREEN_WIDTH // 2 + 100, 400),  # Right Lower Arm
        (SCREEN_WIDTH // 2, 300),         # Chest
        (SCREEN_WIDTH // 2 - 50, 450),    # Left Hip
        (SCREEN_WIDTH // 2 + 50, 450),    # Right Hip
        (SCREEN_WIDTH // 2 - 80, 520),    # Left Upper Leg
        (SCREEN_WIDTH // 2 + 80, 520),    # Right Upper Leg
        (SCREEN_WIDTH // 2 - 110, 590),   # Left Lower Leg
        (SCREEN_WIDTH // 2 + 110, 590)    # Right Lower Leg
    ])
    return base_positions

# Function to calculate the movement of the points
def move_points(points, step):
    motion_factor = 0.1 * step  # Influences the movement's timing and spacing
    offset = np.array([
        (0, np.sin(motion_factor) * 5),  # Head
        (0, np.sin(motion_factor + np.pi / 2) * 5),  # Neck
        (-np.cos(motion_factor) * 3, np.sin(motion_factor) * 5),  # Left Shoulder
        (np.cos(motion_factor) * 3, np.sin(motion_factor) * 5),  # Right Shoulder
        (-np.cos(motion_factor) * 5, np.sin(motion_factor) * 2),  # Left Upper Arm
        (np.cos(motion_factor) * 5, np.sin(motion_factor) * 2),  # Right Upper Arm
        (-np.cos(motion_factor) * 2, np.sin(motion_factor) * 10),  # Left Lower Arm
        (np.cos(motion_factor) * 2, np.sin(motion_factor) * 10),  # Right Lower Arm
        (0, np.sin(motion_factor) * 3),  # Chest
        (-np.cos(motion_factor) * 4, np.sin(motion_factor) * 5),  # Left Hip
        (np.cos(motion_factor) * 4, np.sin(motion_factor) * 5),  # Right Hip
        (-np.cos(motion_factor) * 2, np.sin(motion_factor) * 10),  # Left Upper Leg
        (np.cos(motion_factor) * 2, np.sin(motion_factor) * 10),  # Right Upper Leg
        (-np.cos(motion_factor) * 1, np.sin(motion_factor) * 5),  # Left Lower Leg
        (np.cos(motion_factor) * 1, np.sin(motion_factor) * 5)  # Right Lower Leg
    ])
    return points + offset

def main():
    clock = pygame.time.Clock()
    points = initialize_points()
    step = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        
        # Move points over time
        new_points = move_points(points, step)
        
        for point in new_points:
            pygame.draw.circle(screen, (255, 255, 255), (round(point[0]), round(point[1])), 5)
        
        pygame.display.flip()
        clock.tick(60)  # Ensuring the animation runs at 60 FPS
        step += 0.02  # Increase step to progress movement

    pygame.quit()

if __name__ == "__main__":
    main()
