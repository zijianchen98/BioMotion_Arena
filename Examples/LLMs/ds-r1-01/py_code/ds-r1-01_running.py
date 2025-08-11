
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Running")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

def calculate_positions(t):
    points = []
    torso_x = width // 2
    torso_y = height // 2 + 15 * math.sin(t * 0.05)

    # Head
    points.append((torso_x, torso_y - 50 + 5 * math.sin(t * 0.1)))

    # Shoulders
    shoulder_dx = 40 * math.sin(t * 0.2)
    points.append((torso_x - 35 - shoulder_dx, torso_y - 20))
    points.append((torso_x + 35 + shoulder_dx, torso_y - 20))

    # Elbows
    elbow_dx = 30 * math.sin(t * 0.2 + math.pi/2)
    points.append((torso_x - 60 - elbow_dx, torso_y + 15))
    points.append((torso_x + 60 + elbow_dx, torso_y + 15))

    # Hands
    hand_dx = 25 * math.sin(t * 0.2 + math.pi)
    points.append((torso_x - 75 - hand_dx, torso_y + 50))
    points.append((torso_x + 75 + hand_dx, torso_y + 50))

    # Hips
    hip_dx = 30 * math.sin(t * 0.2 + math.pi)
    points.append((torso_x - 25 - hip_dx, torso_y + 30))
    points.append((torso_x + 25 + hip_dx, torso_y + 30))

    # Knees
    knee_dx = 50 * math.sin(t * 0.2)
    knee_dy = 20 * math.sin(t * 0.3)
    points.append((torso_x - 50 - knee_dx, torso_y + 80 + knee_dy))
    points.append((torso_x + 50 + knee_dx, torso_y + 80 - knee_dy))

    # Ankles
    ankle_dx = 40 * math.sin(t * 0.2 + math.pi/2)
    points.append((torso_x - 60 - ankle_dx, torso_y + 130))
    points.append((torso_x + 60 + ankle_dx, torso_y + 130))

    # Feet
    foot_dx = 30 * math.sin(t * 0.2 + math.pi)
    points.append((torso_x - 70 - foot_dx, torso_y + 150))
    points.append((torso_x + 70 + foot_dx, torso_y + 150))

    return points

time = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    points = calculate_positions(time)

    for (x, y) in points:
        pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)
    time += 0.1

pygame.quit()
sys.exit()
