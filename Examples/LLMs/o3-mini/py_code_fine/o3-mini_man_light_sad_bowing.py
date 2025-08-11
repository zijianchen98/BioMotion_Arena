
"""
This program creates a point‐light animation of a “sadman” bowing.
It displays exactly 15 white points on a black background representing
key joints of a human figure. The upper body (head, spine top, shoulders, elbows, wrists)
rotates about the lower spine (“spine bottom”) to simulate a realistic
bowing motion.
Press the window close button or ESC to exit.
"""

import sys, math, pygame

# Initialize pygame.
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Point-Light Biological Motion: Bowing")

clock = pygame.time.Clock()
FPS = 60

# Define the skeleton joint positions in the upright pose.
# There are 15 points in the following order:
# 0: Head
# 1: Spine Top
# 2: Spine Bottom (pivot for rotation)
# 3: Left Shoulder
# 4: Right Shoulder
# 5: Left Elbow
# 6: Right Elbow
# 7: Left Wrist
# 8: Right Wrist
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle
joints = [
    (300, 220),  # Head
    (300, 240),  # Spine Top
    (300, 260),  # Spine Bottom (pivot)
    (280, 240),  # Left Shoulder
    (320, 240),  # Right Shoulder
    (270, 260),  # Left Elbow
    (330, 260),  # Right Elbow
    (265, 280),  # Left Wrist
    (335, 280),  # Right Wrist
    (290, 260),  # Left Hip
    (310, 260),  # Right Hip
    (285, 300),  # Left Knee
    (315, 300),  # Right Knee
    (280, 340),  # Left Ankle
    (320, 340)   # Right Ankle
]

# Identify the indices of the joints that belong to the upper body.
# Those joints will undergo rotation (bowing movement) around the pivot.
upper_body_indices = [0, 1, 3, 4, 5, 6, 7, 8]
# The pivot is the spine bottom at index 2.
pivot = joints[2]

# Bowing motion parameters:
# Amplitude: up to 20 degrees clockwise (converted to radians)
max_angle = math.radians(20)
# Bowing will be cyclic (sine wave) with a period of 2 seconds.
period = 2.0

def rotate_point(point, pivot, angle):
    """
    Rotate a point around a pivot by the given angle.
    Angle is in radians. A negative angle produces a clockwise rotation,
    which is used to mimic the bowing (head and upper body bending downward).
    """
    # Translate point relative to pivot
    dx = point[0] - pivot[0]
    dy = point[1] - pivot[1]
    # Rotate the point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    rx = dx * cos_a - dy * sin_a
    ry = dx * sin_a + dy * cos_a
    # Translate back
    return (pivot[0] + rx, pivot[1] + ry)

def main():
    start_ticks = pygame.time.get_ticks()  # starting time in milliseconds

    running = True
    while running:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Calculate time elapsed in seconds.
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Calculate the current rotation angle.
        # We use a sine function to get a smooth oscillatory motion.
        # Multiplying by -max_angle to produce a clockwise rotation (bowing).
        angle = -max_angle * math.sin(2 * math.pi * t / period)

        # Clear the screen to black.
        screen.fill((0, 0, 0))

        # Draw each joint.
        # For joints in the upper body, apply the rotation.
        for idx, pt in enumerate(joints):
            if idx in upper_body_indices:
                new_pt = rotate_point(pt, pivot, angle)
            else:
                new_pt = pt
            # Draw the point as a white circle, radius 5.
            pygame.draw.circle(screen, (255, 255, 255), (int(new_pt[0]), int(new_pt[1])), 5)

        # Update the display.
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()