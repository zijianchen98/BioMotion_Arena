
import pygame
import numpy as np
from math import sin, cos, pi

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Animation: Jumping Man")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define joint positions for a jumping man (15 points)
class PointLightMan:
    def __init__(self):
        self.points = [
            [0, 0],   # Head
            [-20, 40], # Left shoulder
            [20, 40],  # Right shoulder
            [-15, 80], # Left elbow
            [15, 80],  # Right elbow
            [-10, 120],# Left wrist
            [10, 120], # Right wrist
            [0, 150],  # Hip
            [-15, 200],# Left knee
            [15, 200], # Right knee
            [-10, 250],# Left ankle
            [10, 250], # Right ankle
            [-5, 180], # Left hip
            [5, 180],  # Right hip
            [0, 280]   # Center base
        ]
        self.phase = 0
        self.jump_height = 0

    def update(self):
        # Simulate jumping motion with a sinusoidal wave
        self.phase += 0.05
        self.jump_height = 100 * sin(self.phase) + 100
        jump_offset = min(self.jump_height, 0)  # Move down when landing

        # Biomechanically plausible movement
        for i, (x, y) in enumerate(self.points):
            if i == 0:  # Head
                y -= self.jump_height
            elif i in [1, 2]:  # Shoulders
                y -= self.jump_height * 0.8
            elif i in [3, 4]:  # Elbows
                y -= self.jump_height * 0.6
                x += 10 * sin(self.phase + pi/2)
            elif i in [5, 6]:  # Wrists
                y -= self.jump_height * 0.4
                x += 15 * sin(self.phase + pi)
            elif i == 7:  # Hip
                y -= self.jump_height * 0.9
            elif i in [8, 9]:  # Knees
                y -= self.jump_height * 0.7
                if self.jump_height > 50:
                    y += 20 * cos(self.phase)
            elif i in [10, 11]:  # Ankles
                y -= self.jump_height * 0.5
                if self.jump_height > 50:
                    y += 30 * cos(self.phase + pi/2)
            elif i in [12, 13]:  # Hips
                y -= self.jump_height * 0.9
            elif i == 14:  # Center base
                y -= self.jump_height * 0.3

            self.points[i] = [x + WIDTH/2, y + HEIGHT/2 + jump_offset]

    def draw(self, surface):
        for x, y in self.points:
            pygame.draw.circle(surface, WHITE, (int(x), int(y)), 5)

# Create man instance
man = PointLightMan()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    man.update()

    # Draw
    screen.fill(BLACK)
    man.draw(screen)
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
