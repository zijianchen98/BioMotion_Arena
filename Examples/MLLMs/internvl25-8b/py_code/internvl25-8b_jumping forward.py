
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants for the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point Light Stimulus Animation")

# Constants for the points
num_points = 15
point_radius = 5
point_color = (255, 255, 255)

# Constants for the moving points
points = []
for _ in range(num_points):
    x = screen_width // 2
    y = screen_height * 0.8
    angle = (_ * 360 / num_points) - (math.pi / 2)  # Equally spaced points
    points.append([x + 20 * math.cos(angle), y + 10 * math.sin(angle)])

clock = pygame.time.Clock()
run = True
forward_speed = 5
backward_speed = -3

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update positions
    for i, (x, y) in enumerate(points):
        # Calculate position based on angle
        new_angle = ((i // num_points) * 360) + (i % num_points * math.pi / 2)
        points[i] = [x + forward_speed * math.cos(new_angle) * 5,
                     y + backward_speed * math.sin(new_angle) * 5]

    # Draw the points
    for x, y in points:
        pygame.draw.circle(screen, point_color, (int(x), int(y)), point_radius)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
