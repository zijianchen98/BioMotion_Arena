
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_RADIUS = 5
LIGHT_COLOR = (255, 255, 255)  # White

# Sadman's joints
JOINTS = [
    "head",
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_hand",
    "right_hand",
    "left_hip",
    "right_hip",
    "left_knee",
    "right_knee",
    "left_foot",
    "right_foot",
    "torso",
    "waist"
]

# Animation frames
FRAMES = 100

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, frame):
        # Update joint positions based on the animation frame
        if self.x == "head":
            self.x = WIDTH // 2
            self.y = HEIGHT // 2 - 100 + frame * 2
        elif self.x == "left_shoulder":
            self.x = WIDTH // 2 - 50
            self.y = HEIGHT // 2 - 50 + frame * 2
        elif self.x == "right_shoulder":
            self.x = WIDTH // 2 + 50
            self.y = HEIGHT // 2 - 50 + frame * 2
        elif self.x == "left_elbow":
            self.x = WIDTH // 2 - 100
            self.y = HEIGHT // 2 + frame * 2
        elif self.x == "right_elbow":
            self.x = WIDTH // 2 + 100
            self.y = HEIGHT // 2 + frame * 2
        elif self.x == "left_hand":
            self.x = WIDTH // 2 - 150
            self.y = HEIGHT // 2 + 50 + frame * 2
        elif self.x == "right_hand":
            self.x = WIDTH // 2 + 150
            self.y = HEIGHT // 2 + 50 + frame * 2
        elif self.x == "left_hip":
            self.x = WIDTH // 2 - 50
            self.y = HEIGHT // 2 + 100 + frame * 2
        elif self.x == "right_hip":
            self.x = WIDTH // 2 + 50
            self.y = HEIGHT // 2 + 100 + frame * 2
        elif self.x == "left_knee":
            self.x = WIDTH // 2 - 50
            self.y = HEIGHT // 2 + 150 + frame * 2
        elif self.x == "right_knee":
            self.x = WIDTH // 2 + 50
            self.y = HEIGHT // 2 + 150 + frame * 2
        elif self.x == "left_foot":
            self.x = WIDTH // 2 - 50
            self.y = HEIGHT // 2 + 200 + frame * 2
        elif self.x == "right_foot":
            self.x = WIDTH // 2 + 50
            self.y = HEIGHT // 2 + 200 + frame * 2
        elif self.x == "torso":
            self.x = WIDTH // 2
            self.y = HEIGHT // 2 + 50 + frame * 2
        elif self.x == "waist":
            self.x = WIDTH // 2
            self.y = HEIGHT // 2 + 100 + frame * 2

    def draw(self, screen):
        pygame.draw.circle(screen, LIGHT_COLOR, (self.x, self.y), LIGHT_RADIUS)

def main():
    running = True
    frame = 0
    point_lights = [
        PointLight("head", HEIGHT // 2 - 100),
        PointLight("left_shoulder", WIDTH // 2 - 50),
        PointLight("right_shoulder", WIDTH // 2 + 50),
        PointLight("left_elbow", WIDTH // 2 - 100),
        PointLight("right_elbow", WIDTH // 2 + 100),
        PointLight("left_hand", WIDTH // 2 - 150),
        PointLight("right_hand", WIDTH // 2 + 150),
        PointLight("left_hip", WIDTH // 2 - 50),
        PointLight("right_hip", WIDTH // 2 + 50),
        PointLight("left_knee", WIDTH // 2 - 50),
        PointLight("right_knee", WIDTH // 2 + 50),
        PointLight("left_foot", WIDTH // 2 - 50),
        PointLight("right_foot", WIDTH // 2 + 50),
        PointLight("torso", WIDTH // 2),
        PointLight("waist", WIDTH // 2),
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Black background

        for point_light in point_lights:
            point_light.update(frame)
            point_light.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        frame = (frame + 1) % FRAMES

    pygame.quit()

if __name__ == "__main__":
    main()
