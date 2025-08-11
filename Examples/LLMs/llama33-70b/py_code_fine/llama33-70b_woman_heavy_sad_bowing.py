
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions and velocities for a sad woman bowing
# The points are arranged to represent the major joints of the body
points = [
    {"x": WIDTH / 2, "y": HEIGHT / 2 - 100, "vx": 0, "vy": 0},  # Head
    {"x": WIDTH / 2 - 20, "y": HEIGHT / 2 - 80, "vx": 0, "vy": 0},  # Left shoulder
    {"x": WIDTH / 2 + 20, "y": HEIGHT / 2 - 80, "vx": 0, "vy": 0},  # Right shoulder
    {"x": WIDTH / 2 - 40, "y": HEIGHT / 2 - 40, "vx": 0, "vy": 0},  # Left elbow
    {"x": WIDTH / 2 + 40, "y": HEIGHT / 2 - 40, "vx": 0, "vy": 0},  # Right elbow
    {"x": WIDTH / 2 - 60, "y": HEIGHT / 2 + 20, "vx": 0, "vy": 0},  # Left wrist
    {"x": WIDTH / 2 + 60, "y": HEIGHT / 2 + 20, "vx": 0, "vy": 0},  # Right wrist
    {"x": WIDTH / 2, "y": HEIGHT / 2 + 60, "vx": 0, "vy": 0},  # Spine
    {"x": WIDTH / 2 - 20, "y": HEIGHT / 2 + 100, "vx": 0, "vy": 0},  # Left hip
    {"x": WIDTH / 2 + 20, "y": HEIGHT / 2 + 100, "vx": 0, "vy": 0},  # Right hip
    {"x": WIDTH / 2 - 40, "y": HEIGHT / 2 + 140, "vx": 0, "vy": 0},  # Left knee
    {"x": WIDTH / 2 + 40, "y": HEIGHT / 2 + 140, "vx": 0, "vy": 0},  # Right knee
    {"x": WIDTH / 2 - 60, "y": HEIGHT / 2 + 180, "vx": 0, "vy": 0},  # Left ankle
    {"x": WIDTH / 2 + 60, "y": HEIGHT / 2 + 180, "vx": 0, "vy": 0},  # Right ankle
    {"x": WIDTH / 2, "y": HEIGHT / 2 + 220, "vx": 0, "vy": 0}  # Heavy weight
]

# Animation parameters
bowing_angle = 0
bowing_speed = 0.05

def update_points():
    global bowing_angle
    global points

    # Update head position
    points[0]["x"] = WIDTH / 2
    points[0]["y"] = HEIGHT / 2 - 100 + 50 * math.sin(bowing_angle)

    # Update shoulder positions
    points[1]["x"] = WIDTH / 2 - 20 + 10 * math.cos(bowing_angle)
    points[1]["y"] = HEIGHT / 2 - 80 + 20 * math.sin(bowing_angle)
    points[2]["x"] = WIDTH / 2 + 20 - 10 * math.cos(bowing_angle)
    points[2]["y"] = HEIGHT / 2 - 80 + 20 * math.sin(bowing_angle)

    # Update elbow positions
    points[3]["x"] = WIDTH / 2 - 40 + 20 * math.cos(bowing_angle)
    points[3]["y"] = HEIGHT / 2 - 40 + 30 * math.sin(bowing_angle)
    points[4]["x"] = WIDTH / 2 + 40 - 20 * math.cos(bowing_angle)
    points[4]["y"] = HEIGHT / 2 - 40 + 30 * math.sin(bowing_angle)

    # Update wrist positions
    points[5]["x"] = WIDTH / 2 - 60 + 30 * math.cos(bowing_angle)
    points[5]["y"] = HEIGHT / 2 + 20 + 40 * math.sin(bowing_angle)
    points[6]["x"] = WIDTH / 2 + 60 - 30 * math.cos(bowing_angle)
    points[6]["y"] = HEIGHT / 2 + 20 + 40 * math.sin(bowing_angle)

    # Update spine position
    points[7]["x"] = WIDTH / 2
    points[7]["y"] = HEIGHT / 2 + 60 + 50 * math.sin(bowing_angle)

    # Update hip positions
    points[8]["x"] = WIDTH / 2 - 20 + 10 * math.cos(bowing_angle)
    points[8]["y"] = HEIGHT / 2 + 100 + 20 * math.sin(bowing_angle)
    points[9]["x"] = WIDTH / 2 + 20 - 10 * math.cos(bowing_angle)
    points[9]["y"] = HEIGHT / 2 + 100 + 20 * math.sin(bowing_angle)

    # Update knee positions
    points[10]["x"] = WIDTH / 2 - 40 + 20 * math.cos(bowing_angle)
    points[10]["y"] = HEIGHT / 2 + 140 + 30 * math.sin(bowing_angle)
    points[11]["x"] = WIDTH / 2 + 40 - 20 * math.cos(bowing_angle)
    points[11]["y"] = HEIGHT / 2 + 140 + 30 * math.sin(bowing_angle)

    # Update ankle positions
    points[12]["x"] = WIDTH / 2 - 60 + 30 * math.cos(bowing_angle)
    points[12]["y"] = HEIGHT / 2 + 180 + 40 * math.sin(bowing_angle)
    points[13]["x"] = WIDTH / 2 + 60 - 30 * math.cos(bowing_angle)
    points[13]["y"] = HEIGHT / 2 + 180 + 40 * math.sin(bowing_angle)

    # Update heavy weight position
    points[14]["x"] = WIDTH / 2
    points[14]["y"] = HEIGHT / 2 + 220 + 50 * math.sin(bowing_angle)

    # Update bowing angle
    bowing_angle += bowing_speed

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        update_points()

        for point in points:
            pygame.draw.circle(screen, (255, 255, 255), (int(point["x"]), int(point["y"])), 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
