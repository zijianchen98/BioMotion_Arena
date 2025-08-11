
import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Man Running with Point-Lights")
clock = pygame.time.Clock()

# Define a simple biomechanical model for a running man
class Runner:
    def __init__(self):
        self.body = [
            # Joints and positions (simplified)
            (400, 300),  # Hip
            (450, 250),  # Knee
            (500, 250),  # Ankle
            (425, 350),  # Shoulder
            (475, 350),  # Elbow
            (525, 350),  # Wrist
            (450, 400),  # Hip (left)
            (400, 450),  # Knee (left)
            (350, 450),  # Ankle (left)
            (425, 400),  # Shoulder (right)
            (475, 450),  # Elbow (right)
            (525, 450),  # Wrist (right)
        ]
        self.body_positions = self.body[:]
        self.speed = 5
        self.phase = 0

    def update(self):
        # Simple running motion using sine waves for joint movement
        self.phase += 0.05
        self.body_positions = [
            (400 + self.speed * math.sin(self.phase), 300),
            (450 + self.speed * math.sin(self.phase + 0.2), 250),
            (500 + self.speed * math.sin(self.phase + 0.4), 250),
            (425 + self.speed * math.sin(self.phase + 0.6), 350),
            (475 + self.speed * math.sin(self.phase + 0.8), 350),
            (525 + self.speed * math.sin(self.phase + 1.0), 350),
            (450 + self.speed * math.sin(self.phase + 1.2), 400),
            (400 + self.speed * math.sin(self.phase + 1.4), 450),
            (350 + self.speed * math.sin(self.phase + 1.6), 450),
            (425 + self.speed * math.sin(self.phase + 1.8), 400),
            (475 + self.speed * math.sin(self.phase + 2.0), 450),
            (525 + self.speed * math.sin(self.phase + 2.2), 450),
        ]

    def draw(self, screen):
        # Draw the body as lines (simplified)
        for i in range(0, len(self.body_positions), 3):
            pygame.draw.line(screen, WHITE, self.body_positions[i], self.body_positions[i+1], 2)
            pygame.draw.line(screen, WHITE, self.body_positions[i+1], self.body_positions[i+2], 2)

# Create the runner
runner = Runner()

# Create point lights (15 points)
point_lights = [pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(15)]

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Update and draw the runner
    runner.update()
    runner.draw(screen)

    # Update and draw point lights
    for light in point_lights:
        light += pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        light = pygame.Vector2(max(0, min(WIDTH, light.x)), max(0, min(HEIGHT, light.y)))
        pygame.draw.circle(screen, WHITE, (int(light.x), int(light.y)), 3)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
