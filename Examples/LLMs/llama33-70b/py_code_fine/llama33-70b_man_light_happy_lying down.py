
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities
point_lights = [
    {"x": 100, "y": 200, "vx": 0.5, "vy": -0.2},  # Head
    {"x": 120, "y": 220, "vx": 0.3, "vy": -0.1},  # Right shoulder
    {"x": 80, "y": 220, "vx": -0.3, "vy": -0.1},  # Left shoulder
    {"x": 100, "y": 250, "vx": 0.2, "vy": 0.1},  # Right elbow
    {"x": 100, "y": 250, "vx": -0.2, "vy": 0.1},  # Left elbow
    {"x": 120, "y": 280, "vx": 0.4, "vy": 0.2},  # Right hand
    {"x": 80, "y": 280, "vx": -0.4, "vy": 0.2},  # Left hand
    {"x": 100, "y": 300, "vx": 0.1, "vy": 0.3},  # Right hip
    {"x": 100, "y": 300, "vx": -0.1, "vy": 0.3},  # Left hip
    {"x": 120, "y": 330, "vx": 0.3, "vy": 0.4},  # Right knee
    {"x": 80, "y": 330, "vx": -0.3, "vy": 0.4},  # Left knee
    {"x": 120, "y": 360, "vx": 0.2, "vy": 0.5},  # Right ankle
    {"x": 80, "y": 360, "vx": -0.2, "vy": 0.5},  # Left ankle
    {"x": 100, "y": 380, "vx": 0.1, "vy": 0.6},  # Right foot
    {"x": 100, "y": 380, "vx": -0.1, "vy": 0.6},  # Left foot
]

def update_point_lights():
    for point_light in point_lights:
        point_light["x"] += point_light["vx"]
        point_light["y"] += point_light["vy"]

        # Boundary checking
        if point_light["x"] < 0 or point_light["x"] > WIDTH:
            point_light["vx"] *= -1
        if point_light["y"] < 0 or point_light["y"] > HEIGHT:
            point_light["vy"] *= -1

def draw_point_lights(screen):
    screen.fill((0, 0, 0))  # Fill background with black
    for point_light in point_lights:
        pygame.draw.circle(screen, (255, 255, 255), (int(point_light["x"]), int(point_light["y"])), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_point_lights()
        draw_point_lights(screen)

        # Simulate lying down motion
        if point_lights[0]["y"] < HEIGHT // 2:
            point_lights[0]["vy"] += 0.01
        else:
            point_lights[0]["vy"] = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
