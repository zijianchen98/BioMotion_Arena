
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define points' standing and sitting positions (model coordinates)
points = [
    # Head
    {'standing': (0, -100), 'sitting': (0, -30)},
    # Neck
    {'standing': (0, -80), 'sitting': (0, -40)},
    # Left Shoulder
    {'standing': (-25, -80), 'sitting': (-25, -50)},
    # Right Shoulder
    {'standing': (25, -80), 'sitting': (25, -50)},
    # Left Elbow
    {'standing': (-50, -60), 'sitting': (-40, -20)},
    # Right Elbow
    {'standing': (50, -60), 'sitting': (40, -20)},
    # Left Wrist
    {'standing': (-60, -40), 'sitting': (-50, 10)},
    # Right Wrist
    {'standing': (60, -40), 'sitting': (50, 10)},
    # Upper Spine
    {'standing': (0, -70), 'sitting': (0, -45)},
    # Lower Spine
    {'standing': (0, -50), 'sitting': (0, 20)},
    # Left Hip
    {'standing': (-20, 0), 'sitting': (-20, 60)},
    # Right Hip
    {'standing': (20, 0), 'sitting': (20, 60)},
    # Left Knee
    {'standing': (-20, 50), 'sitting': (-35, 40)},
    # Right Knee
    {'standing': (20, 50), 'sitting': (35, 40)},
    # Mid Hip
    {'standing': (0, 0), 'sitting': (0, 60)},
]

# Animation parameters
speed = 0.75
scale = 3
time = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate smooth transition parameter
    time += 0.01
    t = (math.sin(time * speed * 2 * math.pi) + 1) / 2  # 0->1->0 cycle

    screen.fill(BLACK)

    # Draw each point-light
    for point in points:
        # Interpolate positions
        stand_x, stand_y = point['standing']
        sit_x, sit_y = point['sitting']
        current_x = stand_x + (sit_x - stand_x) * t
        current_y = stand_y + (sit_y - stand_y) * t

        # Convert to screen coordinates
        screen_x = width // 2 + current_x * scale
        screen_y = height // 2 - current_y * scale  # Invert y-axis

        # Render point
        pygame.draw.circle(screen, WHITE, (int(screen_x), int(screen_y)), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
