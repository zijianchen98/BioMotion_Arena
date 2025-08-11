
"""
This Python program uses Pygame to display a point‐light biological motion
animation on a black background. The 15 white dots represent key points on
a happy, light‐weight woman who is waving a hand. The program sets up a
simplified stick‐figure (point-light display) with 15 points:
 
  1. Head
  2. Left Shoulder
  3. Right Shoulder
  4. Left Elbow
  5. Right Elbow
  6. Left Hand
  7. Right Hand (animated to wave)
  8. Upper Spine
  9. Torso
 10. Left Hip
 11. Right Hip
 12. Left Knee
 13. Right Knee
 14. Left Foot
 15. Right Foot

The right-hand point is animated to simulate a natural hand‐waving motion,
rotating around the right elbow in a biomechanically plausible way.
"""

import pygame
import math
import sys

# Initialize Pygame and set up the display window.
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion Point-Light Animation")
clock = pygame.time.Clock()

# Define body fixed points (x, y) relative to the window.
# Positions chosen for a simplified stick figure.
# Base coordinates:
head       = (400, 150)  # Point 1: Head
left_shoulder  = (360, 200)  # Point 2
right_shoulder = (440, 200)  # Point 3
left_elbow     = (330, 250)  # Point 4
right_elbow    = (470, 250)  # Point 5 -- used as pivot for right hand
left_hand      = (320, 300)  # Point 6 (static)
# Point 7: Right hand will be calculated dynamically

upper_spine   = (400, 210)  # Point 8
torso        = (400, 260)  # Point 9
left_hip      = (370, 300)  # Point 10
right_hip     = (430, 300)  # Point 11
left_knee     = (360, 350)  # Point 12
right_knee    = (440, 350)  # Point 13
left_foot     = (350, 400)  # Point 14
right_foot    = (450, 400)  # Point 15

# The right hand (point 7) will be computed relative to right_elbow.
# Define arm segment length (from elbow to hand) and baseline angle.
hand_length = 50
# Baseline angle in radians (waving: hand initially somewhat raised).
# Here, -pi/4 means the hand is angled up (relative to horizontal right)
base_angle = -math.pi / 4  

# Animation parameters for the waving motion.
# Oscillate the angle with an amplitude (in radians) and frequency.
amplitude = math.radians(20)  # 20 degree amplitude
frequency = 2.0  # cycles per second

def compute_right_hand(elbow, t):
    """
    Compute the position of the right hand (point 7) given the elbow position and time.
    The angle is the sum of a base_angle and a sinusoidal modulation.
    """
    # Compute the offset angle using a sine function for a smooth oscillation.
    offset = amplitude * math.sin(2 * math.pi * frequency * t)
    angle = base_angle + offset
    # Calculate the hand position relative to the elbow.
    hand_x = elbow[0] + hand_length * math.cos(angle)
    hand_y = elbow[1] + hand_length * math.sin(angle)
    return (int(hand_x), int(hand_y))

def main():
    start_ticks = pygame.time.get_ticks()  # get start time in milliseconds
    running = True
    while running:
        # Handle events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate time in seconds.
        t = (pygame.time.get_ticks() - start_ticks) / 1000.0
        
        # Compute the dynamic position for the right hand.
        right_hand = compute_right_hand(right_elbow, t)
        
        # Create a list of all point-light positions.
        points = [
            head,            # 1
            left_shoulder,   # 2
            right_shoulder,  # 3
            left_elbow,      # 4
            right_elbow,     # 5
            left_hand,       # 6
            right_hand,      # 7 (animated)
            upper_spine,     # 8
            torso,           # 9
            left_hip,        # 10
            right_hip,       # 11
            left_knee,       # 12
            right_knee,      # 13
            left_foot,       # 14
            right_foot       # 15
        ]
        
        # Clear the screen with black.
        screen.fill((0, 0, 0))
        
        # Draw each point as a white circle.
        for pt in points:
            pygame.draw.circle(screen, (255, 255, 255), pt, 5)
        
        # Update the display.
        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate at 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()