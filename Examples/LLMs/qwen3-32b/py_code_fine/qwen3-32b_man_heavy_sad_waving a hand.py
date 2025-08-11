
import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Man with Heavy Weight Waving Hand - Point-Light Animation")
clock = pygame.time.Clock()

# Joint indices for clarity
HEAD = 0
NECK = 1
SPINE = 2
LEFT_SHOULDER = 3
LEFT_ELBOW = 4
LEFT_WRIST = 5
RIGHT_SHOULDER = 6
RIGHT_ELBOW = 7
RIGHT_WRIST = 8
LEFT_HIP = 9
LEFT_KNEE = 10
LEFT_ANKLE = 11
RIGHT_HIP = 12
RIGHT_KNEE = 13
RIGHT_ANKLE = 14

# Base joint positions (relative to center of screen)
JOINT_OFFSETS = {
    HEAD: (0, -100),
    NECK: (0, -80),
    SPINE: (0, -40),
    LEFT_SHOULDER: (-25, -30),
    LEFT_ELBOW: (-40, 10),
    LEFT_WRIST: (-50, 50),
    RIGHT_SHOULDER: (25, -30),
    RIGHT_ELBOW: (40, 10),
    RIGHT_WRIST: (50, 50),
    LEFT_HIP: (-15, 10),
    LEFT_KNEE: (-20, 50),
    LEFT_ANKLE: (-20, 90),
    RIGHT_HIP: (15, 10),
    RIGHT_KNEE: (20, 50),
    RIGHT_ANKLE: (20, 90),
}

# Scale factor to adjust size
SCALE = 2.0

# Animation parameters
WAVE_SPEED = 0.03
WAVE_AMPLITUDE = 15
SADNESS_DROP = 10  # Vertical drop due to sadness
WEIGHT_DROP = 15   # Additional drop due to heavy weight in hand

# Function to compute positions based on time
def compute_positions(t):
    positions = []
    cx, cy = WIDTH // 2, HEIGHT // 2  # Center of the screen

    # Head, neck, spine
    for joint in [HEAD, NECK, SPINE]:
        dx, dy = JOINT_OFFSETS[joint]
        positions.append((cx + dx * SCALE, cy + dy * SCALE - SADNESS_DROP))

    # Left arm
    for i, joint in enumerate([LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST]):
        dx, dy = JOINT_OFFSETS[joint]
        angle = t * WAVE_SPEED * (i + 1)
        x = cx + (dx + math.sin(angle) * WAVE_AMPLITUDE) * SCALE
        y = cy + (dy + math.cos(angle) * WAVE_AMPLITUDE) * SCALE - SADNESS_DROP
        if joint == LEFT_WRIST:
            y += WEIGHT_DROP  # Heavy weight in hand
        positions.append((x, y))

    # Right arm (not waving)
    for joint in [RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST]:
        dx, dy = JOINT_OFFSETS[joint]
        positions.append((cx + dx * SCALE, cy + dy * SCALE - SADNESS_DROP))

    # Legs
    for joint in [LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE]:
        dx, dy = JOINT_OFFSETS[joint]
        positions.append((cx + dx * SCALE, cy + dy * SCALE - SADNESS_DROP))

    return positions

# Main loop
def main():
    t = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        t += 1
        positions = compute_positions(t)

        # Draw point-lights
        for x, y in positions:
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
