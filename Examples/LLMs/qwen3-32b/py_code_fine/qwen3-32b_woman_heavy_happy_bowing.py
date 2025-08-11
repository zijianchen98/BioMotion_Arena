
import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point-Light Biological Motion: Happy Woman Bowing with Heavy Weight")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Joint indices for clarity
JOINTS = [
    'pelvis', 'spine', 'chest', 'neck', 'head',
    'left_clavicle', 'left_shoulder', 'left_elbow', 'left_wrist',
    'right_clavicle', 'right_shoulder', 'right_elbow', 'right_wrist',
    'left_hip', 'left_knee', 'left_ankle',
    'right_hip', 'right_knee', 'right_ankle'
]

# Initial joint positions (simplified skeleton)
positions = {
    'pelvis': [400, 300],
    'spine': [400, 280],
    'chest': [400, 260],
    'neck': [400, 240],
    'head': [400, 220],
    'left_clavicle': [380, 260],
    'left_shoulder': [360, 260],
    'left_elbow': [340, 280],
    'left_wrist': [330, 300],
    'right_clavicle': [420, 260],
    'right_shoulder': [440, 260],
    'right_elbow': [460, 280],
    'right_wrist': [470, 300],
    'left_hip': [380, 300],
    'left_knee': [360, 340],
    'left_ankle': [350, 380],
    'right_hip': [420, 300],
    'right_knee': [440, 340],
    'right_ankle': [450, 380]
}

# Convert to a list for easier manipulation
joint_list = [positions[joint] for joint in JOINTS]

# Animation parameters
bowing = False
bow_frame = 0
max_bow_frame = 60
bow_depth = 40  # how much head and chest lower during bow
head_weight = 1.5  # exaggerate head movement for the heavy weight
arm_swing = 20  # how much arms swing during bow

def update_bow_animation(frame):
    if frame < max_bow_frame:
        # Bowing down
        progress = frame / max_bow_frame
        head_y = positions['head'][1] - bow_depth * head_weight * progress
        chest_y = positions['chest'][1] - bow_depth * progress
        neck_y = positions['neck'][1] - bow_depth * progress
        spine_y = positions['spine'][1] - bow_depth * progress
        pelvis_y = positions['pelvis'][1] + bow_depth * 0.2 * progress
        left_wrist_y = positions['left_wrist'][1] + arm_swing * progress
        right_wrist_y = positions['right_wrist'][1] + arm_swing * progress
    else:
        # Return to original position
        progress = (frame - max_bow_frame) / max_bow_frame
        head_y = positions['head'][1] - bow_depth * head_weight * (1 - progress)
        chest_y = positions['chest'][1] - bow_depth * (1 - progress)
        neck_y = positions['neck'][1] - bow_depth * (1 - progress)
        spine_y = positions['spine'][1] - bow_depth * (1 - progress)
        pelvis_y = positions['pelvis'][1] + bow_depth * 0.2 * (1 - progress)
        left_wrist_y = positions['left_wrist'][1] + arm_swing * (1 - progress)
        right_wrist_y = positions['right_wrist'][1] + arm_swing * (1 - progress)

    # Update joint positions
    positions['head'][1] = head_y
    positions['chest'][1] = chest_y
    positions['neck'][1] = neck_y
    positions['spine'][1] = spine_y
    positions['pelvis'][1] = pelvis_y
    positions['left_wrist'][1] = left_wrist_y
    positions['right_wrist'][1] = right_wrist_y

def draw_joints(joints):
    for joint in joints:
        x, y = int(joint[0]), int(joint[1])
        pygame.draw.circle(screen, WHITE, (x, y), 5)

# Main loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animation control
    if not bowing:
        bowing = True
        bow_frame = 0
    else:
        bow_frame += 1

    if bow_frame >= 2 * max_bow_frame:
        bowing = False
        bow_frame = 0

    update_bow_animation(bow_frame)
    draw_joints(joint_list)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
