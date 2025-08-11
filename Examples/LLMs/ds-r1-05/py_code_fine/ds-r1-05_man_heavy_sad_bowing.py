
import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Bowing Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 30

# Initial joint positions (person facing right, side-view)
base_points = [
    (0, -100),    # Head
    (0, -80),     # Neck
    (-15, -70),   # Left Shoulder
    (-35, -50),   # Left Elbow
    (-55, -30),   # Left Wrist
    (15, -70),    # Right Shoulder
    (35, -50),    # Right Elbow
    (55, -30),    # Right Wrist
    (0, 0),       # Mid Hip
    (-15, 0),     # Left Hip
    (15, 0),      # Right Hip
    (-15, 40),    # Left Knee
    (15, 40),     # Right Knee
    (-15, 80),    # Left Ankle
    (15, 80)      # Right Ankle
]

# Translate points to screen center
def translate_points(points, offset_x, offset_y):
    return [(x + offset_x, y + offset_y) for x, y in points]

# Rotate point around pivot (clockwise for forward bowing)
def rotate_point(point, pivot, angle):
    px, py = pivot
    x, y = point
    # Translate to origin
    tx, ty = x - px, y - py
    # Rotate (clockwise: cos(a) and sin(a) with the given signs)
    rx = tx * math.cos(angle) + ty * math.sin(angle)
    ry = -tx * math.sin(angle) + ty * math.cos(angle)
    # Translate back
    return (rx + px, ry + py)

# Main animation loop
running = True
time_passed = 0.0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen to black
    screen.fill(BLACK)
    
    # Sinusoidal bending (0 to 70 degrees and back)
    max_bend_degrees = 70
    bend_radians = math.radians(max_bend_degrees) * abs(math.sin(time_passed * 2))
    
    # Copy base points
    current_points = base_points[:]
    pivot = (0, 0)  # Mid Hip (index 8) is pivot
    
    # Apply rotation to upper body points (index 0 to 7)
    for i in range(8):  # Head to Right Wrist
        current_points[i] = rotate_point(current_points[i], pivot, bend_radians)
    
    # Translate to screen center
    current_points = translate_points(current_points, WIDTH//2, HEIGHT//2)
    
    # Draw points as white circles
    for point in current_points:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)
    
    pygame.display.flip()
    time_passed += 1 / FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
