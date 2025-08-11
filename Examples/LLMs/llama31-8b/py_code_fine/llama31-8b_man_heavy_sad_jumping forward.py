
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Sadman:
    def __init__(self):
        self.body_parts = {
            'head': {'x': WIDTH // 2, 'y': HEIGHT // 2 - 50},
            'left_shoulder': {'x': WIDTH // 2 - 50, 'y': HEIGHT // 2 - 100},
            'left_elbow': {'x': WIDTH // 2 - 100, 'y': HEIGHT // 2 - 150},
            'left_wrist': {'x': WIDTH // 2 - 150, 'y': HEIGHT // 2 - 200},
            'left_hip': {'x': WIDTH // 2 - 50, 'y': HEIGHT // 2},
            'left_knee': {'x': WIDTH // 2 - 100, 'y': HEIGHT // 2 + 50},
            'left_ankle': {'x': WIDTH // 2 - 150, 'y': HEIGHT // 2 + 100},
            'right_shoulder': {'x': WIDTH // 2 + 50, 'y': HEIGHT // 2 - 100},
            'right_elbow': {'x': WIDTH // 2 + 100, 'y': HEIGHT // 2 - 150},
            'right_wrist': {'x': WIDTH // 2 + 150, 'y': HEIGHT // 2 - 200},
            'right_hip': {'x': WIDTH // 2 + 50, 'y': HEIGHT // 2},
            'right_knee': {'x': WIDTH // 2 + 100, 'y': HEIGHT // 2 + 50},
            'right_ankle': {'x': WIDTH // 2 + 150, 'y': HEIGHT // 2 + 100},
        }

        self.jump_velocity = 5
        self.time = 0

    def update(self):
        self.time += 1

        # Jumping motion
        if self.time < 30:
            self.body_parts['head']['y'] -= self.jump_velocity
            self.body_parts['left_shoulder']['y'] -= self.jump_velocity
            self.body_parts['left_elbow']['y'] -= self.jump_velocity
            self.body_parts['left_wrist']['y'] -= self.jump_velocity
            self.body_parts['left_hip']['y'] -= self.jump_velocity
            self.body_parts['left_knee']['y'] -= self.jump_velocity
            self.body_parts['left_ankle']['y'] -= self.jump_velocity
            self.body_parts['right_shoulder']['y'] -= self.jump_velocity
            self.body_parts['right_elbow']['y'] -= self.jump_velocity
            self.body_parts['right_wrist']['y'] -= self.jump_velocity
            self.body_parts['right_hip']['y'] -= self.jump_velocity
            self.body_parts['right_knee']['y'] -= self.jump_velocity
            self.body_parts['right_ankle']['y'] -= self.jump_velocity

        # Landing motion
        elif self.time < 60:
            self.body_parts['head']['y'] += self.jump_velocity
            self.body_parts['left_shoulder']['y'] += self.jump_velocity
            self.body_parts['left_elbow']['y'] += self.jump_velocity
            self.body_parts['left_wrist']['y'] += self.jump_velocity
            self.body_parts['left_hip']['y'] += self.jump_velocity
            self.body_parts['left_knee']['y'] += self.jump_velocity
            self.body_parts['left_ankle']['y'] += self.jump_velocity
            self.body_parts['right_shoulder']['y'] += self.jump_velocity
            self.body_parts['right_elbow']['y'] += self.jump_velocity
            self.body_parts['right_wrist']['y'] += self.jump_velocity
            self.body_parts['right_hip']['y'] += self.jump_velocity
            self.body_parts['right_knee']['y'] += self.jump_velocity
            self.body_parts['right_ankle']['y'] += self.jump_velocity

    def draw(self, screen):
        for i, (part, pos) in enumerate(self.body_parts.items()):
            if i % 2 == 0:
                pygame.draw.circle(screen, WHITE, (pos['x'], pos['y']), 5)
            else:
                pygame.draw.circle(screen, WHITE, (pos['x'], pos['y']), 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    sadman = Sadman()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        sadman.update()
        sadman.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
