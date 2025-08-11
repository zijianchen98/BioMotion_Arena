
"""
A Python program using pygame to show a point‐light stimulus animation of a “happyman with heavy weight” 
jumping forward. The animation shows a 15‐point stick‐figure (white point‐lights on a black background) whose 
limb movements are manipulated to roughly simulate a biomechanically plausible jump. 

Press ESC or close the window to exit.
"""

import math
import sys
import pygame

# Initialize pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Point-light Biological Motion: Heavy Jump")
clock = pygame.time.Clock()

# ---------------------------------------------------------------
# Helper function: rotate a 2D vector by angle theta (radians)
def rotate_vector(vec, theta):
    (x, y) = vec
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return (x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta)

# ---------------------------------------------------------------
# Define the base skeleton in a local coordinate system
# Coordinates are given relative to the pelvis (joint index 10 set at (0,0)).
#
# Joint index mapping:
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Wrist
# 6: Right Wrist
# 7: Mid-Spine
# 8: Left Hip
# 9: Right Hip
#10: Pelvis (reference)
#11: Left Knee
#12: Right Knee
#13: Left Ankle
#14: Right Ankle
#
# The coordinates are chosen so that the figure is roughly proportioned.
base_joints = [
    (0, -70),      # 0 Head
    (-15, -40),    # 1 Left Shoulder
    (15, -40),     # 2 Right Shoulder
    (-30, -40),    # 3 Left Elbow (base vector from left shoulder is (-15,0))
    (30, -40),     # 4 Right Elbow (base vector from right shoulder is (15,0))
    (-40, -20),    # 5 Left Wrist (base from left elbow: (-10,20))
    (40, -20),     # 6 Right Wrist (base from right elbow: (10,20))
    (0, -30),      # 7 Mid-Spine
    (-15, 10),     # 8 Left Hip
    (15, 10),      # 9 Right Hip
    (0, 0),        #10 Pelvis (reference)
    (-15, 40),     #11 Left Knee (base from left hip: (0,30))
    (15, 40),      #12 Right Knee (base from right hip: (0,30))
    (-15, 70),     #13 Left Ankle (base from left knee: (0,30))
    (15, 70)       #14 Right Ankle (base from right knee: (0,30))
]

# Groups for limbs that will have joint rotations to simulate limb swing.
# For arms: we rotate about the shoulder joints.
left_arm = {'shoulder': 1, 'elbow': 3, 'wrist': 5}
right_arm = {'shoulder': 2, 'elbow': 4, 'wrist': 6}
# For legs: we rotate about the hip joints.
left_leg = {'hip': 8, 'knee': 11, 'ankle': 13}
right_leg = {'hip': 9, 'knee': 12, 'ankle': 14}

# Global parameters for jump:
total_frames = 120         # Duration of animation (frames)
jump_distance = 200        # Horizontal displacement (pixels)
max_jump = 100             # Maximum vertical jump "lift" (pixels)
# Global origin: We'll place the pelvis of the figure initially at (300, 250)
global_origin = (300, 250)

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
point_radius = 4  # Radius for each white point-light

