
import pygame
import pygame.locals

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the point lights
lights = []
for i in range(15):
    light = pygame.sprite.Sprite()
    light.image = pygame.Surface((10, 10))
    light.image.fill((255, 255, 255))
    light.rect = light.image.get_rect()
    light.rect.x = i * (WIDTH // 15)
    light.rect.y = HEIGHT // 2
    lights.append(light)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            running = False

    # Update the lights
    for light in lights:
        light.rect.y -= 1
        if light.rect.y < 0:
            light.rect.y = HEIGHT

    # Draw everything
    screen.fill((0, 0, 0))
    for light in lights:
        screen.blit(light.image, light.rect)

    # Flip the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
