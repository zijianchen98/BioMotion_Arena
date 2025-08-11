
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
POINT_COLOR = (255, 255, 255)  # White
FPS = 60

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-light Animation - Jumping Forward")

clock = pygame.time.Clock()

# Function to create jumping forward motion for 15 point-lights
def generate_jumping_motion(frame):
    """
    Generate positions for 15 point-lights representing a man jumping forward.

    :param frame: Current animation frame
    :return: List of positions [(x1, y1), (x2, y2), ..., (x15, y15)]
    """
    positions = []

    # Center of the jumping animation
    center_x = SCREEN_WIDTH // 2 + int((frame % 100) * 5)  # Forward movement
    center_y = SCREEN_HEIGHT // 2

    # Biomechanically plausible motion parameters
    jump_height = 50  # Maximum height of the jump
    jump_phase = math.sin(math.pi * frame / 30) * jump_height  # Vertical motion

    # Define the body structure (static relative offsets)
    body_offsets = [
        (-20, -100),  # Head
        (-40, -80), (0, -80),  # Shoulders
        (-60, -40), (-20, -40), (20, -40), (60, -40),  # Elbows + Hands
        (-40, 0), (0, 0),  # Hips
        (-60, 40), (-20, 40), (20, 40), (60, 40),  # Knees + Feet
        (-40, 80), (0, 80),  # Feet (lower extremities)
    ]

    # Simulate jumping motion
    for offset in body_offsets:
        # Dynamic positions with jump height applied
        x = center_x + offset[0]
        y = center_y + offset[1] - jump_phase
        positions.append((x, y))

    return positions

def main():
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Generate positions for current frame
        positions = generate_jumping_motion(frame)

        # Draw point-lights
        for pos in positions:
            pygame.draw.circle(screen, POINT_COLOR, pos, 5)  # Radius 5

        # Update display
        pygame.display.flip()

        # Increment frame count
        frame += 1

        # Control frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