# Main animation loop variables
frame = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear screen to black background.
    screen.fill(BLACK)

    # Compute normalized time t in [0,1]
    t = frame / total_frames
    # Compute global offsets for jump (parabolic vertical displacement, linear horizontal)
    jump_offset_x = t * jump_distance
    # Use a parabolic curve: at t=0 and t=1, offset=0; at t=0.5, offset = -max_jump (upwards)
    jump_offset_y = - max_jump * (4 * t * (1 - t))
    
    # Determine limb rotation angles that simulate swinging.
    # Arms: swing upward slightly during the jump. Use sinusoidal modulation.
    theta_arm = math.radians(-30 * math.sin(math.pi * t))
    # Legs: swing outward slightly for push-off. 
    theta_leg = math.radians(30 * math.sin(math.pi * t))
    
    # Make a working copy of the joints for this frame.
    # We start with the base skeleton positions.
    joints = [pt for pt in base_joints]

    # ------------------------------
    # Update Arms with rotation about the shoulder.
    # Left Arm:
    shoulder_idx = left_arm['shoulder']
    elbow_idx = left_arm['elbow']
    wrist_idx = left_arm['wrist']
    shoulder_pos = joints[shoulder_idx]
    # Compute new elbow: rotate (elbow - shoulder)
    vec_elbow = (joints[elbow_idx][0] - shoulder_pos[0],
                 joints[elbow_idx][1] - shoulder_pos[1])
    new_elbow = (shoulder_pos[0] + rotate_vector(vec_elbow, theta_arm)[0],
                 shoulder_pos[1] + rotate_vector(vec_elbow, theta_arm)[1])
    joints[elbow_idx] = new_elbow
    # For wrist: compute relative vector from original elbow to wrist, then rotate and add to new elbow.
    vec_wrist = (joints[wrist_idx][0] - base_joints[elbow_idx][0],
                 joints[wrist_idx][1] - base_joints[elbow_idx][1])
    new_wrist = (new_elbow[0] + rotate_vector(vec_wrist, theta_arm)[0],
                 new_elbow[1] + rotate_vector(vec_wrist, theta_arm)[1])
    joints[wrist_idx] = new_wrist

    # Right Arm:
    shoulder_idx = right_arm['shoulder']
    elbow_idx = right_arm['elbow']
    wrist_idx = right_arm['wrist']
    shoulder_pos = joints[shoulder_idx]
    vec_elbow = (joints[elbow_idx][0] - shoulder_pos[0],
                 joints[elbow_idx][1] - shoulder_pos[1])
    new_elbow = (shoulder_pos[0] + rotate_vector(vec_elbow, theta_arm)[0],
                 shoulder_pos[1] + rotate_vector(vec_elbow, theta_arm)[1])
    joints[elbow_idx] = new_elbow
    vec_wrist = (joints[wrist_idx][0] - base_joints[elbow_idx][0],
                 joints[wrist_idx][1] - base_joints[elbow_idx][1])
    new_wrist = (new_elbow[0] + rotate_vector(vec_wrist, theta_arm)[0],
                 new_elbow[1] + rotate_vector(vec_wrist, theta_arm)[1])
    joints[wrist_idx] = new_wrist

    # ------------------------------
    # Update Legs with rotation about the hip.
    # Left Leg:
    hip_idx = left_leg['hip']
    knee_idx = left_leg['knee']
    ankle_idx = left_leg['ankle']
    hip_pos = joints[hip_idx]
    vec_knee = (joints[knee_idx][0] - hip_pos[0],
                joints[knee_idx][1] - hip_pos[1])
    new_knee = (hip_pos[0] + rotate_vector(vec_knee, theta_leg)[0],
                hip_pos[1] + rotate_vector(vec_knee, theta_leg)[1])
    joints[knee_idx] = new_knee
    vec_ankle = (joints[ankle_idx][0] - base_joints[knee_idx][0],
                 joints[ankle_idx][1] - base_joints[knee_idx][1])
    new_ankle = (new_knee[0] + rotate_vector(vec_ankle, theta_leg)[0],
                 new_knee[1] + rotate_vector(vec_ankle, theta_leg)[1])
    joints[ankle_idx] = new_ankle

    # Right Leg:
    hip_idx = right_leg['hip']
    knee_idx = right_leg['knee']
    ankle_idx = right_leg['ankle']
    hip_pos = joints[hip_idx]
    vec_knee = (joints[knee_idx][0] - hip_pos[0],
                joints[knee_idx][1] - hip_pos[1])
    new_knee = (hip_pos[0] + rotate_vector(vec_knee, theta_leg)[0],
                hip_pos[1] + rotate_vector(vec_knee, theta_leg)[1])
    joints[knee_idx] = new_knee
    vec_ankle = (joints[ankle_idx][0] - base_joints[knee_idx][0],
                 joints[ankle_idx][1] - base_joints[knee_idx][1])
    new_ankle = (new_knee[0] + rotate_vector(vec_ankle, theta_leg)[0],
                 new_knee[1] + rotate_vector(vec_ankle, theta_leg)[1])
    joints[ankle_idx] = new_ankle

    # ------------------------------
    # Apply global transformation: add global_origin and jump offsets.
    # Each joint's final position = global_origin + (local position) + (jump_offset).
    transformed_joints = []
    for (x, y) in joints:
        global_x = global_origin[0] + x + jump_offset_x
        global_y = global_origin[1] + y + jump_offset_y
        transformed_joints.append((int(global_x), int(global_y)))

    # Draw each joint as a white circle.
    for pos in transformed_joints:
        pygame.draw.circle(screen, WHITE, pos, point_radius)

    pygame.display.flip()
    clock.tick(60)  # Aim for 60 frames per second

    frame += 1
    if frame > total_frames:
        # After completing the jump, hold the last frame for a moment then exit.
        pygame.time.wait(1000)
        running = False

pygame.quit()
sys.exit()