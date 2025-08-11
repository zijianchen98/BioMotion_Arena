
import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
POINT_RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)  # Black
POINT_COLOR = (255, 255, 255)  # White
FPS = 30

# Joint movement offsets for the sitting animation
joint_positions = [
    {'x': 400, 'y': 200},  # Head
    {'x': 370, 'y': 250},  # Left Shoulder
    {'x': 430, 'y': 250},  # Right Shoulder
    {'x': 360, 'y': 320},  # Left Elbow
    {'x': 440, 'y': 320},  # Right Elbow
    {'x': 350, 'y': 400},  # Left Hand
    {'x': 450, 'y': 400},  # Right Hand
    {'x': 370, 'y': 380},  # Waist Left
    {'x': 430, 'y': 380},  # Waist Right
    {'x': 360, 'y': 480},  # Left Knee
    {'x': 440, 'y': 480},  # Right Knee
    {'x': 350, 'y': 550},  # Left Foot
    {'x': 450, 'y': 550},  # Right Foot
    {'x': 400, 'y': 350},  # Spine Mid-top
    {'x': 400, 'y': 400},  # Spine Mid-bottom
]

# Function to animate the joint positions
def animate_points():
    for index, joint in enumerate(joint_positions):
        amplitude_x = 5 + (index % 3) * 2  # Adding natural variation
        amplitude_y = 3 + (index % 2) * 4
        frequency = 0.1 + (index % 5) * 0.03

        # Update positions with natural oscillation
        joint['x'] += amplitude_x * math.sin(pygame.time.get_ticks() * 0.002 * frequency)
        joint['y'] += amplitude_y * math.cos(pygame.time.get_ticks() * 0.002 * frequency)

# Main program
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Biological Motion: Sitting Happy Woman')
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        animate_points()

        # Draw the points
        for joint in joint_positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(joint['x']), int(joint['y'])), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
