
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions for the sad man
# Each point-light represents a joint or a significant point on the body
point_lights = [
    {'x': WIDTH / 2, 'y': HEIGHT / 2 - 100},  # Head
    {'x': WIDTH / 2 - 20, 'y': HEIGHT / 2 - 80},  # Left shoulder
    {'x': WIDTH / 2 + 20, 'y': HEIGHT / 2 - 80},  # Right shoulder
    {'x': WIDTH / 2 - 40, 'y': HEIGHT / 2 - 40},  # Left elbow
    {'x': WIDTH / 2 + 40, 'y': HEIGHT / 2 - 40},  # Right elbow
    {'x': WIDTH / 2 - 60, 'y': HEIGHT / 2},  # Left wrist
    {'x': WIDTH / 2 + 60, 'y': HEIGHT / 2},  # Right wrist
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 20},  # Torso
    {'x': WIDTH / 2 - 20, 'y': HEIGHT / 2 + 60},  # Left hip
    {'x': WIDTH / 2 + 20, 'y': HEIGHT / 2 + 60},  # Right hip
    {'x': WIDTH / 2 - 40, 'y': HEIGHT / 2 + 100},  # Left knee
    {'x': WIDTH / 2 + 40, 'y': HEIGHT / 2 + 100},  # Right knee
    {'x': WIDTH / 2 - 60, 'y': HEIGHT / 2 + 140},  # Left ankle
    {'x': WIDTH / 2 + 60, 'y': HEIGHT / 2 + 140},  # Right ankle
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 180}  # Feet
]

# Waving hand animation parameters
waving_hand_angle = 0
waving_hand_speed = 2

def draw_point_lights(screen, point_lights):
    """Draw the point-lights on the screen."""
    for point_light in point_lights:
        pygame.draw.circle(screen, WHITE, (int(point_light['x']), int(point_light['y'])), 5)

def update_point_lights(point_lights):
    """Update the point-lights positions for the waving hand animation."""
    global waving_hand_angle
    waving_hand_angle += waving_hand_speed

    # Update the left wrist position
    point_lights[5]['x'] = WIDTH / 2 - 60 + math.sin(math.radians(waving_hand_angle)) * 20
    point_lights[5]['y'] = HEIGHT / 2 + math.sin(math.radians(waving_hand_angle)) * 10

    # Update the left elbow position
    point_lights[3]['x'] = WIDTH / 2 - 40 + math.sin(math.radians(waving_hand_angle)) * 10
    point_lights[3]['y'] = HEIGHT / 2 - 40 + math.sin(math.radians(waving_hand_angle)) * 5

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        update_point_lights(point_lights)
        draw_point_lights(screen, point_lights)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
