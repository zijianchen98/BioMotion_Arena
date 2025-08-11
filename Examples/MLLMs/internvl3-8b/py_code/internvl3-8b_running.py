
import pygame
import math

def draw_point_light(screen, position):
    pygame.draw.circle(screen, (255, 255, 255), position, 10)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    positions = [(400, 300)]  # Starting position of the man in the center

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for pos in positions:
            draw_point_light(screen, pos)

        positions[0] = move_man(positions[0])
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def move_man(position):
    # Implement a simple biomechanically plausible movement
    angle = 0
    radius = 50
    x = position[0] + radius * math.cos(math.radians(angle))
    y = position[1] + radius * math.sin(math.radians(angle))
    return (x, y)

if __name__ == "__main__":
    main()
