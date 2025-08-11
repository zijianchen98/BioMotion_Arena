#!/usr/bin/env python3

import pygame
import math
import sys

# Window dimensions
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Number of points for the biological motion
NUM_POINTS = 15

# Walking cycle duration (in seconds) and stride parameters
CYCLE_TIME = 1.5  # shorter or longer for faster/slower walk
AMPLITUDE = 0.3   # leg swing amplitude
ARM_AMP = 0.2     # arm swing amplitude
TORSO_LEAN = 0.2  # forward lean to simulate carrying heavy weight
VERTICAL_BOB = 0.05  # vertical displacement to imitate walking bounce

# Scale factor for drawing
SCALE = 150
# Center offset so that the figure is roughly centered
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2 + 50

def get_joint_positions(t):
    """
    Returns a list of (x, y) tuples for 15 key points of a walking figure
    at time t, representing a 'happy man with heavy weight' walking.
    """
    # Phase in [0, 2*pi) for one cycle
    phase = (t * 2 * math.pi) / CYCLE_TIME

    # Basic angles for legs (left leg out of phase with right)
    left_leg_angle = AMPLITUDE * math.sin(phase)
    right_leg_angle = AMPLITUDE * math.sin(phase + math.pi)

    # Arms out of phase with legs, but smaller amplitude
    left_arm_angle = ARM_AMP * math.sin(phase + math.pi)
    right_arm_angle = ARM_AMP * math.sin(phase)

    # Vertical torso bob
    torso_bob = VERTICAL_BOB * math.sin(phase * 2)

    # Torso lean forward
    # We'll treat it as a small horizontal offset for upper body
    torso_lean = TORSO_LEAN

    # Body segment lengths (arbitrary but consistent)
    head_height = 0.2
    torso_length = 0.3
    arm_length_upper = 0.18
    arm_length_lower = 0.18
    leg_length_upper = 0.25
    leg_length_lower = 0.25

    # Root (pelvis) coordinates
    root_x = 0
    root_y = 0 + torso_bob

    # Torso coordinates
    # We'll define a top-of-torso point and a bottom-of-torso (root) point
    # Then the head on top
    # The torso is leaning forward
    torso_top_x = root_x + torso_lean
    torso_top_y = root_y + torso_length

    # Head point
    head_x = torso_top_x + torso_lean
    head_y = torso_top_y + head_height

    # Shoulders: We'll place shoulders near the top of the torso
    left_shoulder_x = torso_top_x + torso_lean * 0.5
    left_shoulder_y = torso_top_y
    right_shoulder_x = torso_top_x + torso_lean * 0.5
    right_shoulder_y = torso_top_y

    # Hips: We'll treat the root as the midpoint (pelvis)
    left_hip_x = root_x - 0.05
    left_hip_y = root_y
    right_hip_x = root_x + 0.05
    right_hip_y = root_y

    # Arms:
    # We'll rotate arms from the shoulder pivot
    # For a heavy weight, arms might be in front. We'll approximate with angles
    # around some forward angle. Let's define "forward angle" as -45 degrees in x.
    base_arm_angle = -math.pi / 4  # arms slightly forward
    left_arm_upper_angle = base_arm_angle + left_arm_angle
    right_arm_upper_angle = base_arm_angle + right_arm_angle

    # Positions of elbows
    left_elbow_x = left_shoulder_x + arm_length_upper * math.cos(left_arm_upper_angle)
    left_elbow_y = left_shoulder_y + arm_length_upper * math.sin(left_arm_upper_angle)
    right_elbow_x = right_shoulder_x + arm_length_upper * math.cos(right_arm_upper_angle)
    right_elbow_y = right_shoulder_y + arm_length_upper * math.sin(right_arm_upper_angle)

    # Forearms angled similarly but with a slight bend
    bend_factor = 0.5
    left_forearm_angle = left_arm_upper_angle + bend_factor
    right_forearm_angle = right_arm_upper_angle + bend_factor

    # Pos of hands
    left_hand_x = left_elbow_x + arm_length_lower * math.cos(left_forearm_angle)
    left_hand_y = left_elbow_y + arm_length_lower * math.sin(left_forearm_angle)
    right_hand_x = right_elbow_x + arm_length_lower * math.cos(right_forearm_angle)
    right_hand_y = right_elbow_y + arm_length_lower * math.sin(right_forearm_angle)

    # Legs
    # We rotate from hips
    base_leg_angle = 0  # neutral is straight down
    left_leg_upper_angle = base_leg_angle + left_leg_angle
    right_leg_upper_angle = base_leg_angle + right_leg_angle

    # Knees
    left_knee_x = left_hip_x + leg_length_upper * math.sin(left_leg_upper_angle)
    left_knee_y = left_hip_y - leg_length_upper * math.cos(left_leg_upper_angle)
    right_knee_x = right_hip_x + leg_length_upper * math.sin(right_leg_upper_angle)
    right_knee_y = right_hip_y - leg_length_upper * math.cos(right_leg_upper_angle)

    # Additional bend for lower legs
    lower_leg_bend = 0.3
    left_leg_lower_angle = left_leg_upper_angle + lower_leg_bend * math.sin(phase)
    right_leg_lower_angle = right_leg_upper_angle + lower_leg_bend * math.sin(phase + math.pi)

    # Feet
    left_foot_x = left_knee_x + leg_length_lower * math.sin(left_leg_lower_angle)
    left_foot_y = left_knee_y - leg_length_lower * math.cos(left_leg_lower_angle)
    right_foot_x = right_knee_x + leg_length_lower * math.sin(right_leg_lower_angle)
    right_foot_y = right_knee_y - leg_length_lower * math.cos(right_leg_lower_angle)

    # Collect 15 key points (head, neck, shoulders, elbows, hands, torso, hips, knees, feet)
    # For clarity, let's define them in a consistent order:
    points = [
        (head_x, head_y),                # 1  Head
        (torso_top_x, torso_top_y),      # 2  Neck/Top of torso
        (left_shoulder_x, left_shoulder_y),   # 3  Left shoulder
        (right_shoulder_x, right_shoulder_y), # 4  Right shoulder
        (left_elbow_x, left_elbow_y),    # 5  Left elbow
        (right_elbow_x, right_elbow_y),  # 6  Right elbow
        (left_hand_x, left_hand_y),      # 7  Left hand
        (right_hand_x, right_hand_y),    # 8  Right hand
        (root_x, root_y),                # 9  Torso (pelvis)
        (left_hip_x, left_hip_y),        # 10 Left hip
        (right_hip_x, right_hip_y),      # 11 Right hip
        (left_knee_x, left_knee_y),      # 12 Left knee
        (right_knee_x, right_knee_y),    # 13 Right knee
        (left_foot_x, left_foot_y),      # 14 Left foot
        (right_foot_x, right_foot_y),    # 15 Right foot
    ]

    return points

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biological Motion: Happyman with Heavy Weight Walking")
    clock = pygame.time.Clock()

    start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate elapsed time in seconds
        elapsed_ms = pygame.time.get_ticks() - start_time
        t = elapsed_ms / 1000.0

        # Get point positions for this time
        points = get_joint_positions(t)

        # Clear screen
        screen.fill(BLACK)

        # Draw each point
        for (x, y) in points:
            # Convert from abstract coords to screen coords
            draw_x = CENTER_X + int(x * SCALE)
            draw_y = CENTER_Y - int(y * SCALE)
            pygame.draw.circle(screen, WHITE, (draw_x, draw_y), 5)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()