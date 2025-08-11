
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Walker")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Walker:
    def __init__(self):
        self.time = 0.0
        self.speed = 0.1  # Animation speed control

    def update(self):
        self.time += self.speed

    def get_points(self):
        points = []
        center_x, center_y = width//2, height//2

        # Body parameters
        body_bounce = 8 * math.cos(2 * self.time)
        leg_swing = 35 * math.sin(self.time)
        arm_swing = 30 * math.sin(self.time + math.pi)  # Opposite phase to legs

        # Head
        points.append((center_x, center_y - 60 + body_bounce))

        # Shoulders
        points.append((center_x - 40 + arm_swing, center_y - 30 + body_bounce))
        points.append((center_x + 40 - arm_swing, center_y - 30 + body_bounce))

        # Elbows
        points.append((center_x - 60 + arm_swing*1.2, center_y + 10 + body_bounce))
        points.append((center_x + 60 - arm_swing*1.2, center_y + 10 + body_bounce))

        # Hands
        points.append((center_x - 75 + arm_swing*1.5, center_y + 40 + body_bounce))
        points.append((center_x + 75 - arm_swing*1.5, center_y + 40 + body_bounce))

        # Hips
        points.append((center_x - 25 + leg_swing*0.7, center_y + 30 + body_bounce))
        points.append((center_x + 25 - leg_swing*0.7, center_y + 30 + body_bounce))

        # Knees
        points.append((center_x - 30 + leg_swing, center_y + 80 + body_bounce))
        points.append((center_x + 30 - leg_swing, center_y + 80 + body_bounce))

        # Ankles
        points.append((center_x - 45 + leg_swing*1.2, center_y + 130 + body_bounce))
        points.append((center_x + 45 - leg_swing*1.2, center_y + 130 + body_bounce))

        # Feet
        points.append((center_x - 50 + leg_swing*1.5, center_y + 160 + body_bounce))
        points.append((center_x + 50 - leg_swing*1.5, center_y + 160 + body_bounce))

        return points

# Create walker instance
walker = Walker()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    walker.update()
    points = walker.get_points()

    # Draw all points
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 6)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
