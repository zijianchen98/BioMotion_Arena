
"""
This program uses pygame to render a “point‐light” animation of a forward‐rolling human.
The simulation shows exactly 15 white points representing key joints (head, neck, shoulders, elbows, hands, torso, hips, knees, feet) 
moving against a solid black background. The animation simulates a biomechanically plausible forward roll 
via a continuous rigid-body rotation with a forward translation. While a full biomechanical simulation would 
involve complex joint kinematics, this animation uses a smooth rigid rotation plus slight limb‐offsets 
to evoke a “tucked” forward roll.
"""

import sys, math, pygame

# ---------- Configuration Parameters ----------
WIDTH, HEIGHT = 800, 600
FPS = 60

# Speed parameters:
# translation: move to the right simulating forward rolling
TRANSLATION_SPEED = 2         # pixels per frame
# rotation: one full roll every 120 frames (~2 seconds at 60 FPS)
ROTATION_SPEED = (2*math.pi) / 120   # radians per frame

# Visual parameters:
POINT_RADIUS = 5
POINT_COLOR = (255, 255, 255)  # white
BG_COLOR = (0, 0, 0)           # black

# ---------- Define the 15 Joint Points in a local coordinate system ----------
# The skeleton is defined in a “tucked” posture amenable to a forward roll.
# (x, y) coordinates: y increases downward.
# Coordinates adapted so that the center of the figure is near (0,0).
# Coordinates (in pixels)
# 1. Head, 2. Neck, 3. Right Shoulder, 4. Right Elbow, 5. Right Hand,
# 6. Left Shoulder, 7. Left Elbow, 8. Left Hand, 9. Torso,
# 10. Right Hip, 11. Right Knee, 12. Right Foot, 13. Left Hip, 14. Left Knee, 15. Left Foot.
joints = [
    (0, -40),    # Head
    (0, -30),    # Neck
    (10, -30),   # Right Shoulder
    (15, -20),   # Right Elbow
    (20, -10),   # Right Hand
    (-10, -30),  # Left Shoulder
    (-15, -20),  # Left Elbow
    (-20, -10),  # Left Hand
    (0, 0),      # Torso
    (8, 0),      # Right Hip
    (10, 20),    # Right Knee
    (12, 40),    # Right Foot
    (-8, 0),     # Left Hip
    (-10, 20),   # Left Knee
    (-12, 40)    # Left Foot
]

def rotate_point(x, y, angle):
    """
    Rotate a point (x, y) around the origin by the given angle (in radians).
    """
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return x * cos_a - y * sin_a, x * sin_a + y * cos_a

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Forward Rolling Point-Light Animation")
    clock = pygame.time.Clock()

    # Starting position for the figure (center of rotation translation).
    # We start sufficiently to the left so the figure rolls across the screen.
    base_x = 100
    base_y = HEIGHT // 2  + 50  # Adjust vertical offset for ground-level feeling

    # Initial rotation angle.
    angle = 0

    running = True
    while running:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update position and rotation.
        base_x += TRANSLATION_SPEED
        angle += ROTATION_SPEED

        # If the figure moves off the right edge, wrap around.
        if base_x > WIDTH + 50:
            base_x = -50

        # Clear screen.
        screen.fill(BG_COLOR)

        # Draw each of the 15 joints.
        for (jx, jy) in joints:
            # For a slightly more natural roll, we can simulate a tiny sinusoidal offset
            # on some joints (for instance the arms) relative to the body rotation.
            # Here, for demonstration, we add an extra offset to hand joints.
            extra_offset = (0, 0)
            if (jx, jy) in [(20, -10), (-20, -10)]:
                # vary vertical position by a small sine function
                offset_y = 3 * math.sin(angle * 2)
                extra_offset = (0, offset_y)
            
            # Combine the extra offset.
            point_local_x = jx + extra_offset[0]
            point_local_y = jy + extra_offset[1]
            # Rotate the joint about origin.
            rx, ry = rotate_point(point_local_x, point_local_y, angle)
            # Translate to screen coordinates.
            screen_x = int(base_x + rx)
            screen_y = int(base_y + ry)
            pygame.draw.circle(screen, POINT_COLOR, (screen_x, screen_y), POINT_RADIUS)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()