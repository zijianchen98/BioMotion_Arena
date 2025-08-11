
import pygame
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
FPS = 60

# Number of point-lights
NUM_POINTS = 15

# Happywoman-specific motion parameters (simulating forward rolling)
POINT_POSITIONS = [
    (0, -100), (30, -70), (-30, -70),  # Head (center, top-right, top-left)
    (50, -40), (-50, -40),             # Shoulders
    (70, 0), (-70, 0),                 # Elbows
    (0, 0),                            # Spine
    (40, 40), (-40, 40),               # Hips
    (70, 80), (-70, 80),               # Knees
    (30, 120), (-30, 120)              # Feet
]

ROLL_RADIUS = 150
ANGULAR_SPEED = 0.075  # Speed of rotation in radians/frame

def rotate_point(point, angle):
    """Helper function to rotate point around origin."""
    x, y = point
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

def update_positions(base_angle):
    """Simulate the forward rolling motion."""
    positions = []
    for point in POINT_POSITIONS:
        rotated_point = rotate_point(point, base_angle)
        positions.append((rotated_point[0] + SCREEN_WIDTH // 2, rotated_point[1] + SCREEN_HEIGHT // 2))
    return positions

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Point-Light Stimulus: Forward Rolling")
    clock = pygame.time.Clock()
    
    base_angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update position for the rolling animation
        base_angle += ANGULAR_SPEED
        positions = update_positions(base_angle)

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, (int(pos[0]), int(pos[1])), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
