
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Bowing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 60
PERIOD = 2.5  # Animation cycle duration in seconds

class PointLight:
    def __init__(self, base_x, base_y, amp_x, amp_y, phase=0, freq=1.0):
        self.base_x = base_x
        self.base_y = base_y
        self.amp_x = amp_x
        self.amp_y = amp_y
        self.phase = phase
        self.freq = freq

    def update_position(self, time):
        theta = 2 * math.pi * (time / PERIOD) * self.freq + self.phase
        self.x = self.base_x + self.amp_x * math.sin(theta)
        self.y = self.base_y + self.amp_y * math.sin(theta)

def create_points():
    center_x, center_y = WIDTH//2, HEIGHT//2
    points = [
        # Head (large vertical movement)
        PointLight(center_x, center_y-120, 15, 50),
        # Shoulders
        PointLight(center_x-35, center_y-80, 12, 40),
        PointLight(center_x+35, center_y-80, 12, 40),
        # Elbows (opposite phase for arm swing)
        PointLight(center_x-60, center_y-50, -25, 30, phase=math.pi),
        PointLight(center_x+60, center_y-50, -25, 30, phase=math.pi),
        # Hands
        PointLight(center_x-80, center_y-20, -40, 40, phase=math.pi),
        PointLight(center_x+80, center_y-20, -40, 40, phase=math.pi),
        # Torso points
        PointLight(center_x, center_y-60, 10, 30),
        PointLight(center_x, center_y-30, 8, 25),
        PointLight(center_x, center_y, 5, 15),
        # Hips
        PointLight(center_x-20, center_y+20, 5, 5),
        PointLight(center_x+20, center_y+20, 5, 5),
        # Knees
        PointLight(center_x-25, center_y+60, 0, 10),
        PointLight(center_x+25, center_y+60, 0, 10),
        # Ankles
        PointLight(center_x-25, center_y+100, 0, 5)
    ]
    return points

def main():
    clock = pygame.time.Clock()
    points = create_points()
    start_time = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate elapsed time
        current_time = (pygame.time.get_ticks() - start_time) / 1000
        current_time %= PERIOD  # Loop animation

        # Update points
        for point in points:
            point.update_position(current_time)

        # Draw
        screen.fill(BLACK)
        for point in points:
            pygame.draw.circle(screen, WHITE, (int(point.x), int(point.y)), 5)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
