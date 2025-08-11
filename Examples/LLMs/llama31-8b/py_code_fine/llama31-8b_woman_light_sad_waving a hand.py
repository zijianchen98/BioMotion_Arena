
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Sad woman's body points
BODY_POINTS = [
    {'x': 400, 'y': 100, 'radius': 50},  # head
    {'x': 400, 'y': 150, 'radius': 30},  # head
    {'x': 350, 'y': 200, 'radius': 20},  # left shoulder
    {'x': 450, 'y': 200, 'radius': 20},  # right shoulder
    {'x': 300, 'y': 250, 'radius': 20},  # left elbow
    {'x': 500, 'y': 250, 'radius': 20},  # right elbow
    {'x': 250, 'y': 300, 'radius': 20},  # left hand
    {'x': 550, 'y': 300, 'radius': 20},  # right hand
    {'x': 300, 'y': 350, 'radius': 20},  # left wrist
    {'x': 500, 'y': 350, 'radius': 20},  # right wrist
    {'x': 350, 'y': 400, 'radius': 20},  # left hip
    {'x': 450, 'y': 400, 'radius': 20},  # right hip
    {'x': 300, 'y': 450, 'radius': 20},  # left knee
    {'x': 500, 'y': 450, 'radius': 20},  # right knee
    {'x': 250, 'y': 500, 'radius': 20},  # left ankle
    {'x': 550, 'y': 500, 'radius': 20},  # right ankle
]

# Animation parameters
FPS = 60
DURATION = 10  # seconds

class PointLightAnimation:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.angle = 0

    def draw_body_points(self):
        for i, point in enumerate(BODY_POINTS):
            if i < 7:  # upper body
                radius = 20
            else:  # lower body
                radius = 20
            pygame.draw.circle(self.screen, WHITE, (point['x'], point['y']), radius)
            if i == 6:  # left hand
                self.draw_hand(point['x'], point['y'], -math.pi / 2 + self.angle)
            elif i == 7:  # right hand
                self.draw_hand(point['x'], point['y'], math.pi / 2 + self.angle)

    def draw_hand(self, x, y, angle):
        # draw hand bones
        bone_length = 50
        bone_radius = 5
        pygame.draw.line(self.screen, WHITE, (x, y), (x + math.cos(angle) * bone_length, y + math.sin(angle) * bone_length), bone_radius)
        pygame.draw.line(self.screen, WHITE, (x + math.cos(angle) * bone_length, y + math.sin(angle) * bone_length), (x + math.cos(angle) * bone_length + math.cos(angle + math.pi / 2) * bone_length, y + math.sin(angle) * bone_length + math.sin(angle + math.pi / 2) * bone_length), bone_radius)
        pygame.draw.line(self.screen, WHITE, (x + math.cos(angle) * bone_length, y + math.sin(angle) * bone_length), (x + math.cos(angle) * bone_length + math.cos(angle - math.pi / 2) * bone_length, y + math.sin(angle) * bone_length + math.sin(angle - math.pi / 2) * bone_length), bone_radius)

    def animate(self):
        self.screen.fill(BLACK)
        self.draw_body_points()
        pygame.display.flip()
        self.clock.tick(FPS)
        self.angle += math.pi / 180  # increment angle by 1 degree
        self.frame += 1
        if self.frame >= FPS * DURATION:
            pygame.quit()
            quit()

def main():
    pygame.init()
    animation = PointLightAnimation()
    for _ in range(DURATION * FPS):
        animation.animate()

if __name__ == "__main__":
    main()
