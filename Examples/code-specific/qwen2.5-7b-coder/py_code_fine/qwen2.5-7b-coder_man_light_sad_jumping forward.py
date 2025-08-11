
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sadman Jumping Forward")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Point-light properties
NUM_LIGHTS = 15
lights = []
for _ in range(NUM_LIGHTS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    lights.append([x, y])

# Gravity and jump parameters
gravity = 0.5
jump_strength = -15
velocity = [0, 0]
is_jumping = False

# Clock
clock = pygame.time.Clock()

def draw_lights():
    for light in lights:
        pygame.draw.circle(screen, WHITE, light, 5)

def update_lights():
    global velocity, is_jumping
    if not is_jumping:
        velocity[1] += gravity
        for i in range(len(lights)):
            lights[i][1] += velocity[1]
            if lights[i][1] > HEIGHT:
                lights[i][1] = 0
                lights[i][0] = random.randint(0, WIDTH)
    else:
        for i in range(len(lights)):
            lights[i][1] += velocity[1]
            if lights[i][1] <= 0:
                is_jumping = False
                velocity[1] = 0

def main():
    global is_jumping
    running = True
    while running:
        screen.fill(BLACK)
        draw_lights()
        update_lights()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    velocity[1] = jump_strength

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
