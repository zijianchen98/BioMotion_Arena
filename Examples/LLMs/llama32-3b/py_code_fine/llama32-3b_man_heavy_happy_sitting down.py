
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
JOINTS = 15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class PointLight:
    def __init__(self, x, y, angle, size, weight):
        self.x = x
        self.y = y
        self.angle = angle
        self.size = size
        self.weight = weight

    def update(self):
        self.angle += 0.01

    def draw(self):
        # Calculate the position of the light
        px = self.x + self.size * math.cos(self.angle)
        py = self.y + self.size * math.sin(self.angle)

        # Draw the light
        pygame.draw.circle(screen, WHITE, (int(px), int(py)), 2)

        # Draw the weight
        weight_x = self.x + self.size * math.cos(self.angle + math.pi / 4)
        weight_y = self.y + self.size * math.sin(self.angle + math.pi / 4)
        pygame.draw.circle(screen, WHITE, (int(weight_x), int(weight_y)), 5)

def main():
    clock = pygame.time.Clock()
    running = True

    # Set up the joints
    joints = [
        PointLight(200, 200, 0, 20, 1),  # Head
        PointLight(200, 250, 0, 20, 1),  # Neck
        PointLight(200, 300, 0, 20, 1),  # Torso
        PointLight(200, 350, 0, 20, 1),  # Left Arm
        PointLight(200, 400, 0, 20, 1),  # Left Hand
        PointLight(200, 450, 0, 20, 1),  # Right Arm
        PointLight(200, 500, 0, 20, 1),  # Right Hand
        PointLight(200, 550, 0, 20, 1),  # Left Leg
        PointLight(200, 600, 0, 20, 1),  # Left Foot
        PointLight(200, 650, 0, 20, 1),  # Right Leg
        PointLight(200, 700, 0, 20, 1),  # Right Foot
        PointLight(200, 750, 0, 20, 1),  # Spine
        PointLight(200, 800, 0, 20, 1),  # Hip
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Update and draw the joints
        for joint in joints:
            joint.update()
            joint.draw()

        # Draw the body
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 50, 2)

        # Draw the weight
        weight_x = WIDTH // 2 + 20 * math.cos(joints[JOINTS - 1].angle + math.pi / 4)
        weight_y = HEIGHT // 2 + 20 * math.sin(joints[JOINTS - 1].angle + math.pi / 4)
        pygame.draw.circle(screen, WHITE, (int(weight_x), int(weight_y)), 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
