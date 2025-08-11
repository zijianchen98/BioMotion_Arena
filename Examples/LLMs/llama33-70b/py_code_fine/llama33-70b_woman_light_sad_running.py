
import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Point-light positions for a running woman
point_lights = [
    {"x": 0.5, "y": 0.8, "dx": 0, "dy": -0.01},  # Head
    {"x": 0.4, "y": 0.7, "dx": 0.01, "dy": -0.02},  # Left shoulder
    {"x": 0.6, "y": 0.7, "dx": -0.01, "dy": -0.02},  # Right shoulder
    {"x": 0.3, "y": 0.6, "dx": 0.02, "dy": -0.01},  # Left elbow
    {"x": 0.7, "y": 0.6, "dx": -0.02, "dy": -0.01},  # Right elbow
    {"x": 0.2, "y": 0.5, "dx": 0.03, "dy": 0},  # Left wrist
    {"x": 0.8, "y": 0.5, "dx": -0.03, "dy": 0},  # Right wrist
    {"x": 0.5, "y": 0.4, "dx": 0, "dy": 0.01},  # Hips
    {"x": 0.4, "y": 0.3, "dx": 0.01, "dy": 0.02},  # Left knee
    {"x": 0.6, "y": 0.3, "dx": -0.01, "dy": 0.02},  # Right knee
    {"x": 0.3, "y": 0.2, "dx": 0.02, "dy": 0.01},  # Left ankle
    {"x": 0.7, "y": 0.2, "dx": -0.02, "dy": 0.01},  # Right ankle
    {"x": 0.2, "y": 0.1, "dx": 0.03, "dy": 0},  # Left toe
    {"x": 0.8, "y": 0.1, "dx": -0.03, "dy": 0},  # Right toe
    {"x": 0.5, "y": 0.9, "dx": 0, "dy": -0.01}  # Sad face indicator (above head)
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        for point_light in point_lights:
            x = int(point_light["x"] * WIDTH + point_light["dx"] * WIDTH)
            y = int(point_light["y"] * HEIGHT + point_light["dy"] * HEIGHT)

            # Update point-light position
            point_light["x"] += point_light["dx"]
            point_light["y"] += point_light["dy"]

            # Boundary checking to keep the point-lights within the screen
            if x < 0 or x > WIDTH:
                point_light["dx"] *= -1
            if y < 0 or y > HEIGHT:
                point_light["dy"] *= -1

            pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)  # Draw the point-light

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
