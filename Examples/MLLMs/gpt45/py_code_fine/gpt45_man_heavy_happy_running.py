
import pygame
import sys
import numpy as np

pygame.init()

# Screen setup
width, height = 560, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Biological Motion Animation")

clock = pygame.time.Clock()

# Defining colors
white = (255, 255, 255)
black = (0, 0, 0)

# Running animation parameters for "a happy man running with heavy weight"
t = np.linspace(0, 2 * np.pi, 100)
speed = 0.04

# Helper function to calculate positions
def runner_motion(t):
    xpos = width // 2 + 80 * np.sin(t * 2)
    ypos = height // 2 + 50 * np.sin(t * 4)

    # 15 points: [head, shoulders(2), elbows(2), hands(2), hips(2), knees(2), ankles(2), feet(2)]
    points = np.zeros((15, 2))

    # Head position
    points[0] = [xpos, ypos - 120]

    # Shoulders positions
    points[1] = [xpos - 30, ypos - 90]
    points[2] = [xpos + 30, ypos - 90]

    # Elbows positions
    points[3] = [xpos - 50 + 20 * np.sin(t*2), ypos - 50]
    points[4] = [xpos + 50 + 20 * np.cos(t*2), ypos - 50]

    # Hands positions
    points[5] = [xpos - 70 + 30 * np.sin(t*2), ypos - 10]
    points[6] = [xpos + 70 + 30 * np.cos(t*2), ypos - 10]

    # Hips positions
    points[7] = [xpos - 15, ypos - 10]
    points[8] = [xpos + 15, ypos - 10]

    # Knees positions
    points[9] = [xpos - 30 + 20 * np.cos(t*2), ypos + 50 + 20 * np.sin(t*2)]
    points[10] = [xpos + 30 + 20 * np.cos(t*2+np.pi), ypos + 50 + 20 * np.sin(t*2 + np.pi)]

    # Ankles positions (heavier weight induces smaller oscillations)
    points[11] = [xpos - 40 + 10 * np.cos(t*2), ypos + 100 + 10 * np.sin(t*2)]
    points[12] = [xpos + 40 + 10 * np.cos(t*2+np.pi), ypos + 100 + 10 * np.sin(t*2 + np.pi)]

    # Feet positions
    points[13] = [points[11][0] - 10 * np.sin(t*2), points[11][1] + 10]
    points[14] = [points[12][0] - 10 * np.sin(t*2+np.pi), points[12][1] + 10]

    return points

running = True
frame = 0

# Animation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    points = runner_motion(t[frame % len(t)])

    # Draw points
    for p in points:
        pygame.draw.circle(screen, white, (int(p[0]), int(p[1])), 6)

    pygame.display.flip()
    frame += 1
    clock.tick(30)

pygame.quit()
sys.exit()
