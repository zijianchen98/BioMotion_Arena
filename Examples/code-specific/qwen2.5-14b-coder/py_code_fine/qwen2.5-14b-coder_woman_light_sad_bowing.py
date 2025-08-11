
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sad Woman Bowing Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of point lights
NUM_LIGHTS = 15

# Sad woman bowing parameters
class SadWoman:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = 0
        self.bow_angle = 0
        self.bow_speed = 0.05

    def update(self):
        # Update bow angle
        self.bow_angle += self.bow_speed
        if self.bow_angle > math.pi / 4:
            self.bow_speed = -0.05
        elif self.bow_angle < -math.pi / 4:
            self.bow_speed = 0.05

    def get_light_positions(self):
        positions = []
        # Head
        positions.append((self.x, self.y - 50))
        # Body
        positions.append((self.x, self.y))
        # Arms
        arm_length = 30
        arm_angle = math.pi / 6
        positions.append((self.x + arm_length * math.cos(arm_angle + self.bow_angle), self.y + arm_length * math.sin(arm_angle + self.bow_angle)))
        positions.append((self.x + arm_length * math.cos(-arm_angle + self.bow_angle), self.y + arm_length * math.sin(-arm_angle + self.bow_angle)))
        # Legs
        leg_length = 50
        leg_angle = math.pi / 12
        positions.append((self.x + leg_length * math.cos(leg_angle), self.y + leg_length * math.sin(leg_angle)))
        positions.append((self.x + leg_length * math.cos(-leg_angle), self.y + leg_length * math.sin(-leg_angle)))
        # Additional lights for realism
        for i in range(3):
            positions.append((self.x + (i + 1) * 10, self.y - 50 + (i + 1) * 5))
            positions.append((self.x + (i + 1) * 10, self.y + (i + 1) * 5))
        return positions

# Create sad woman instance
sad_woman = SadWoman()

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sad woman
    sad_woman.update()

    # Clear screen
    screen.fill(BLACK)

    # Draw point lights
    light_positions = sad_woman.get_light_positions()
    for pos in light_positions:
        pygame.draw.circle(screen, WHITE, pos, 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
