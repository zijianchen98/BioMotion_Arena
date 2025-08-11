
"""
This program uses Pygame to animate a point‐light display representing a man “sitting down.”
It shows 15 white point‐lights (representing joints) on a solid black background.
The initial posture is a standing position and the final posture is a sitting position.
The joint positions smoothly interpolate using an ease‑in‑out function for natural motion.
"""

import pygame
import sys
import time

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Duration of the animation in seconds
ANIMATION_DURATION = 3.0

# Points names (15 joints)
joint_names = [
    "head",
    "neck",
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_hand",
    "right_hand",
    "torso",
    "left_hip",
    "right_hip",
    "left_knee",
    "right_knee",
    "left_foot",
    "right_foot"
]

# Initial positions (standing posture)
# Coordinates are chosen in the window (x,y)
initial_positions = {
    "head": (300, 100),
    "neck": (300, 140),
    "left_shoulder": (260, 140),
    "right_shoulder": (340, 140),
    "left_elbow": (240, 180),
    "right_elbow": (360, 180),
    "left_hand": (230, 220),
    "right_hand": (370, 220),
    "torso": (300, 200),
    "left_hip": (280, 240),
    "right_hip": (320, 240),
    "left_knee": (280, 320),
    "right_knee": (320, 320),
    "left_foot": (280, 400),
    "right_foot": (320, 400)
}

# Final positions (sitting posture)
final_positions = {
    "head": (300, 100),          # head remains in place
    "neck": (300, 140),
    "left_shoulder": (260, 140),
    "right_shoulder": (340, 140),
    "left_elbow": (240, 180),
    "right_elbow": (360, 180),
    "left_hand": (230, 220),
    "right_hand": (370, 220),
    "torso": (300, 220),         # torso drops slightly lower
    "left_hip": (280, 260),
    "right_hip": (320, 260),
    "left_knee": (260, 300),     # knees move forward and up to simulate bending
    "right_knee": (340, 300),
    "left_foot": (260, 380),     # feet repositioned for sitting posture
    "right_foot": (340, 380)
}

def ease_in_out(t):
    """
    Smooth ease-in-out interpolation function.
    t should be in the range [0, 1] and the output will also be in [0, 1].
    """
    return 3 * t**2 - 2 * t**3

def interpolate_points(start, end, factor):
    """
    Linearly interpolate between two points (start and end) with the given factor.
    factor should be between 0 and 1.
    """
    x0, y0 = start
    x1, y1 = end
    x = x0 + factor * (x1 - x0)
    y = y0 + factor * (y1 - y0)
    return (x, y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-light Biological Motion: Sitting Down")
    clock = pygame.time.Clock()

    start_time = time.time()
    running = True

    while running:
        # Handle events: graceful exit if window is closed or ESC is pressed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Time elapsed since the start of the animation
        elapsed = time.time() - start_time

        # Compute interpolation factor t in [0,1]
        if elapsed < ANIMATION_DURATION:
            t = elapsed / ANIMATION_DURATION
        else:
            t = 1.0  # hold final posture after animation

        # Apply ease in/out on t for smooth movement.
        smooth_t = ease_in_out(t)

        # Compute the current positions for all joints
        current_positions = {}
        for joint in joint_names:
            start_pos = initial_positions[joint]
            end_pos = final_positions[joint]
            current_positions[joint] = interpolate_points(start_pos, end_pos, smooth_t)

        # Draw the animation frame
        screen.fill(BLACK)
        # Draw each joint as a white circle ("point-light").
        for joint in joint_names:
            pos = current_positions[joint]
            pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), 4)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()