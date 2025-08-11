
"""
This program shows a point‐light stimulus animation representing biological motion 
of a happy, light‐weight woman performing a sitting‐down action.
It uses 15 white point‐lights (representing key joints) moving on a solid black background.
The motion is generated via a smooth interpolation (with an easing function) between
a standing pose and a sitting pose.
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen parameters
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Sitting Down")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Define the two poses with 15 markers each.
# Pose indices:
# 0 - Head
# 1 - Left Shoulder
# 2 - Right Shoulder
# 3 - Left Elbow
# 4 - Right Elbow
# 5 - Left Hand
# 6 - Right Hand
# 7 - Spine
# 8 - Pelvis (center)
# 9 - Left Hip
# 10 - Right Hip
# 11 - Left Knee
# 12 - Right Knee
# 13 - Left Ankle
# 14 - Right Ankle

# Standing pose (approximate frontal view)
standing_pose = [
    (320,  80),   # 0 Head
    (280, 120),   # 1 Left Shoulder
    (360, 120),   # 2 Right Shoulder
    (260, 160),   # 3 Left Elbow
    (380, 160),   # 4 Right Elbow
    (250, 200),   # 5 Left Hand
    (390, 200),   # 6 Right Hand
    (320, 150),   # 7 Spine
    (320, 200),   # 8 Pelvis (center)
    (300, 200),   # 9 Left Hip
    (340, 200),   # 10 Right Hip
    (290, 260),   # 11 Left Knee
    (350, 260),   # 12 Right Knee
    (280, 320),   # 13 Left Ankle
    (360, 320)    # 14 Right Ankle
]

# Sitting pose (approximate frontal view, mimicking a sitting down posture)
sitting_pose = [
    (320,  80),   # 0 Head (remains roughly at the same height)
    (280, 120),   # 1 Left Shoulder (slight adjustment can be made)
    (360, 120),   # 2 Right Shoulder
    (270, 140),   # 3 Left Elbow (arm lifted slightly)
    (350, 140),   # 4 Right Elbow
    (260, 160),   # 5 Left Hand
    (360, 160),   # 6 Right Hand
    (320, 170),   # 7 Spine (bent forward slightly)
    (320, 210),   # 8 Pelvis (center lowered)
    (305, 210),   # 9 Left Hip (moved inward a bit)
    (335, 210),   # 10 Right Hip
    (300, 250),   # 11 Left Knee (bent)
    (340, 250),   # 12 Right Knee
    (300, 300),   # 13 Left Ankle (moved up toward the body)
    (340, 300)    # 14 Right Ankle
]

# Total animation duration (in seconds) and total frames.
animation_duration = 2.5  # seconds for the sitting down transition
total_frames = int(FPS * animation_duration)

# Easing function (ease-in-out using half cosine) for smooth interpolation
def ease_in_out(t):
    # t is a value in [0, 1]
    return 0.5 - 0.5 * math.cos(math.pi * t)

# Interpolate between two poses
def interpolate_pose(pose_start, pose_end, t_normalized):
    # t_normalized is between 0 and 1; apply easing.
    t = ease_in_out(t_normalized)
    interp_pose = []
    for (x0, y0), (x1, y1) in zip(pose_start, pose_end):
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        interp_pose.append((x, y))
    return interp_pose

# Main animation loop
frame = 0
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen: fill with black
    screen.fill((0, 0, 0))

    # Compute normalized time factor; if animation finished, hold last pose.
    if frame < total_frames:
        t_normalized = frame / total_frames
    else:
        t_normalized = 1.0

    # Interpolate current pose between standing and sitting
    current_pose = interpolate_pose(standing_pose, sitting_pose, t_normalized)

    # Draw the point-lights (white circles)
    # Ensure exactly 15 points
    for point in current_pose:
        pygame.draw.circle(screen, (255, 255, 255), (int(point[0]), int(point[1])), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
    frame += 1

# Clean up
pygame.quit()
sys.exit()