
"""
A Python program that shows a point‐light stimulus animation representing biological motion.
This animation depicts a happy man with light weight who is waving a hand.
It uses exactly 15 white point-lights on a solid black background.
The movement is biomechanically plausible and smooth.
"""

import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Waving Hand")

# Colors and point settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_RADIUS = 5

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Static points for the body (all coordinates relative to the window)
# We assume that the person is standing roughly in the center (x around 400, y between 180 and 420).
# The numbering of points (1 to 15) is as follows:
# 1: Head, 2: Upper spine, 3: Left shoulder, 4: Right shoulder, 5: Left elbow, 6: Right elbow,
# 7: Left hand, 8: Right hand (animated), 9: Left hip, 10: Right hip, 11: Left knee,
# 12: Right knee, 13: Left foot, 14: Right foot, 15: Belly (center torso)

# Define fixed key-points
head       = [400, 180]   # Point 1
upper_spine= [400, 220]   # Point 2
left_shoulder = [370, 220]# Point 3
right_shoulder= [430, 220]# Point 4
left_elbow   = [350, 250] # Point 5
right_elbow  = [450, 250] # Point 6
left_hand    = [340, 280] # Point 7 (static, left arm not waving)
# Point 8: right hand will be animated based on the right elbow.
left_hip     = [370, 280] # Point 9
right_hip    = [430, 280] # Point 10
left_knee    = [370, 350] # Point 11
right_knee   = [430, 350] # Point 12
left_foot    = [370, 420] # Point 13
right_foot   = [430, 420] # Point 14
belly       = [400, 260]  # Point 15

# Animation parameters for the waving hand (point 8)
# The waving hand is attached to the right elbow.
# The right hand's position is determined by an arm segment of fixed length oscillating with a sinusoidal function.
arm_length = 40  # pixels, length from right elbow to right hand
# Amplitude of angular oscillation in radians (30 degrees)
angle_amplitude = math.radians(30)
# Frequency of waving (cycles per second)
waving_frequency = 1.5  # cycles per second

def compute_right_hand_position(time_sec):
    """
    Compute the current position of the right hand as it waves.
    The hand oscillates around the right elbow.
    The baseline is with the hand extended horizontally (to the right) at 0 radians.
    The angle oscillates as: angle = amplitude * sin(2*pi*frequency*time)
    """
    angle = angle_amplitude * math.sin(2 * math.pi * waving_frequency * time_sec)
    # When angle==0, the hand is directly to the right of the elbow.
    x = right_elbow[0] + arm_length * math.cos(angle)
    y = right_elbow[1] + arm_length * math.sin(angle)
    return [int(x), int(y)]

def main():
    start_ticks = pygame.time.get_ticks()  # for timing the wave
    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get current elapsed time in seconds
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0

        # Compute current position for right hand (point 8)
        right_hand = compute_right_hand_position(t)

        # Clear screen with black background
        WINDOW.fill(BLACK)

        # Draw all 15 points as white circles.
        # Points that remain constant:
        points = [
            head,           # 1
            upper_spine,    # 2
            left_shoulder,  # 3
            right_shoulder, # 4
            left_elbow,     # 5
            right_elbow,    # 6
            left_hand,      # 7
            right_hand,     # 8 (animated)
            left_hip,       # 9
            right_hip,      # 10
            left_knee,      # 11
            right_knee,     # 12
            left_foot,      # 13
            right_foot,     # 14
            belly           # 15
        ]
        
        for pt in points:
            pygame.draw.circle(WINDOW, WHITE, pt, POINT_RADIUS)

        # Optionally, connect points with lines to hint at a figure (uncomment if desired)
        # This is not required by the specification but can add clarity
        # pygame.draw.line(WINDOW, WHITE, head, upper_spine, 2)
        # pygame.draw.line(WINDOW, WHITE, upper_spine, left_shoulder, 2)
        # pygame.draw.line(WINDOW, WHITE, upper_spine, right_shoulder, 2)
        # pygame.draw.line(WINDOW, WHITE, left_shoulder, left_elbow, 2)
        # pygame.draw.line(WINDOW, WHITE, left_elbow, left_hand, 2)
        # pygame.draw.line(WINDOW, WHITE, right_shoulder, right_elbow, 2)
        # pygame.draw.line(WINDOW, WHITE, right_elbow, right_hand, 2)
        # pygame.draw.line(WINDOW, WHITE, upper_spine, belly, 2)
        # pygame.draw.line(WINDOW, WHITE, belly, left_hip, 2)
        # pygame.draw.line(WINDOW, WHITE, belly, right_hip, 2)
        # pygame.draw.line(WINDOW, WHITE, left_hip, left_knee, 2)
        # pygame.draw.line(WINDOW, WHITE, left_knee, left_foot, 2)
        # pygame.draw.line(WINDOW, WHITE, right_hip, right_knee, 2)
        # pygame.draw.line(WINDOW, WHITE, right_knee, right_foot, 2)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()