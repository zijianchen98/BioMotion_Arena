
import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINTS = 15
RADIUS = 5
BACKGROUND_COLOR = (0, 0, 0)
LIGHT_COLOR = (255, 255, 255)

# Walking pattern for a happy man's animation (coordinates for point-lights)
def walking_animation(frame):
    positions = []
    # Define the positions for point-lights
    # Head, torso, arms, and legs
    for i in range(POINTS):
        angle = math.radians(30 * frame + i * (360 / POINTS))
        x = WIDTH // 2 + 50 * math.cos(angle) * (1 + 0.5 * math.sin(frame * 0.1))
        y = HEIGHT // 2 + 50 * math.sin(angle) * (1 + 0.5 * math.sin(frame * 0.1))
        positions.append((x, y))
    return positions

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-light Walking Animation")

    clock = pygame.time.Clock()
    frame = 0

    # Animation loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Get positions of point-lights
        point_positions = walking_animation(frame)

        # Draw point-lights
        for pos in point_positions:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(pos[0]), int(pos[1])), RADIUS)

        # Update the display
        pygame.display.flip()

        # Increment frame count
        frame += 1
        clock.tick(FPS)

    pygame.quit()

# Run the animation
if __name__ == "__main__":
    main()
