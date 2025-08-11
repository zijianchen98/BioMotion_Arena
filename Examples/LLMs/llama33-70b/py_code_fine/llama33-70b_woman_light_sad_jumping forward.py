
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions for a sad woman
# Each point represents a joint in the body
# The positions are based on a simplified human body model
points = [
    # Head
    {"x": 100, "y": 100, "vx": 0, "vy": 0},
    # Left shoulder
    {"x": 120, "y": 150, "vx": 0, "vy": 0},
    # Right shoulder
    {"x": 80, "y": 150, "vx": 0, "vy": 0},
    # Left elbow
    {"x": 140, "y": 200, "vx": 0, "vy": 0},
    # Right elbow
    {"x": 60, "y": 200, "vx": 0, "vy": 0},
    # Left wrist
    {"x": 160, "y": 250, "vx": 0, "vy": 0},
    # Right wrist
    {"x": 40, "y": 250, "vx": 0, "vy": 0},
    # Left hip
    {"x": 120, "y": 300, "vx": 0, "vy": 0},
    # Right hip
    {"x": 80, "y": 300, "vx": 0, "vy": 0},
    # Left knee
    {"x": 140, "y": 350, "vx": 0, "vy": 0},
    # Right knee
    {"x": 60, "y": 350, "vx": 0, "vy": 0},
    # Left ankle
    {"x": 160, "y": 400, "vx": 0, "vy": 0},
    # Right ankle
    {"x": 40, "y": 400, "vx": 0, "vy": 0},
    # Torso
    {"x": 100, "y": 250, "vx": 0, "vy": 0},
    # Pelvis
    {"x": 100, "y": 350, "vx": 0, "vy": 0},
]

def update_points(points, frame):
    # Update the position of each point based on the frame number
    # This is a simplified example and does not accurately represent human motion
    for point in points:
        # Move the point up and down to simulate jumping
        point["y"] = point["y"] + 10 * math.sin(frame / 10)
        # Move the point forward to simulate movement
        point["x"] = point["x"] + 1

def draw_points(screen, points):
    # Draw each point on the screen
    for point in points:
        pygame.draw.circle(screen, WHITE, (int(point["x"]), int(point["y"])), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    frame = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        update_points(points, frame)
        draw_points(screen, points)

        pygame.display.flip()
        frame += 1
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
