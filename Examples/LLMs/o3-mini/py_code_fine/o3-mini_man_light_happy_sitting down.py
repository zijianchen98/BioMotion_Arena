
"""
This program displays a point‐light biological motion stimulus of a “happyman with light weight” sitting down.
It uses exactly 15 white points on a black background. The points represent key body landmarks,
and the animation smoothly interpolates between a standing posture and a sitting posture,
making the movement biomechanically plausible.
"""

import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up the drawing window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-light Biological Motion: Sitting Down")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the two postures: standing and sitting.
# All coordinates are absolute positions on the screen.
# The following 15 points represent:
# 1. Head, 2. Left Shoulder, 3. Right Shoulder, 
# 4. Left Elbow, 5. Right Elbow, 6. Left Wrist, 7. Right Wrist,
# 8. Chest, 9. Abdomen, 10. Left Hip, 11. Right Hip,
# 12. Left Knee, 13. Right Knee, 14. Left Ankle, 15. Right Ankle

standing = [
    (400, 200),  # Head
    (370, 230),  # Left Shoulder
    (430, 230),  # Right Shoulder
    (350, 270),  # Left Elbow
    (450, 270),  # Right Elbow
    (340, 310),  # Left Wrist
    (460, 310),  # Right Wrist
    (400, 250),  # Chest
    (400, 280),  # Abdomen
    (380, 320),  # Left Hip
    (420, 320),  # Right Hip
    (370, 380),  # Left Knee
    (430, 380),  # Right Knee
    (360, 440),  # Left Ankle
    (440, 440)   # Right Ankle
]

sitting = [
    (400, 210),  # Head (slightly lowered)
    (370, 240),  # Left Shoulder
    (430, 240),  # Right Shoulder
    (360, 260),  # Left Elbow (moving slightly forward/up)
    (440, 260),  # Right Elbow
    (355, 280),  # Left Wrist
    (445, 280),  # Right Wrist
    (400, 260),  # Chest (moved down a little)
    (400, 290),  # Abdomen
    (380, 300),  # Left Hip (rising to a seated level)
    (420, 300),  # Right Hip
    (380, 340),  # Left Knee (bent)
    (420, 340),  # Right Knee
    (370, 340),  # Left Ankle (shifted horizontally)
    (430, 340)   # Right Ankle
]

# Duration (in seconds) for one phase of the movement.
# We'll use a complete cycle: standing -> sitting -> standing.
phase_duration = 2.0  # seconds for one-way transition

clock = pygame.time.Clock()

def interpolate_points(pts_start, pts_end, f):
    """Linearly interpolates between two sets of points given a fraction f (0 to 1)."""
    interpolated = []
    for (x0, y0), (x1, y1) in zip(pts_start, pts_end):
        x = x0 + (x1 - x0) * f
        y = y0 + (y1 - y0) * f
        interpolated.append((x, y))
    return interpolated

def ease_in_out(t):
    """A smooth ease-in-out function using sine.
       Input t in [0, 1] returns a value in [0, 1] with smooth acceleration and deceleration.
    """
    return 0.5 * (1 - math.cos(math.pi * t))

# Main loop
start_ticks = pygame.time.get_ticks()  # start timer

running = True
while running:
    # Handle events (close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate elapsed time (in seconds)
    t = (pygame.time.get_ticks() - start_ticks) / 1000.0
    # The motion cycle is 2*phase_duration seconds (standing->sitting->standing)
    cycle_time = (t % (2 * phase_duration))
    
    # Calculate fraction (f) for the transition:
    if cycle_time < phase_duration:
        # Standing to Sitting phase
        f = cycle_time / phase_duration
    else:
        # Sitting back to Standing phase
        f = 1 - ((cycle_time - phase_duration) / phase_duration)
    
    # Optionally, use smooth easing function
    f_eased = ease_in_out(f)
    
    # Compute the current positions
    current_points = interpolate_points(standing, sitting, f_eased)
    
    # Fill the background
    screen.fill(BLACK)
    
    # Draw each point as a filled circle
    for pt in current_points:
        pygame.draw.circle(screen, WHITE, (int(pt[0]), int(pt[1])), 5)
    
    # Flip the display
    pygame.display.flip()
    
    # Cap the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()