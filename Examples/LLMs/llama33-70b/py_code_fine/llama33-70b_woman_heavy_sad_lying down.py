
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light properties
NUM_LIGHTS = 15
LIGHT_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Woman's joints and their initial positions
JOINTS = {
    'head': (WIDTH / 2, HEIGHT / 2 - 100),
    'neck': (WIDTH / 2, HEIGHT / 2 - 50),
    'left_shoulder': (WIDTH / 2 - 50, HEIGHT / 2),
    'left_elbow': (WIDTH / 2 - 100, HEIGHT / 2 + 50),
    'left_hand': (WIDTH / 2 - 150, HEIGHT / 2 + 100),
    'right_shoulder': (WIDTH / 2 + 50, HEIGHT / 2),
    'right_elbow': (WIDTH / 2 + 100, HEIGHT / 2 + 50),
    'right_hand': (WIDTH / 2 + 150, HEIGHT / 2 + 100),
    'left_hip': (WIDTH / 2 - 50, HEIGHT / 2 + 150),
    'left_knee': (WIDTH / 2 - 50, HEIGHT / 2 + 250),
    'left_foot': (WIDTH / 2 - 50, HEIGHT / 2 + 350),
    'right_hip': (WIDTH / 2 + 50, HEIGHT / 2 + 150),
    'right_knee': (WIDTH / 2 + 50, HEIGHT / 2 + 250),
    'right_foot': (WIDTH / 2 + 50, HEIGHT / 2 + 350),
}

# Animation parameters
ANIMATION_SPEED = 0.05

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, joint_name, angle, distance):
        self.x = JOINTS[joint_name][0] + distance * math.cos(angle)
        self.y = JOINTS[joint_name][1] + distance * math.sin(angle)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    point_lights = [
        PointLight(JOINTS['head'][0], JOINTS['head'][1]),
        PointLight(JOINTS['neck'][0], JOINTS['neck'][1]),
        PointLight(JOINTS['left_shoulder'][0], JOINTS['left_shoulder'][1]),
        PointLight(JOINTS['left_elbow'][0], JOINTS['left_elbow'][1]),
        PointLight(JOINTS['left_hand'][0], JOINTS['left_hand'][1]),
        PointLight(JOINTS['right_shoulder'][0], JOINTS['right_shoulder'][1]),
        PointLight(JOINTS['right_elbow'][0], JOINTS['right_elbow'][1]),
        PointLight(JOINTS['right_hand'][0], JOINTS['right_hand'][1]),
        PointLight(JOINTS['left_hip'][0], JOINTS['left_hip'][1]),
        PointLight(JOINTS['left_knee'][0], JOINTS['left_knee'][1]),
        PointLight(JOINTS['left_foot'][0], JOINTS['left_foot'][1]),
        PointLight(JOINTS['right_hip'][0], JOINTS['right_hip'][1]),
        PointLight(JOINTS['right_knee'][0], JOINTS['right_knee'][1]),
        PointLight(JOINTS['right_foot'][0], JOINTS['right_foot'][1]),
        PointLight(WIDTH / 2, HEIGHT / 2 + 200),  # Additional point-light for the weight
    ]

    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        # Update point-lights
        point_lights[0].update('head', angle, 0)
        point_lights[1].update('neck', angle, 0)
        point_lights[2].update('left_shoulder', angle, 0)
        point_lights[3].update('left_elbow', angle + math.pi / 2, 50)
        point_lights[4].update('left_hand', angle + math.pi / 2, 100)
        point_lights[5].update('right_shoulder', angle, 0)
        point_lights[6].update('right_elbow', angle - math.pi / 2, 50)
        point_lights[7].update('right_hand', angle - math.pi / 2, 100)
        point_lights[8].update('left_hip', angle, 0)
        point_lights[9].update('left_knee', angle + math.pi / 2, 100)
        point_lights[10].update('left_foot', angle + math.pi / 2, 150)
        point_lights[11].update('right_hip', angle, 0)
        point_lights[12].update('right_knee', angle - math.pi / 2, 100)
        point_lights[13].update('right_foot', angle - math.pi / 2, 150)
        point_lights[14].update('left_hip', angle, 50)  # Weight

        # Draw point-lights
        for point_light in point_lights:
            pygame.draw.circle(screen, LIGHT_COLOR, (int(point_light.x), int(point_light.y)), 5)

        pygame.display.flip()
        clock.tick(60)

        angle += ANIMATION_SPEED

    pygame.quit()

if __name__ == "__main__":
    main()
