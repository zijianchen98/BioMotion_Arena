
import pygame
import numpy as np
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
POINT_COUNT = 15
GRAVITY = 0.5
JUMP_STRENGTH = 10

# Point-light positions for the happy man's animation (simplified)
# The positions are based on key points for the body (head, shoulders, hips, knees, etc.)
# Adjust these values as necessary for a more realistic representation
points = np.array([
    [0, -50],  # head
    [-15, -30],  # left shoulder
    [15, -30],  # right shoulder
    [-25, 0],  # left elbow
    [25, 0],  # right elbow
    [-20, 40],  # left hip
    [20, 40],  # right hip
    [-15, 100],  # left knee
    [15, 100],  # right knee
    [0, 150],  # feet
]) * 2  # Scale up for visibility

class JumpingAnimation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Point-Light Animation')
        self.clock = pygame.time.Clock()

        self.reset()

    def reset(self):
        self.y_offset = HEIGHT // 2
        self.jump_velocity = JUMP_STRENGTH
        self.is_jumping = True

    def jump(self):
        if self.is_jumping:
            self.y_offset -= self.jump_velocity
            self.jump_velocity -= GRAVITY
            
            if self.jump_velocity <= 0 and self.y_offset >= HEIGHT // 2:
                self.is_jumping = False
                self.y_offset = HEIGHT // 2
                self.jump_velocity = JUMP_STRENGTH
            
        # Simulate falling down and continue jumping
        if not self.is_jumping:
            self.jump_velocity = JUMP_STRENGTH
            self.is_jumping = True
            self.y_offset = HEIGHT // 2  # Reset position

    def draw_points(self):
        for point in points:
            x = WIDTH // 2 + point[0]
            y = self.y_offset + point[1]
            pygame.draw.circle(self.screen, (255, 255, 255), (int(x), int(y)), 5)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.jump()
            self.draw_points()
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    app = JumpingAnimation()
    app.run()
