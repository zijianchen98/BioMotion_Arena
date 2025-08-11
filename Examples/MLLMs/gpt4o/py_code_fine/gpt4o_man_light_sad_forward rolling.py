
import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Stimulus Animation - Forward Rolling")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Frame rate
FPS = 60

# Clock for smooth animation
clock = pygame.time.Clock()

# Sadman point-light positions relative to a rolling circle
# These positions represent biomechanically plausible joints of the human figure.
POINT_LIGHTS = [
    (-50, -100), (-25, -80), (-70, -60), (0, -40), (-90, 0),
    (-80, 30), (-50, 50), (-70, 80), (-30, 100), (-10, 120),
    (30, -20), (50, 0), (70, 20), (100, 50), (80, 80)
]

# Circle rolling parameters
CIRCLE_RADIUS = 100
ROLLING_SPEED = 2 * math.pi / 180  # Angular velocity (radians per frame)
ANGLE_OFFSET = 0

def draw_sadman(anchor_x, anchor_y, angle):
    """
    Draw the sadman's point-lights rolling forward.
    :param anchor_x: x-coordinate of the rolling circle's center
    :param anchor_y: y-coordinate of the rolling circle's center
    :param angle: current rotation angle of the rolling circle
    """
    for point in POINT_LIGHTS:
        # Calculate the new positions of each point-light based on the rolling angle
        shifted_x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
        shifted_y = point[0] * math.sin(angle) + point[1] * math.cos(angle)

        # Adjust the position relative to the circle's anchor (center) and draw the point-light
        pygame.draw.circle(screen, WHITE, (int(anchor_x + shifted_x), int(anchor_y + shifted_y)), 4)

# Main loop
def main():
    global ANGLE_OFFSET

    running = True
    while running:
        screen.fill(BLACK)  # Set background color
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit on window close
                running = False

        # Anchor point for the rolling sadman (circle)
        circle_x = (WIDTH // 2) - 200 + (ANGLE_OFFSET * 150)
        circle_y = HEIGHT // 2

        # Draw the sadman moving forward
        draw_sadman(circle_x, circle_y, ANGLE_OFFSET)

        # Update rotation angle for motion
        ANGLE_OFFSET += ROLLING_SPEED
        if ANGLE_OFFSET > 2 * math.pi:
            ANGLE_OFFSET -= 2 * math.pi

        # Update display
        pygame.display.flip()

        # Cap at 60 FPS
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
