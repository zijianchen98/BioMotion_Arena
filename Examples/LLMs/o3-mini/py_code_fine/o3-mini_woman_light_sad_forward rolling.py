
"""
This program uses Pygame to show a point‐light stimulus animation representing “biological motion”
of a sad, light‐weight woman doing a forward roll. The stimulus is made up of exactly 15 white dots
(rendered as circles) on a solid black background. The motion is implemented by “rolling” a body‐skeleton
representation (with 15 keypoints) across the screen: the skeleton rotates continuously (simulating a
forward roll) while its center steadily translates across the display. The positions of the dots are
defined relative to a body‐center so that the roll appears smooth, natural, and biomechanically plausible.
"""

import sys
import math
import pygame

# --- Configuration ---
WIDTH, HEIGHT = 800, 600          # Window dimensions
FPS = 60                          # Frames per second
DOT_RADIUS = 5                    # Radius of the point-light circles
ROLL_SPEED = math.radians(3)      # Rotation increment per frame (in radians)
TRANSLATION_SPEED = 2             # Horizontal translation (pixels per frame)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Point-Light Forward Roll Animation")
    clock = pygame.time.Clock()

    # Define the 15 keypoints (x, y) in a local body coordinate system.
    # These resemble a sadwoman posture:
    #   0: Head top
    #   14: Chin (to emphasize a sad, bowed head)
    #   1: Left shoulder
    #   2: Right shoulder
    #   3: Left elbow
    #   4: Right elbow
    #   5: Left wrist
    #   6: Right wrist
    #   7: Torso center
    #   8: Left hip
    #   9: Right hip
    #   10: Left knee
    #   11: Right knee
    #   12: Left ankle
    #   13: Right ankle
    skeleton = [
        (0, -50),    # 0: Head top
        (-15, -30),  # 1: Left shoulder
        (15, -30),   # 2: Right shoulder
        (-25, -10),  # 3: Left elbow
        (25, -10),   # 4: Right elbow
        (-30, 10),   # 5: Left wrist
        (30, 10),    # 6: Right wrist
        (0, 0),      # 7: Torso center
        (-10, 10),   # 8: Left hip
        (10, 10),    # 9: Right hip
        (-10, 30),   # 10: Left knee
        (10, 30),    # 11: Right knee
        (-10, 50),   # 12: Left ankle
        (10, 50),    # 13: Right ankle
        (0, -40)     # 14: Chin (emphasizes the bowed, sad look)
    ]
    
    # Calculate the center-of-mass (COM) of the skeleton.
    sum_x = sum(pt[0] for pt in skeleton)
    sum_y = sum(pt[1] for pt in skeleton)
    num_points = len(skeleton)
    com = (sum_x / num_points, sum_y / num_points)

    # Starting translation: place the COM near the left, vertically centered.
    translation_x = 100
    translation_y = HEIGHT // 2

    # Current rotation angle.
    angle = 0

    # Main animation loop.
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Allow quitting with the ESC key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update rotation angle and horizontal translation for the roll.
        angle += ROLL_SPEED
        translation_x += TRANSLATION_SPEED

        # Clear screen with a black background.
        screen.fill((0, 0, 0))
        
        # For each point in the skeleton apply the rotation and translation.
        for (x, y) in skeleton:
            # Translate point to be relative to COM.
            rel_x = x - com[0]
            rel_y = y - com[1]
            # Rotate around the COM.
            rotated_x = rel_x * math.cos(angle) - rel_y * math.sin(angle)
            rotated_y = rel_x * math.sin(angle) + rel_y * math.cos(angle)
            # Translate back and add overall translation (keeping the body upright relative to the screen).
            final_x = rotated_x + com[0] + translation_x
            final_y = rotated_y + com[1] + translation_y

            # Draw the white point-light (circle).
            pygame.draw.circle(screen, (255, 255, 255), (int(final_x), int(final_y)), DOT_RADIUS)

        pygame.display.flip()

        # Wrap-around: when the COM moves off the right side, start from the left again.
        if translation_x > WIDTH + 100:
            translation_x = -100

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()