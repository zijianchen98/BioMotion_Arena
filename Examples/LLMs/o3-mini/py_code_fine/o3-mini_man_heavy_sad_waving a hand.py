
"""
A Python program using pygame to animate a point‐light stimulus of a “sad man with heavy weight” 
waving his right hand. The animation displays exactly 15 white point‐lights over a solid black background.
The 15 points represent body landmarks (head, shoulders, elbows, wrists, hips, knees, ankles, and feet).
The animation simulates a biomechanically plausible waving motion of the right wrist.
"""

import pygame
import sys
import math

# Initialize pygame and window parameters
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion - Waving Hand")
clock = pygame.time.Clock()
FPS = 60

# Define the 15 landmark points as the static body structure.
#
# The points represent:
#  0: Head
#  1: Left Shoulder
#  2: Right Shoulder
#  3: Left Elbow
#  4: Right Elbow
#  5: Left Wrist
#  6: Right Wrist  (will be animated to simulate waving)
#  7: Left Hip
#  8: Right Hip
#  9: Left Knee
# 10: Right Knee
# 11: Left Ankle
# 12: Right Ankle
# 13: Left Foot
# 14: Right Foot
#
# These base coordinates are chosen to look like a slightly slumped figure to represent a heavy, sad posture.

base_points = [
    (400, 100),  # 0: Head
    (370, 150),  # 1: Left Shoulder
    (430, 150),  # 2: Right Shoulder
    (350, 200),  # 3: Left Elbow
    (450, 200),  # 4: Right Elbow
    (330, 250),  # 5: Left Wrist
    (470, 250),  # 6: Right Wrist (base position, to be animated)
    (380, 250),  # 7: Left Hip
    (420, 250),  # 8: Right Hip
    (370, 350),  # 9: Left Knee
    (430, 350),  # 10: Right Knee
    (360, 450),  # 11: Left Ankle
    (440, 450),  # 12: Right Ankle
    (350, 480),  # 13: Left Foot
    (450, 480)   # 14: Right Foot
]

# For realistic waving, we simulate a rotation of the right wrist about the right elbow.
# We treat the right wrist as connected to the right elbow by a rigid segment.
# The base vector (from the right elbow to the right wrist) is computed from base_points.
right_elbow = base_points[4]
right_wrist_base = base_points[6]
dx = right_wrist_base[0] - right_elbow[0]
dy = right_wrist_base[1] - right_elbow[1]
segment_length = math.hypot(dx, dy)
# Determine the base angle (in degrees) of the segment.
base_angle_deg = math.degrees(math.atan2(dy, dx))
# The waving motion will rotate this segment about the right elbow, oscillating around the base angle.
# Here, we set an amplitude (in degrees) for the waving motion.
angle_amplitude = 15  # degrees
# Frequency of waving (cycles per second)
waving_frequency = 2  

def compute_right_wrist(t):
    """
    Compute the updated position of the right wrist based on time t.
    The angle oscillates around the base angle to simulate the waving.
    """
    angle_offset = angle_amplitude * math.sin(2 * math.pi * waving_frequency * t)
    current_angle_deg = base_angle_deg + angle_offset
    # Convert to radians for computation.
    current_angle_rad = math.radians(current_angle_deg)
    new_x = right_elbow[0] + segment_length * math.cos(current_angle_rad)
    new_y = right_elbow[1] + segment_length * math.sin(current_angle_rad)
    return (new_x, new_y)

def main():
    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        # Manage event queue.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate elapsed time in seconds.
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Create a copy of the base points that we can modify.
        current_points = list(base_points)
        # Update right wrist point (index 6) with the computed waving motion.
        current_points[6] = compute_right_wrist(t)
        
        # For extra biomechanical plausibility and to show weight, one could add subtle sway in the hips.
        # For demonstration, we add a very slight vertical oscillation to the hip points.
        hip_offset = 2 * math.sin(0.5 * 2 * math.pi * t)
        current_points[7] = (base_points[7][0], base_points[7][1] + hip_offset)
        current_points[8] = (base_points[8][0], base_points[8][1] + hip_offset)

        # Draw black background.
        screen.fill((0, 0, 0))

        # Draw each landmark as a small white circle.
        for point in current_points:
            pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 4)

        # Update the display.
        pygame.display.flip()

        # Cap the frame rate.
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()