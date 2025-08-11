
"""
This Python program uses Pygame to generate a realistic, biomechanically plausible
point‐light animation on a black background. Exactly 15 white point‐lights are used
to depict a “happyman with heavy weight” who is waving his right hand. The 15 points
represent key joints of a human figure (head, neck, shoulders, elbows, hands, torso,
hips, knees, and ankles).

The right “hand” is animated by simulating a natural waving motion via a sinusoidal
rotation of the right forearm (from right elbow to right hand). The overall body is drawn
in a static posture with the exception of the waving hand. A subtle sway is also added
to the entire body to suggest the heaviness of the subject. The animation runs at 60 FPS.
"""

import pygame
import math
import sys

# Pygame initialization
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Biological Motion - Point-Light Stimulus")
clock = pygame.time.Clock()

# Colors and parameters
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
point_radius = 5

# Center point for skeleton (torso center reference)
mid_x = width // 2
mid_y = height // 2

# Base static joint positions (in pixels) relative to the mid point.
# These 15 joint positions describe:
# 1. Head, 2. Neck, 3. Left Shoulder, 4. Right Shoulder, 5. Left Elbow,
# 6. Right Elbow, 7. Left Hand, 8. Right Hand (base vector, animated later),
# 9. Torso, 10. Left Hip, 11. Right Hip, 12. Left Knee, 13. Right Knee,
# 14. Left Ankle, 15. Right Ankle.
base_joints = {
    "head":       (mid_x,      mid_y - 100),
    "neck":       (mid_x,      mid_y - 80),
    "l_shoulder": (mid_x - 40, mid_y - 80),
    "r_shoulder": (mid_x + 40, mid_y - 80),
    "l_elbow":    (mid_x - 60, mid_y - 40),
    "r_elbow":    (mid_x + 60, mid_y - 40),
    "l_hand":     (mid_x - 65, mid_y - 10),
    # "r_hand" will be computed dynamically
    "torso":      (mid_x,      mid_y - 50),
    "l_hip":      (mid_x - 25, mid_y + 0),
    "r_hip":      (mid_x + 25, mid_y + 0),
    "l_knee":     (mid_x - 25, mid_y + 50),
    "r_knee":     (mid_x + 25, mid_y + 50),
    "l_ankle":    (mid_x - 25, mid_y + 90),
    "r_ankle":    (mid_x + 25, mid_y + 90)
}

# We need 15 points; our dynamic point "r_hand" will be added later.
joint_order = [
    "head", "neck", "l_shoulder", "r_shoulder", "l_elbow", "r_elbow",
    "l_hand", "r_hand", "torso", "l_hip", "r_hip", "l_knee", "r_knee",
    "l_ankle", "r_ankle"
]

# For the right arm, we define the base vector from the right elbow to the right hand.
# Base (static) r_hand is offset relative to r_elbow.
base_r_hand_offset = (15, 20)  # from right elbow at (mid_x+60, mid_y-40)
# Pre-calculate base angle and length.
base_length = math.hypot(base_r_hand_offset[0], base_r_hand_offset[1])
base_angle = math.atan2(base_r_hand_offset[1], base_r_hand_offset[0])

# Waving parameters for the right hand:
wave_amplitude = math.radians(20)  # maximum deviation of 20 degrees (~0.35 rad)
wave_frequency = math.pi  # cycles per second (period ~2 seconds)

# Optional: A subtle sway of the whole body (to show the heaviness)
sway_amplitude = 5   # pixels to sway horizontally
sway_frequency = 0.5 # cycles per second

def get_dynamic_joints(time_elapsed):
    """
    Compute the current positions of all joints.
    The right hand position is animated to wave via rotation of the right forearm,
    and a subtle horizontal sway is applied to all joints.
    """
    joints = {}

    # Compute horizontal sway offset (simulate heavy weight shift)
    # Using a slow sine movement.
    sway_offset = sway_amplitude * math.sin(2 * math.pi * sway_frequency * time_elapsed)
    
    # Process static joints (with sway applied)
    for key, pos in base_joints.items():
        x, y = pos
        joints[key] = (x + sway_offset, y)

    # Right hand: animate as a rotation of the base offset vector from r_elbow.
    # Compute oscillation offset based on time.
    delta_angle = wave_amplitude * math.sin(wave_frequency * time_elapsed)
    new_angle = base_angle + delta_angle

    # New vector for right hand relative to right elbow.
    dx = base_length * math.cos(new_angle)
    dy = base_length * math.sin(new_angle)
    
    # r_elbow position updated with sway offset:
    r_elbow_x, r_elbow_y = joints["r_elbow"]
    r_hand = (r_elbow_x + dx, r_elbow_y + dy)
    joints["r_hand"] = r_hand

    return joints

def main():
    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute elapsed time in seconds.
        current_ticks = pygame.time.get_ticks()
        time_elapsed = (current_ticks - start_ticks) / 1000.0

        # Get current joint positions
        joints = get_dynamic_joints(time_elapsed)

        # Clear screen to black
        screen.fill(BLACK)

        # Draw each joint as a white circle
        for joint in joint_order:
            # Some joints (like "r_hand") are computed dynamically.
            if joint in joints:
                pos = joints[joint]
                pygame.draw.circle(screen, WHITE, (int(pos[0]), int(pos[1])), point_radius)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()