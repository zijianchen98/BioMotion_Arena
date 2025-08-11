
import pygame
import math

# Initialize pygame
pygame.init()

# Define screen dimensions and background color
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion")

clock = pygame.time.Clock()
FPS = 60

# Define point positions for "Happyman" as he rolls forward
class PointLightBody:
    def __init__(self):
        self.points = [(400, 200), # Head
                       (370, 250), (430, 250), # Shoulders
                       (370, 300), (430, 300), # Elbows
                       (350, 350), (450, 350), # Hands
                       (400, 320), # Torso
                       (380, 400), (420, 400), # Hips
                       (370, 450), (430, 450), # Knees
                       (360, 500), (440, 500)] # Feet
        self.angle = 0

    def update(self):
        # Animate forward rolling: Circular motion around the center
        center_x = SCREEN_WIDTH / 2
        center_y = SCREEN_HEIGHT / 2
        
        self.angle += 0.05  # Increment angle for smooth rotation

        # The entire shape revolves in a circle
        new_points = []
        radius = 150
        for x, y in self.points:
