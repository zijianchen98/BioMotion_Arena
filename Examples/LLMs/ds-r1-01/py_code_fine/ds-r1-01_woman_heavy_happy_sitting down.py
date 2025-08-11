
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define point-light positions (start and end for sitting motion)
points = [
    # Head
    {'start': (400, 100), 'end': (400, 150)},
    # Neck
    {'start': (400, 130), 'end': (400, 180)},
    # Left shoulder
    {'start': (350, 150), 'end': (350, 200)},
    # Right shoulder
    {'start': (450, 150), 'end': (450, 200)},
    # Left elbow
    {'start': (320, 200), 'end': (300, 250)},
    # Right elbow
    {'start': (480, 200), 'end': (500, 250)},
    # Left hand
    {'start': (300, 250), 'end': (280, 300)},
    # Right hand
    {'start': (500, 250), 'end': (520, 300)},
    # Torso
    {'start': (400, 200), 'end': (400, 300)},
    # Left hip
    {'start': (375, 250), 'end': (375, 400)},
    # Right hip
    {'start': (425, 250), 'end': (425, 400)},
    # Left knee
    {'start': (375, 350), 'end': (350, 400)},
    # Right knee
    {'start': (425, 350), 'end': (450, 400)},
    # Left ankle
    {'start': (375, 450), 'end': (350, 450)},
    # Right ankle
    {'start': (425, 450), 'end': (450, 450)},
]

def ease(t):
    """Easing function for smooth movement"""
    return t * t * (3 - 2 * t)

# Animation parameters
duration = 2000  # 2 seconds
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized time
    current_time = pygame.time.get_ticks() - start_time
    t = current_time / duration
    if t >= 1:
        start_time = pygame.time.get_ticks()  # Reset for looping
        t = 0
    eased_t = ease(t)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw points
    for point in points:
        sx, sy = point['start']
        ex, ey = point['end']
        x = sx + (ex - sx) * eased_t
        y = sy + (ey - sy) * eased_t
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

pygame.quit()
sys.exit()
