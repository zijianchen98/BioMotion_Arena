
import pygame
import math
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biological Motion: Happy Woman Walking")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
clock = pygame.time.Clock()
FPS = 30

# Joint positions (relative to a central body)
# This is a simplified stick figure with 15 joints
# [head, neck, torso, left shoulder, left elbow, left hand,
#  right shoulder, right elbow, right hand, left hip, left knee, left foot,
#  right hip, right knee, right foot]
joint_indices = {
    'head': 0,
    'neck': 1,
    'torso': 2,
    'lshoulder': 3,
    'lelbow': 4,
    'lhand': 5,
    'rshoulder': 6,
    'relbow': 7,
    'rhand': 8,
    'lhip': 9,
    'lknee': 10,
    'lfoot': 11,
    'rhip': 12,
    'rknee': 13,
    'rfoot': 14
}

# Initial joint positions (relative to center)
joint_offsets = np.array([
    [0, -80],     # head
    [0, -40],     # neck
    [0, 0],       # torso
    [-20, 20],    # left shoulder
    [-20, 60],    # left elbow
    [-20, 100],   # left hand
    [20, 20],     # right shoulder
    [20, 60],     # right elbow
    [20, 100],    # right hand
    [-20, 40],    # left hip
    [-20, 80],    # left knee
    [-20, 120],   # left foot
    [20, 40],     # right hip
    [20, 80],     # right knee
    [20, 120],    # right foot
])

# Animation parameters
walk_speed = 0.05  # speed of walking animation
time = 0

def animate_joints(time):
    """Animate the joints to simulate walking."""
    # Base position (center of screen)
    center = np.array([WIDTH // 2, HEIGHT // 2])

    # Torso rotation based on walking (slight side-to-side sway)
    sway = 10 * math.sin(time * 0.5)
    torso_rot = math.radians(sway)

    # Walking motion: left and right legs alternate
    leg_cycle = time * walk_speed
    left_leg_angle = math.sin(leg_cycle) * 0.5
    right_leg_angle = math.sin(leg_cycle + math.pi) * 0.5

    # Arm swing: opposite of legs
    arm_cycle = time * walk_speed
    left_arm_angle = math.sin(arm_cycle + math.pi) * 0.3
    right_arm_angle = math.sin(arm_cycle) * 0.3

    animated_offsets = joint_offsets.copy()

    # Rotate arms
    animated_offsets[joint_indices['lshoulder']] = rotate_point(joint_offsets[joint_indices['lshoulder']], left_arm_angle)
    animated_offsets[joint_indices['lelbow']] = rotate_point(joint_offsets[joint_indices['lelbow']], left_arm_angle)
    animated_offsets[joint_indices['lhand']] = rotate_point(joint_offsets[joint_indices['lhand']], left_arm_angle)
    animated_offsets[joint_indices['rshoulder']] = rotate_point(joint_offsets[joint_indices['rshoulder']], right_arm_angle)
    animated_offsets[joint_indices['relbow']] = rotate_point(joint_offsets[joint_indices['relbow']], right_arm_angle)
    animated_offsets[joint_indices['rhand']] = rotate_point(joint_offsets[joint_indices['rhand']], right_arm_angle)

    # Rotate legs
    animated_offsets[joint_indices['lhip']] = rotate_point(joint_offsets[joint_indices['lhip']], left_leg_angle)
    animated_offsets[joint_indices['lknee']] = rotate_point(joint_offsets[joint_indices['lknee']], left_leg_angle)
    animated_offsets[joint_indices['lfoot']] = rotate_point(joint_offsets[joint_indices['lfoot']], left_leg_angle)
    animated_offsets[joint_indices['rhip']] = rotate_point(joint_offsets[joint_indices['rhip']], right_leg_angle)
    animated_offsets[joint_indices['rknee']] = rotate_point(joint_offsets[joint_indices['rknee']], right_leg_angle)
    animated_offsets[joint_indices['rfoot']] = rotate_point(joint_offsets[joint_indices['rfoot']], right_leg_angle)

    # Apply torso rotation
    animated_offsets = rotate_array(animated_offsets, torso_rot)

    # Translate to screen center
    animated_offsets += center

    return animated_offsets

def rotate_point(point, angle):
    """Rotate a point around the origin."""
    x, y = point
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return np.array([x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta])

def rotate_array(points, angle):
    """Rotate an array of points around the origin."""
    return np.array([rotate_point(p, angle) for p in points])

def draw_point_light(joints):
    """Draw the point-light stimulus."""
    for joint in joints:
        x, y = map(int, joint)
        pygame.draw.circle(screen, WHITE, (x, y), 4)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Animate and draw
    joints = animate_joint_positions(time)
    draw_point_light(joints)

    # Update display
    pygame.display.flip()

    # Update time
    time += 1
    clock.tick(FPS)

pygame.quit()
sys.exit()
