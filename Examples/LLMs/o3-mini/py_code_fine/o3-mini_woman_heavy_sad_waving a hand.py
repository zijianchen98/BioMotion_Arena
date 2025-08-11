
"""
This program displays a point‐light biological motion stimulus representing a “sadwoman with heavy weight” waving a hand.
It uses 15 white points on a black background. The skeleton is defined by 15 joints and the right arm (shoulder–elbow–hand)
is animated to simulate a biomechanically plausible, smooth waving motion.
"""

import sys
import math
import pygame

# Initialize pygame and set the window size and caption.
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Sadwoman Waving a Hand")
clock = pygame.time.Clock()

# Define colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Pre-calc fixed joint positions for the 15 points.
# The points represent: 
#  0: Head, 1: Left Shoulder, 2: Right Shoulder,
#  3: Left Elbow, 4: Right Elbow (animated),
#  5: Left Hand, 6: Right Hand (animated),
#  7: Torso (Chest), 8: Pelvis, 9: Left Hip, 10: Right Hip,
#  11: Left Knee, 12: Right Knee, 13: Left Foot, 14: Right Foot
#
# The base positions are chosen for a standing figure with a slightly drooped posture (sad, heavy weight).
head = (400, 150)
left_shoulder = (350, 200)
right_shoulder = (450, 200)
left_elbow = (330, 260)   # static for left side
left_hand = (320, 320)    # static for left side
torso = (400, 260)
pelvis = (400, 330)
left_hip = (370, 335)
right_hip = (430, 335)
left_knee = (360, 400)
right_knee = (440, 400)
left_foot = (350, 470)
right_foot = (450, 470)

# Parameters for the right arm (which will be animated to wave):
# We'll simulate the right upper arm as a segment from right_shoulder.
# Set upper arm and forearm lengths (in pixels):
upper_arm_length = 70
forearm_length = 70
# For a heavy, sad posture, the initial arm is drooping.
# We choose a fixed base angle (in radians) from the shoulder.
base_angle = math.radians(110)  # roughly pointing downward and slightly outward

# Waving parameters: Let the forearm (right hand) oscillate relative to the upper arm.
wave_amplitude = 0.4   # amplitude of oscillation in radians (~23 degrees)
wave_speed = 0.005     # controls the speed of waving

def compute_right_arm_positions(time_ms):
    """
    Given the current time (in milliseconds), compute the positions (as (x, y) tuples)
    of the right elbow and right hand.
    The right_shoulder is fixed.
    """
    # Calculate oscillation for the waving motion.
    delta = wave_amplitude * math.sin(time_ms * wave_speed)
    
    # Right elbow position is determined by the upper arm.
    ex = right_shoulder[0] + upper_arm_length * math.cos(base_angle)
    ey = right_shoulder[1] + upper_arm_length * math.sin(base_angle)
    right_elbow = (ex, ey)
    
    # The forearm (from elbow to hand) rotates relative to the upper arm.
    forearm_angle = base_angle + delta
    hx = ex + forearm_length * math.cos(forearm_angle)
    hy = ey + forearm_length * math.sin(forearm_angle)
    right_hand = (hx, hy)
    
    return right_elbow, right_hand

def draw_points(points_list):
    """
    Draw each point as a white filled circle.
    """
    for point in points_list:
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), POINT_RADIUS)

running = True
while running:
    # Event processing.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background.
    screen.fill(BLACK)

    # Get current time for animation.
    current_time = pygame.time.get_ticks()

    # Update the dynamic points for the right arm.
    right_elbow, right_hand = compute_right_arm_positions(current_time)
    
    # Construct the full list of 15 point positions.
    # Order of points as described in the comment above:
    joint_positions = [
        head,                     # 0. Head
        left_shoulder,            # 1. Left Shoulder
        right_shoulder,           # 2. Right Shoulder
        left_elbow,               # 3. Left Elbow
        right_elbow,              # 4. Right Elbow (animated)
        left_hand,                # 5. Left Hand
        right_hand,               # 6. Right Hand (animated)
        torso,                    # 7. Torso (Chest)
        pelvis,                   # 8. Pelvis
        left_hip,                 # 9. Left Hip
        right_hip,                # 10. Right Hip
        left_knee,                # 11. Left Knee
        right_knee,               # 12. Right Knee
        left_foot,                # 13. Left Foot
        right_foot                # 14. Right Foot
    ]
    
    # Draw the point-lights.
    draw_points(joint_positions)
    
    # Optionally, you can draw lines between joints to help the viewer appreciate the motion
    # (commented out since the specification says "point-lights" only).
    # However, if needed for debugging, uncomment the following block:
    """
    skeleton_connections = [
        (0, 1), (0, 2),   # Head to shoulders
        (1, 3), (2, 4),   # Shoulders to elbows
        (3, 5), (4, 6),   # Elbows to hands
        (1, 7), (2, 7),   # Shoulders to torso
        (7, 8),          # Torso to Pelvis
        (8, 9), (8, 10),  # Pelvis to hips
        (9, 11), (10, 12),# Hips to knees
        (11, 13), (12, 14) # Knees to feet
    ]
    for start, end in skeleton_connections:
        pygame.draw.line(screen, WHITE, joint_positions[start], joint_positions[end], 1)
    """
    
    pygame.display.flip()
    clock.tick(60)  # limit to 60 frames per second

pygame.quit()
sys.exit()