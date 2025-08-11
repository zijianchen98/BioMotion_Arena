
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Animation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for frame rate control
clock = pygame.time.Clock()

# Jump parameters
jump_duration = 1.5  # seconds per jump cycle
jump_height = 30     # pixels
forward_speed = 50   # pixels per second
base_y = height * 0.7  # ground level

# Point-light definitions (relative to center)
points_base = [
    (0, -40),    # Head
    (-15, -30),  # Left shoulder
    (15, -30),   # Right shoulder
    (-25, -20),  # Left elbow
    (25, -20),   # Right elbow
    (-35, -5),   # Left hand
    (35, -5),    # Right hand
    (-15, 0),    # Left hip
    (15, 0),     # Right hip
    (-20, 20),   # Left knee
    (20, 20),    # Right knee
    (-25, 40),   # Left ankle
    (25, 40),    # Right ankle
    (-30, 50),   # Left foot
    (30, 50)     # Right foot
]

time_elapsed = 0.0

# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(60) / 1000.0
    time_elapsed += dt

    # Calculate jump phase
    jump_phase = time_elapsed % jump_duration
    t = jump_phase / jump_duration

    # Vertical motion (parabolic trajectory)
    vertical_offset = -4 * jump_height * t * (t - 1)
    current_y = base_y - vertical_offset

    # Horizontal motion with wrap-around
    current_x = (width * 0.2 + forward_speed * time_elapsed) % (width * 1.2)

    # Squash effect during landing
    squash = 1.0
    if t > 0.7:
        squash = max(0.8, 1.0 - (t - 0.7) * 4)

    screen.fill(BLACK)

    # Draw all points
    for idx, (dx, dy) in enumerate(points_base):
        # Apply dynamic offsets
        mod_dx = dx
        mod_dy = dy * squash

        # Limb-specific animations
        if idx in [5, 6]:  # Hands
            mod_dy += 15 * math.sin(2 * math.pi * t)
        elif idx in [9, 10]:  # Knees
            mod_dy += 10 * (1 - abs(t - 0.5) * 2
        elif idx in [3, 4]:  # Elbows
            mod_dx += 8 * math.sin(2 * math.pi * t)

        # Calculate actual position
        pos_x = current_x + mod_dx
        pos_y = current_y + mod_dy

        # Keep points within screen bounds
        if pos_x < -30:
            pos_x += width * 1.2
        elif pos_x > width * 1.2:
            pos_x -= width * 1.2

        pygame.draw.circle(screen, WHITE, (int(pos_x), int(pos_y)), 5)

    pygame.display.flip()
