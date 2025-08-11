
import sys
import pygame
import random
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))
screen.fill(black)

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = white
        self.radius = 5

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]: self.y -= 5
        elif key[pygame.K_DOWN]: self.y += 5
        elif key[pygame.K_LEFT]: self.x -= 5
        elif key[pygame.K_RIGHT]: self.x += 5
    
point_lights = [PointLight(random.randint(100,700), random.randint(100,500)) for _ in range(15)]
# This will create 15 'point-lights' at random locatons on screen.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    for light in point_lights:
        light.move()
        light.draw()
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
sys.exit()
