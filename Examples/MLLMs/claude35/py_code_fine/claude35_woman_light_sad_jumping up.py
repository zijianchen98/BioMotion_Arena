
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)
POINT_COUNT = 15
FPS = 30

# Define the points for the body parts
joint_positions = np.array([
    [WIDTH // 2, HEIGHT - 100],  # Head
    [WIDTH // 2, HEIGHT - 80],   # Neck
    [WIDTH // 2 - 30, HEIGHT - 60],  # Left Shoulder
    [WIDTH // 2 + 30, HEIGHT - 60],  # Right Shoulder
    [WIDTH // 2 - 30, HEIGHT - 30],  # Left Elbow
    [WIDTH // 2 + 30, HEIGHT - 30],  # Right Elbow
    [WIDTH // 2 - 60, HEIGHT],        # Left Hand
    [WIDTH // 2 + 60, HEIGHT],        # Right Hand
    [WIDTH // 2 - 40, HEIGHT - 100],  # Left Hip
    [WIDTH // 2 + 40, HEIGHT - 100],  # Right Hip
    [WIDTH // 2 - 30, HEIGHT - 20],   # Left Knee
    [WIDTH // 2 + 30, HEIGHT - 20],   # Right Knee
    [WIDTH // 2 - 30, HEIGHT],         # Left Foot
    [WIDTH // 2 + 30, HEIGHT],         # Right Foot
    [WIDTH // 2, HEIGHT - 150],        # Torso
])

# Movement parameters
jump_height = 100
jump_duration = FPS * 1  # 1 second
fall_duration = FPS * 0.5  # 0.5 second

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Point-Light Biological Motion Animation')

    clock = pygame.time.Clock()
    time_passed = 0
    jumping = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        if jumping:
            if time_passed < jump_duration:
                # Calculate jump displacement
                y_offset = -jump_height * np.sin(np.pi * time_passed / jump_duration)
                time_passed += 1
                
                # Update the y coordinates for jumping
                current_positions = joint_positions.copy()
                current_positions[:, 1] += y_offset
            else:
                # Transition to falling
                jumping = False
                time_passed = 0  # Reset time for falling

        else:
            if time_passed < fall_duration:
                # Calculate fall displacement
                y_offset = (jump_height * (time_passed / fall_duration))
                time_passed += 1
                
                # Update the y coordinates for falling
                current_positions = joint_positions.copy()
                current_positions[:, 1] += y_offset
            else:
                # Reset for another jump
                jumping = True
                time_passed = 0

        # Draw the points
        for pos in current_positions:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(pos[0]), int(pos[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
