
import pygame
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SPEED = 2

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the square
x = WIDTH // 2
y = HEIGHT // 2
width = 50
height = 50
vel = 5

# Game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
