
import pygame
import math

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Point-light positions for a person lying down
# These positions are approximate and based on the typical joints of the human body
# The positions are defined in a way that the person is lying on their back
point_lights = [
    {'x': WIDTH / 2, 'y': HEIGHT / 2, 'dx': 0, 'dy': 0},  # Head
    {'x': WIDTH / 2, 'y': HEIGHT / 2 - 50, 'dx': 0, 'dy': 0},  # Neck
    {'x': WIDTH / 2 - 50, 'y': HEIGHT / 2 - 100, 'dx': 0, 'dy': 0},  # Left shoulder
    {'x': WIDTH / 2 + 50, 'y': HEIGHT / 2 - 100, 'dx': 0, 'dy': 0},  # Right shoulder
    {'x': WIDTH / 2 - 100, 'y': HEIGHT / 2 - 150, 'dx': 0, 'dy': 0},  # Left elbow
    {'x': WIDTH / 2 + 100, 'y': HEIGHT / 2 - 150, 'dx': 0, 'dy': 0},  # Right elbow
    {'x': WIDTH / 2 - 150, 'y': HEIGHT / 2 - 200, 'dx': 0, 'dy': 0},  # Left wrist
    {'x': WIDTH / 2 + 150, 'y': HEIGHT / 2 - 200, 'dx': 0, 'dy': 0},  # Right wrist
    {'x': WIDTH / 2, 'y': HEIGHT / 2 + 50, 'dx': 0, 'dy': 0},  # Spine
    {'x': WIDTH / 2 - 50, 'y': HEIGHT / 2 + 100, 'dx': 0, 'dy': 0},  # Left hip
    {'x': WIDTH / 2 + 50, 'y': HEIGHT / 2 + 100, 'dx': 0, 'dy': 0},  # Right hip
    {'x': WIDTH / 2 - 100, 'y': HEIGHT / 2 + 150, 'dx': 0, 'dy': 0},  # Left knee
    {'x': WIDTH / 2 + 100, 'y': HEIGHT / 2 + 150, 'dx': 0, 'dy': 0},  # Right knee
    {'x': WIDTH / 2 - 150, 'y': HEIGHT / 2 + 200, 'dx': 0, 'dy': 0},  # Left ankle
    {'x': WIDTH / 2 + 150, 'y': HEIGHT / 2 + 200, 'dx': 0, 'dy': 0}  # Right ankle
]

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move point-lights to simulate the person lying down
        # This is a simple example and does not include complex motion
        for i, point_light in enumerate(point_lights):
            if i == 0:  # Head
                point_light['x'] = WIDTH / 2 + math.sin(pygame.time.get_ticks() / 1000) * 10
                point_light['y'] = HEIGHT / 2 + math.cos(pygame.time.get_ticks() / 1000) * 10
            elif i == 1:  # Neck
                point_light['x'] = WIDTH / 2 + math.sin(pygame.time.get_ticks() / 1000) * 5
                point_light['y'] = HEIGHT / 2 - 50 + math.cos(pygame.time.get_ticks() / 1000) * 5
            elif i == 2 or i == 3:  # Shoulders
                point_light['x'] = WIDTH / 2 + (i - 2) * 50 + math.sin(pygame.time.get_ticks() / 1000) * 10
                point_light['y'] = HEIGHT / 2 - 100 + math.cos(pygame.time.get_ticks() / 1000) * 10
            elif i == 4 or i == 5:  # Elbows
                point_light['x'] = WIDTH / 2 + (i - 4) * 100 + math.sin(pygame.time.get_ticks() / 1000) * 5
                point_light['y'] = HEIGHT / 2 - 150 + math.cos(pygame.time.get_ticks() / 1000) * 5
            elif i == 6 or i == 7:  # Wrists
                point_light['x'] = WIDTH / 2 + (i - 6) * 150 + math.sin(pygame.time.get_ticks() / 1000) * 5
                point_light['y'] = HEIGHT / 2 - 200 + math.cos(pygame.time.get_ticks() / 1000) * 5
            elif i == 8:  # Spine
                point_light['x'] = WIDTH / 2 + math.sin(pygame.time.get_ticks() / 1000) * 5
                point_light['y'] = HEIGHT / 2 + 50 + math.cos(pygame.time.get_ticks() / 1000) * 5
            elif i == 9 or i == 10:  # Hips
                point_light['x'] = WIDTH / 2 + (i - 9) * 50 + math.sin(pygame.time.get_ticks() / 1000) * 10
                point_light['y'] = HEIGHT / 2 + 100 + math.cos(pygame.time.get_ticks() / 1000) * 10
            elif i == 11 or i == 12:  # Knees
                point_light['x'] = WIDTH / 2 + (i - 11) * 100 + math.sin(pygame.time.get_ticks() / 1000) * 5
                point_light['y'] = HEIGHT / 2 + 150 + math.cos(pygame.time.get_ticks() / 1000) * 5
            elif i == 13 or i == 14:  # Ankles
                point_light['x'] = WIDTH / 2 + (i - 13) * 150 + math.sin(pygame.time.get_ticks() / 1000) * 5
                point_light['y'] = HEIGHT / 2 + 200 + math.cos(pygame.time.get_ticks() / 1000) * 5

        window.fill(BLACK)
        for point_light in point_lights:
            pygame.draw.circle(window, WHITE, (int(point_light['x']), int(point_light['y'])), 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
