
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FPS = 30
POINT_RADIUS = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Point-light Animation")

# Clock to control frame rate
clock = pygame.time.Clock()

# Define the skeleton with coordinates (x, y)
# Points relative to the torso (center of the screen)
happyman_points = {
    "head": (0, -120),
    "shoulder_l": (-50, -80),
    "shoulder_r": (50, -80),
    "elbow_l": (-80, -40),
    "elbow_r": (80, -40),
    "hand_l": (-120, -10),
    "hand_r": (120, -10),
    "torso": (0, 0),
    "hip_l": (-40, 60),
    "hip_r": (40, 60),
    "knee_l": (-50, 120),
    "knee_r": (50, 120),
    "foot_l": (-60, 180),
    "foot_r": (60, 180),
    "center": (0, 0),  # This is the reference point for torso alignment
}

# Function to update hand movements for waving
def update_motion(frame):
    # Waving motion for the left hand
    angle = math.sin(frame / 10) * math.pi / 4  # Oscillating between -45 and 45 degrees
    hand_x = happyman_points["elbow_l"][0] + math.cos(angle) * 40
    hand_y = happyman_points["elbow_l"][1] + math.sin(angle) * 40
    happyman_points["hand_l"] = (hand_x, hand_y)

# Draw function
def draw_points(screen, center_x, center_y):
    for point, offset in happyman_points.items():
        x = center_x + offset[0]
        y = center_y + offset[1]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), POINT_RADIUS)

# Main loop
def main():
    frame = 0
    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update waving motion
        update_motion(frame)
        frame += 1

        # Clear screen
        screen.fill(BLACK)

        # Draw points
        draw_points(screen, center_x, center_y)

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

# Run the program
main()
