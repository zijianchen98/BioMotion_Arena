
"""
This program uses pygame to animate a point‐light display of a “happy, light‐weight woman” running.
The figure is represented by exactly 15 white dots against a black background.
The dots correspond to (in order):
  0: Head
  1: Left Shoulder
  2: Right Shoulder
  3: Left Elbow
  4: Right Elbow
  5: Left Hand
  6: Right Hand
  7: Torso (upper body center)
  8: Pelvis (lower torso)
  9: Left Hip
 10: Right Hip
 11: Left Knee
 12: Right Knee
 13: Left Ankle
 14: Right Ankle

The running motion is created by cyclically varying the angles of the arms and legs.
The arms swing in opposite phase to the legs so that the left arm swings forward when the right leg swings forward, and vice‐versa.
The kinematics are simplified but provide a biologically plausible, smooth, and coherent running movement.
"""

import sys
import math
import pygame

# Initialize pygame and set up the display
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-Light Biological Motion: Running Woman")
clock = pygame.time.Clock()

# Colors and drawing parameters
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
point_radius = 4  # radius for each point light

# Figure geometry (in pixels) relative to a local coordinate system with origin at the torso center.
# Define fixed offsets for many markers.
head_offset = (0, -40)             # head relative to torso
shoulder_offset_left = (-15, -10)
shoulder_offset_right = (15, -10)
torso = (0, 0)                     # reference
pelvis_offset = (0, 20)            # pelvis relative to torso

hip_offset_left = (-10, 0)
hip_offset_right = (10, 0)

# Limb segment lengths
upper_arm_length = 15
forearm_length = 15
thigh_length = 30
lower_leg_length = 30

# Running cycle parameters
cycle_period = 1.0  # seconds for one cycle
# Swing amplitude (in radians)
arm_swing_amp = 0.5
leg_swing_amp = 0.5

# Center of animation on the screen (we keep it fixed here)
center_x = screen_width // 2
center_y = screen_height // 2

