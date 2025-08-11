
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions
point_lights = [
    {"x": 100, "y": 100, "dx": 0, "dy": 0},  # Head
    {"x": 120, "y": 150, "dx": 0, "dy": 0},  # Right shoulder
    {"x": 80, "y": 150, "dx": 0, "dy": 0},   # Left shoulder
    {"x": 120, "y": 200, "dx": 0, "dy": 0},  # Right elbow
    {"x": 80, "y": 200, "dx": 0, "dy": 0},   # Left elbow
    {"x": 120, "y": 250, "dx": 0, "dy": 0},  # Right wrist
    {"x": 80, "y": 250, "dx": 0, "dy": 0},   # Left wrist
    {"x": 100, "y": 200, "dx": 0, "dy": 0},  # Chest
    {"x": 100, "y": 250, "dx": 0, "dy": 0},  # Waist
    {"x": 120, "y": 300, "dx": 0, "dy": 0},  # Right hip
    {"x": 80, "y": 300, "dx": 0, "dy": 0},   # Left hip
    {"x": 120, "y": 350, "dx": 0, "dy": 0},  # Right knee
    {"x": 80, "y": 350, "dx": 0, "dy": 0},   # Left knee
    {"x": 120, "y": 400, "dx": 0, "dy": 0},  # Right ankle
    {"x": 80, "y": 400, "dx": 0, "dy": 0},   # Left ankle
]

def update_point_lights(point_lights, angle):
    for i, point_light in enumerate(point_lights):
        if i == 0:  # Head
            point_light["x"] = 100 + 50 * math.sin(angle)
            point_light["y"] = 100 + 50 * math.cos(angle)
        elif i == 1:  # Right shoulder
            point_light["x"] = 120 + 30 * math.sin(angle)
            point_light["y"] = 150 + 30 * math.cos(angle)
        elif i == 2:  # Left shoulder
            point_light["x"] = 80 - 30 * math.sin(angle)
            point_light["y"] = 150 + 30 * math.cos(angle)
        elif i == 3:  # Right elbow
            point_light["x"] = 120 + 50 * math.sin(angle)
            point_light["y"] = 200 + 50 * math.cos(angle)
        elif i == 4:  # Left elbow
            point_light["x"] = 80 - 50 * math.sin(angle)
            point_light["y"] = 200 + 50 * math.cos(angle)
        elif i == 5:  # Right wrist
            point_light["x"] = 120 + 70 * math.sin(angle)
            point_light["y"] = 250 + 70 * math.cos(angle)
        elif i == 6:  # Left wrist
            point_light["x"] = 80 - 70 * math.sin(angle)
            point_light["y"] = 250 + 70 * math.cos(angle)
        elif i == 7:  # Chest
            point_light["x"] = 100 + 20 * math.sin(angle)
            point_light["y"] = 200 + 20 * math.cos(angle)
        elif i == 8:  # Waist
            point_light["x"] = 100 + 30 * math.sin(angle)
            point_light["y"] = 250 + 30 * math.cos(angle)
        elif i == 9:  # Right hip
            point_light["x"] = 120 + 40 * math.sin(angle)
            point_light["y"] = 300 + 40 * math.cos(angle)
        elif i == 10:  # Left hip
            point_light["x"] = 80 - 40 * math.sin(angle)
            point_light["y"] = 300 + 40 * math.cos(angle)
        elif i == 11:  # Right knee
            point_light["x"] = 120 + 50 * math.sin(angle)
            point_light["y"] = 350 + 50 * math.cos(angle)
        elif i == 12:  # Left knee
            point_light["x"] = 80 - 50 * math.sin(angle)
            point_light["y"] = 350 + 50 * math.cos(angle)
        elif i == 13:  # Right ankle
            point_light["x"] = 120 + 60 * math.sin(angle)
            point_light["y"] = 400 + 60 * math.cos(angle)
        elif i == 14:  # Left ankle
            point_light["x"] = 80 - 60 * math.sin(angle)
            point_light["y"] = 400 + 60 * math.cos(angle)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        update_point_lights(point_lights, angle)

        for point_light in point_lights:
            pygame.draw.circle(screen, WHITE, (int(point_light["x"]), int(point_light["y"])), 5)

        angle += 0.01
        if angle > 2 * math.pi:
            angle = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
