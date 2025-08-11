
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Point-light positions for the sadman
# Each point-light represents a joint in the body
point_lights = [
    (0, -100),  # Head
    (-50, -50),  # Left shoulder
    (50, -50),   # Right shoulder
    (-100, 0),   # Left elbow
    (100, 0),    # Right elbow
    (-150, 50),  # Left wrist
    (150, 50),   # Right wrist
    (0, 100),    # Hips
    (-50, 150),  # Left knee
    (50, 150),   # Right knee
    (-100, 200), # Left ankle
    (100, 200),  # Right ankle
    (-75, 250),  # Left toe
    (75, 250),   # Right toe
    (0, 300)     # Body center
]

# Animation parameters
walking_speed = 2
stride_length = 100
leg_lift = 50

def draw_sadman(screen, x, y, phase):
    # Draw point-lights
    for i, (px, py) in enumerate(point_lights):
        # Apply walking motion
        if i in [3, 4, 7, 8, 11, 12]:  # Legs
            py += math.sin(phase + i * math.pi / 4) * leg_lift
        elif i in [5, 6, 9, 10]:  # Arms
            py += math.sin(phase + i * math.pi / 4) * leg_lift / 2
        pygame.draw.circle(screen, (255, 255, 255), (x + int(px), y + int(py)), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    x, y = WIDTH // 2, HEIGHT // 2
    phase = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Draw sadman
        draw_sadman(screen, x, y, phase)

        # Update animation
        phase += walking_speed / 100
        x -= walking_speed
        if x < -WIDTH // 2:
            x = WIDTH // 2

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