def get_point_coordinates(t):
    """
    Compute and return the coordinates (list of (x,y) tuples) for the 15 point lights
    at time t (in seconds). The positions are computed relative to a figure-centered
    coordinate system, then shifted to the center of the screen.
    """
    # Compute the phase of the cycle
    phase = 2 * math.pi * (t % cycle_period) / cycle_period

    # ---------------------------
    # Torso, Head, Shoulders, and Pelvis (static relative positions)
    # ---------------------------
    torso_pos = (torso[0], torso[1])
    head_pos = (torso[0] + head_offset[0], torso[1] + head_offset[1])
    left_shoulder = (torso[0] + shoulder_offset_left[0], torso[1] + shoulder_offset_left[1])
    right_shoulder = (torso[0] + shoulder_offset_right[0], torso[1] + shoulder_offset_right[1])
    pelvis = (torso[0] + pelvis_offset[0], torso[1] + pelvis_offset[1])
    left_hip = (pelvis[0] + hip_offset_left[0], pelvis[1] + hip_offset_left[1])
    right_hip = (pelvis[0] + hip_offset_right[0], pelvis[1] + hip_offset_right[1])

    # ---------------------------
    # Arms Motion: Upper arm and forearm.
    # Left arm swings with phase 'phase'; right arm with phase shifted by pi.
    # Angles measured in radians. Angle 0 is pointing straight down.
    # For arms we want them to swing in a forward-backward pattern.
    # We'll define the “rest pose” of the arm as pointing diagonally downwards outward.
    # ---------------------------
    # Left arm: rest angle ~ -45° (i.e. -pi/4) then add swing
    left_arm_angle = -math.pi/4 + arm_swing_amp * math.sin(phase)
    # Right arm: rest angle ~ -135° (i.e. -3*pi/4) then add swing (opposite phase)
    right_arm_angle = -3*math.pi/4 + arm_swing_amp * math.sin(phase + math.pi)

    # Compute left elbow and hand positions
    left_elbow = (left_shoulder[0] + upper_arm_length * math.sin(left_arm_angle),
                  left_shoulder[1] + upper_arm_length * math.cos(left_arm_angle))
    left_hand = (left_elbow[0] + forearm_length * math.sin(left_arm_angle),
                 left_elbow[1] + forearm_length * math.cos(left_arm_angle))
    # Compute right elbow and hand positions
    right_elbow = (right_shoulder[0] + upper_arm_length * math.sin(right_arm_angle),
                   right_shoulder[1] + upper_arm_length * math.cos(right_arm_angle))
    right_hand = (right_elbow[0] + forearm_length * math.sin(right_arm_angle),
                  right_elbow[1] + forearm_length * math.cos(right_arm_angle))

    # ---------------------------
    # Legs Motion: Thigh and lower leg.
    # Legs swing about the hip joint. In running, one leg swings forward while the other swings back.
    # We use a sine function for thigh rotation and add a small fixed bend for the lower leg.
    # Angle 0 (for legs) is taken as pointing straight down.
    # ---------------------------
    # Left leg uses phase "phase", right leg is offset by pi.
    left_thigh_angle = 0 + leg_swing_amp * math.sin(phase)
    right_thigh_angle = 0 + leg_swing_amp * math.sin(phase + math.pi)
    # For the lower leg, we simulate a bend at the knee by adding a small offset.
    # When the leg is in the swing phase (sine positive), the knee bends forward (add positive offset),
    # otherwise, it is more extended.
    left_knee_bend = 0.3 if math.sin(phase) > 0 else -0.3
    right_knee_bend = 0.3 if math.sin(phase + math.pi) > 0 else -0.3

    # Left knee position from left hip
    left_knee = (left_hip[0] + thigh_length * math.sin(left_thigh_angle),
                 left_hip[1] + thigh_length * math.cos(left_thigh_angle))
    # Left ankle position from left knee using lower leg with the knee bend applied
    left_lower_leg_angle = left_thigh_angle + left_knee_bend
    left_ankle = (left_knee[0] + lower_leg_length * math.sin(left_lower_leg_angle),
                  left_knee[1] + lower_leg_length * math.cos(left_lower_leg_angle))

    # Right knee position from right hip
    right_knee = (right_hip[0] + thigh_length * math.sin(right_thigh_angle),
                  right_hip[1] + thigh_length * math.cos(right_thigh_angle))
    # Right ankle position from right knee using lower leg with the knee bend applied
    right_lower_leg_angle = right_thigh_angle + right_knee_bend
    right_ankle = (right_knee[0] + lower_leg_length * math.sin(right_lower_leg_angle),
                   right_knee[1] + lower_leg_length * math.cos(right_lower_leg_angle))

    # Assemble the 15 points in the required order:
    points = [
        head_pos,          # 0: Head
        left_shoulder,     # 1: Left Shoulder
        right_shoulder,    # 2: Right Shoulder
        left_elbow,        # 3: Left Elbow
        right_elbow,       # 4: Right Elbow
        left_hand,         # 5: Left Hand
        right_hand,        # 6: Right Hand
        torso_pos,         # 7: Torso (upper body center)
        pelvis,            # 8: Pelvis (lower torso)
        left_hip,          # 9: Left Hip
        right_hip,         # 10: Right Hip
        left_knee,         # 11: Left Knee
        right_knee,        # 12: Right Knee
        left_ankle,        # 13: Left Ankle
        right_ankle        # 14: Right Ankle
    ]

    # Shift all points so that the figure is centered on the screen.
    shifted_points = []
    for (x, y) in points:
        # In our model, y increases downward.
        shifted_points.append((int(x + center_x), int(y + center_y)))
    return shifted_points

def main():
    t_start = pygame.time.get_ticks() / 1000.0  # seconds
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute elapsed time
        t_current = pygame.time.get_ticks() / 1000.0
        t = t_current - t_start

        # Get updated point positions
        points = get_point_coordinates(t)

        # Clear screen
        screen.fill(BLACK)

        # Draw each point light as a small circle
        for point in points:
            pygame.draw.circle(screen, WHITE, point, point_radius)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()