
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Running")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Animation parameters
FPS = 30
clock = pygame.time.Clock()
time = 0
speed = 0.1  # Overall animation speed

# Body parameters
torso_y = height//2
amplitude = 30  # Vertical bounce amplitude
stride_length = 60  # Horizontal leg swing
arm_swing = 50  # Arm movement range

# Define 15 points with parametric motion functions
points = [
    # Head (1)
    {'x': lambda t: width//2,
     'y': lambda t: torso_y - 80 + 10*math.sin(t*2)},

    # Neck (1)
    {'x': lambda t: width//2,
     'y': lambda t: torso_y - 60},

    # Shoulders (2)
    {'x': lambda t: width//2 - 40 + 10*math.sin(t*1.5),
     'y': lambda t: torso_y - 40 + 5*math.sin(t*2)},
    {'x': lambda t: width//2 + 40 - 10*math.sin(t*1.5),
     'y': lambda t: torso_y - 40 + 5*math.sin(t*2)},

    # Elbows (2)
    {'x': lambda t: width//2 - 40 - arm_swing*math.sin(t*2),
     'y': lambda t: torso_y - 20 + 30*math.cos(t*2)},
    {'x': lambda t: width//2 + 40 + arm_swing*math.sin(t*2),
     'y': lambda t: torso_y - 20 + 30*math.cos(t*2 + math.pi)},

    # Wrists (2)
    {'x': lambda t: width//2 - 40 - arm_swing*math.sin(t*2) - 20,
     'y': lambda t: torso_y - 20 + 30*math.cos(t*2) + 15*math.sin(t*4)},
    {'x': lambda t: width//2 + 40 + arm_swing*math.sin(t*2) + 20,
     'y': lambda t: torso_y - 20 + 30*math.cos(t*2 + math.pi) + 15*math.sin(t*4)},

    # Hips (2)
    {'x': lambda t: width//2 - 25,
     'y': lambda t: torso_y + 15*math.sin(t)},
    {'x': lambda t: width//2 + 25,
     'y': lambda t: torso_y + 15*math.sin(t + math.pi)},

    # Knees (2)
    {'x': lambda t: width//2 - 25 - stride_length*math.sin(t*2),
     'y': lambda t: torso_y + 50 + amplitude*math.sin(t*2 + math.pi/2)},
    {'x': lambda t: width//2 + 25 + stride_length*math.sin(t*2),
     'y': lambda t: torso_y + 50 + amplitude*math.sin(t*2 + math.pi/2 + math.pi)},

    # Ankles (2)
    {'x': lambda t: width//2 - 25 - stride_length*math.sin(t*2) - 15*math.sin(t*4),
     'y': lambda t: torso_y + 100 + amplitude*math.sin(t*2 + math.pi/2) + 10*math.cos(t*4)},
    {'x': lambda t: width//2 + 25 + stride_length*math.sin(t*2) + 15*math.sin(t*4),
     'y': lambda t: torso_y + 100 + amplitude*math.sin(t*2 + math.pi/2 + math.pi) + 10*math.cos(t*4)},

    # Torso center (1)
    {'x': lambda t: width//2,
     'y': lambda t: torso_y + 10*math.sin(t)}
]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    time += speed

    # Draw all points
    for point in points:
        x = point['x'](time)
        y = point['y'](time)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 6)

    pygame.display.flip()
    clock.tick(FPS)
