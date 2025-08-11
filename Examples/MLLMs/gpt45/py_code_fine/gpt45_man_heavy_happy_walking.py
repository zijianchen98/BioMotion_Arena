
import pygame
import numpy as np
import sys

pygame.init()

width, height = 600, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Biological Motion Animation")

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

dots = np.array([
    [0, -250], 
    [-50, -200], [0, -200], [50, -200],
    [-75, -150], [0, -150], [75, -150], 
    [-100, -50], [-50, -50], [50, -50], [100, -50],
    [-25, 50], [25, 50], 
    [-25, 150], [25, 150]
])

angles = np.zeros(len(dots))

def update_dots(frame):
    global dots, angles
    walk_cycle = np.sin(np.radians(frame))
    
    angles[7] = 30 * walk_cycle
    angles[8] = -30 * walk_cycle
    angles[9] = 30 * walk_cycle
    angles[10] = -30 * walk_cycle
    
    angles[11] = 30 * walk_cycle  
    angles[12] = -30 * walk_cycle
    angles[13] = -30 * walk_cycle 
    angles[14] = 30 * walk_cycle

    updated = dots.copy()
    updated[7] += [40*np.sin(np.radians(angles[7])), 80*np.cos(np.radians(angles[7]))]
    updated[8] += [40*np.sin(np.radians(angles[8])), 80*np.cos(np.radians(angles[8]))]
    updated[9] += [20*np.sin(np.radians(angles[9])), 80*np.cos(np.radians(angles[9]))]
    updated[10] += [20*np.sin(np.radians(angles[10])), 80*np.cos(np.radians(angles[10]))]

    updated[11] += [5 + 25*np.sin(np.radians(angles[11])), 50*np.cos(np.radians(angles[11]))]
    updated[12] += [-5 + 25*np.sin(np.radians(angles[12])), 50*np.cos(np.radians(angles[12]))]
    updated[13] += [10 + 25*np.sin(np.radians(angles[13])), 45*np.cos(np.radians(angles[13]))]
    updated[14] += [-10 + 25*np.sin(np.radians(angles[14])), 45*np.cos(np.radians(angles[14]))]

    updated[:,1] += 20 * np.abs(walk_cycle)

    updated[:, 0] += width//2
    updated[:, 1] += height//2

    return updated 

frame = 0
running = True

while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    updated_dots = update_dots(frame)
    
    for pos in updated_dots:
        pygame.draw.circle(screen, white, (int(pos[0]), int(pos[1])), 8)

    frame = (frame + 2) % 360
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
