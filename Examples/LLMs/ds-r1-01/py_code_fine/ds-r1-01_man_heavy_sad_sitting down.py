
import pygame
import sys

pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Sitting Down")
clock = pygame.time.Clock()

# Define points with start (standing) and end (sitting) positions
points = [
    # Head (1)
    {'start': (400, 100), 'end': (400, 200)},
    # Left shoulder (2)
    {'start': (350, 150), 'end': (340, 250)},
    # Right shoulder (3)
    {'start': (450, 150), 'end': (460, 250)},
    # Left elbow (4)
    {'start': (330, 200), 'end': (280, 300)},
    # Right elbow (5)
    {'start': (470, 200), 'end': (520, 300)},
    # Left wrist (6)
    {'start': (310, 250), 'end': (220, 350)},
    # Right wrist (7)
    {'start': (490, 250), 'end': (580, 350)},
    # Left hip (8)
    {'start': (350, 300), 'end': (340, 400)},
    # Right hip (9)
    {'start': (450, 300), 'end': (460, 400)},
    # Left knee (10)
    {'start': (350, 400), 'end': (340, 450)},
    # Right knee (11)
    {'start': (450, 400), 'end': (460, 450)},
    # Left ankle (12)
    {'start': (350, 500), 'end': (300, 500)},
    # Right ankle (13)
    {'start': (450, 500), 'end': (500, 500)},
    # Left foot (14)
    {'start': (350, 550), 'end': (300, 550)},
    # Right foot (15)
    {'start': (450, 550), 'end': (500, 550)},
]

def ease_in_out(t):
    """Easing function for smooth start and end"""
    return t * t * (3 - 2 * t)

# Animation control
animation_time = 2  # seconds
total_frames = animation_time * 60  # 60 FPS
current_frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate normalized time [0, 1]
    t = current_frame / total_frames
    eased_t = ease_in_out(t)
    
    # Reset animation
    if current_frame >= total_frames:
        current_frame = 0
    else:
        current_frame += 1

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw all points
    for point in points:
        # Interpolate positions
        x = point['start'][0] + (point['end'][0] - point['start'][0]) * eased_t
        y = point['start'][1] + (point['end'][1] - point['start'][1]) * eased_t
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
