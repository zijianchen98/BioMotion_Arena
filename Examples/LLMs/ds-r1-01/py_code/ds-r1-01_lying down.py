
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Lying Down")

# Colors and settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCALE = 2.5
CENTER = (WIDTH//2, HEIGHT//2)
FPS = 30

# Define joint positions for standing and lying states (model coordinates)
points = [
    # Head, Neck
    ((0, -120), (0, 0)), ((0, -100), (0, 20)),
    # Shoulders
    ((-25, -90), (-80, 30)), ((25, -90), (-80, -30)),
    # Elbows
    ((-40, -70), (-100, 60)), ((40, -70), (-100, -60)),
    # Wrists
    ((-55, -50), (-120, 90)), ((55, -50), (-120, -90)),
    # Torso, Hips
    ((0, -80), (0, 0)), ((-20, -60), (40, 30)), ((20, -60), (40, -30)),
    # Knees
    ((-20, -30), (80, 60)), ((20, -30), (80, -60)),
    # Ankles
    ((-20, 0), (120, 90)), ((20, 0), (120, -90))
]

def ease_in_out(t):
    return 0.5 - math.cos(t * math.pi) / 2

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate animation progress with easing
    elapsed = pygame.time.get_ticks() - start_time
    t = ease_in_out((elapsed % 3000) / 3000)  # 3 second cycle

    screen.fill(BLACK)

    # Draw all joints
    for start, end in points:
        # Interpolate positions
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        
        # Convert to screen coordinates
        screen_x = CENTER[0] + x * SCALE
        screen_y = CENTER[1] - y * SCALE  # Invert Y-axis
        
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), 6)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
