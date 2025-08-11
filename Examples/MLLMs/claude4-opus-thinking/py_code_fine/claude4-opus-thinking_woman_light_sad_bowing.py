
import pygame
import sys
import numpy as np

# **Constants**
WIDTH, HEIGHT = 600, 800
NUM_LIGHTS = 15
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)
FPS = 60

# **Position Settings for Lights**
# Set the base positions of the points that represent joints
def initial_positions():
    return [
        (WIDTH // 2, HEIGHT // 4),                # Head
        (WIDTH // 2 - 20, HEIGHT // 3),           # L Shoulder
        (WIDTH // 2 + 20, HEIGHT // 3),           # R Shoulder
        (WIDTH // 2 - 40, HEIGHT // 2),           # L Elbow
        (WIDTH // 2 + 40, HEIGHT // 2),           # R Elbow
        (WIDTH // 2 - 30, HEIGHT // 1.5),         # L Hand
        (WIDTH // 2 + 30, HEIGHT // 1.5),         # R Hand
        (WIDTH // 2 - 20, HEIGHT // 1.2),         # L Hip
        (WIDTH // 2 + 20, HEIGHT // 1.2),         # R Hip
        (WIDTH // 2 - 20, HEIGHT),                 # L Knee
        (WIDTH // 2 + 20, HEIGHT),                 # R Knee
        (WIDTH // 2 - 15, HEIGHT * 1.1),           # L Ankle
        (WIDTH // 2 + 15, HEIGHT * 1.1),           # R Ankle
        (WIDTH // 2, HEIGHT * 1.1),                # Sacrum
        (WIDTH // 2, HEIGHT * 1.2),                # Toes
    ]

def bowing_positions(frame, duration=60):
    # Calculate the bowing motion for the points
    angle = 15  # degrees to bow down
    rad = np.radians(angle)
    h_offset = 5 * np.sin((np.pi * frame) / duration)

    return [
        (WIDTH // 2, HEIGHT // 4 - h_offset),                  # Head
        (WIDTH // 2 - 20, HEIGHT // 3 - h_offset),             # L Shoulder
        (WIDTH // 2 + 20, HEIGHT // 3 - h_offset),             # R Shoulder
        (WIDTH // 2 - 40, HEIGHT // 2 - h_offset),             # L Elbow
        (WIDTH // 2 + 40, HEIGHT // 2 - h_offset),             # R Elbow
        (WIDTH // 2 - 30, HEIGHT // 1.5 - h_offset),           # L Hand
        (WIDTH // 2 + 30, HEIGHT // 1.5 - h_offset),           # R Hand
        (WIDTH // 2 - 20, HEIGHT // 1.2 - h_offset),           # L Hip
        (WIDTH // 2 + 20, HEIGHT // 1.2 - h_offset),           # R Hip
        (WIDTH // 2 - 20, HEIGHT - h_offset),                   # L Knee
        (WIDTH // 2 + 20, HEIGHT - h_offset),                   # R Knee
        (WIDTH // 2 - 15, HEIGHT * 1.1 - h_offset),            # L Ankle
        (WIDTH // 2 + 15, HEIGHT * 1.1 - h_offset),            # R Ankle
        (WIDTH // 2, HEIGHT * 1.1 - h_offset),                 # Sacrum
        (WIDTH // 2, HEIGHT * 1.2 - h_offset),                 # Toes
    ]

# **Main Function**
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus Animation")
    clock = pygame.time.Clock()

    positions = initial_positions()
    total_frames = 120  # Total frames for the animation

    for frame in range(total_frames):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        # Update positions based on bowing motion
        positions = bowing_positions(frame)

        # Draw the point lights
        for pos in positions:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(pos[0]), int(pos[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
