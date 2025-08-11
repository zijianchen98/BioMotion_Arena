#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# GLOBAL PARAMETERS
FPS = 30
DURATION = 2.0  # seconds for one jump cycle
FRAMES = int(FPS * DURATION)
JUMP_AMPLITUDE = 0.4  # vertical jump offset
ARM_ROTATION_AMPLITUDE = 0.6  # radians
LEG_ROTATION_AMPLITUDE = 0.4  # radians

# 15 body points (some are fixed trunk points, others are pivot-based)
# Trunk points (each will just shift vertically during the jump):
# 0: Head
# 1: Neck
# 2: Chest
# 3: Left Shoulder pivot
# 4: Right Shoulder pivot
# 5: Pelvis
# 6: Left Hip pivot
# 7: Right Hip pivot
trunk_base = np.array([
    [0.0,  0.8],   # Head
    [0.0,  0.6],   # Neck
    [0.0,  0.72],  # Chest
    [-0.2, 0.6],   # Left Shoulder pivot
    [ 0.2, 0.6],   # Right Shoulder pivot
    [0.0,  0.2],   # Pelvis
    [-0.2, 0.2],   # Left Hip pivot
    [ 0.2, 0.2],   # Right Hip pivot
])

# Arms - local coordinates relative to each shoulder pivot:
# For left arm, pivot is trunk_base[3]; right arm, pivot is trunk_base[4].
# Each arm has 2 additional points: elbow, wrist
# We'll rotate them around the pivot
left_arm_local = np.array([
    [-0.2, -0.2],  # Elbow relative to pivot
    [-0.25, -0.4], # Wrist relative to pivot
])
right_arm_local = np.array([
    [ 0.2, -0.2],  # Elbow relative to pivot
    [ 0.25, -0.4], # Wrist relative to pivot
])

# Legs - local coordinates relative to each hip pivot:
# For left leg, pivot is trunk_base[6]; right leg, pivot is trunk_base[7].
# Each leg has 2 additional points: knee, ankle
left_leg_local = np.array([
    [-0.0, -0.3],  # Knee relative to hip
    [-0.0, -0.6],  # Ankle relative to hip
])
right_leg_local = np.array([
    [ 0.0, -0.3],  # Knee relative to hip
    [ 0.0, -0.6],  # Ankle relative to hip
])

# Helper function to rotate a point (px, py) around a pivot (vx, vy) by angle (radians)
def rotate_point(px, py, vx, vy, angle):
    # Translate to origin
    tx, ty = px - vx, py - vy
    # Rotate
    rx = tx * math.cos(angle) - ty * math.sin(angle)
    ry = tx * math.sin(angle) + ty * math.cos(angle)
    # Translate back
    return rx + vx, ry + vy

def get_joint_positions(frame):
    """
    Returns an array of shape (15, 2) with the (x, y) positions
    of all 15 points for the current animation frame.
    """
    t = frame / FRAMES  # goes from 0 to 1 for each full jump cycle
    
    # Vertical jump offset (smooth sinusoidal jump)
    jump_offset = JUMP_AMPLITUDE * math.sin(2 * math.pi * t)
    
    # Arm and leg rotation angles
    arm_angle = ARM_ROTATION_AMPLITUDE * math.sin(2 * math.pi * t)
    leg_angle = LEG_ROTATION_AMPLITUDE * math.sin(2 * math.pi * t)
    
    # Shift trunk vertically
    trunk_positions = trunk_base.copy()
    trunk_positions[:, 1] += jump_offset
    
    all_points = []

    # 0: Head, 1: Neck, 2: Chest, 5: Pelvis remain as-is
    # 3: LShoulder pivot, 4: RShoulder pivot, 6: LHip pivot, 7: RHip pivot also remain
    for i in range(trunk_positions.shape[0]):
        all_points.append((trunk_positions[i, 0], trunk_positions[i, 1]))
    
    # Build arms
    # Left arm
    left_shoulder_x, left_shoulder_y = trunk_positions[3]
    rotated_left_arm = []
    for (lx, ly) in left_arm_local:
        # local coords are relative to the pivot, so pivot is (0,0) in local
        # global coords require rotation around pivot
        px, py = left_shoulder_x + lx, left_shoulder_y + ly
        rx, ry = rotate_point(px, py, left_shoulder_x, left_shoulder_y, arm_angle)
        rotated_left_arm.append((rx, ry))
    
    # Right arm
    right_shoulder_x, right_shoulder_y = trunk_positions[4]
    rotated_right_arm = []
    for (lx, ly) in right_arm_local:
        px, py = right_shoulder_x + lx, right_shoulder_y + ly
        rx, ry = rotate_point(px, py, right_shoulder_x, right_shoulder_y, -arm_angle)
        rotated_right_arm.append((rx, ry))

    # Build legs
    # Left leg
    left_hip_x, left_hip_y = trunk_positions[6]
    rotated_left_leg = []
    for (lx, ly) in left_leg_local:
        px, py = left_hip_x + lx, left_hip_y + ly
        rx, ry = rotate_point(px, py, left_hip_x, left_hip_y, -leg_angle)
        rotated_left_leg.append((rx, ry))
    
    # Right leg
    right_hip_x, right_hip_y = trunk_positions[7]
    rotated_right_leg = []
    for (lx, ly) in right_leg_local:
        px, py = right_hip_x + lx, right_hip_y + ly
        rx, ry = rotate_point(px, py, right_hip_x, right_hip_y, leg_angle)
        rotated_right_leg.append((rx, ry))
    
    # The trunk list had 8 points, we add:
    # 2 left arm points + 2 right arm points + 2 left leg points + 2 right leg points = 8 more
    # total 16 if we included all from trunk, but trunk_base has 8 points (0..7).
    # We only need 15 total. We'll drop the “Chest” or combine Neck/Chest as one.
    # Let's drop the chest from the final set for exactly 15 lights:
    # So remove trunk_positions[2] from all_points:
    del all_points[2]  # remove chest

    # now we have trunk: 7 points + arms(2+2) + legs(2+2) = 13 total
    # we actually need 15 total, so restore the chest, but let's remove something else
    # Let's keep the chest and remove Pelvis or Neck?
    # We'll keep them all except let's skip the pelvis (index 4 in the new array?) 
    # We must ensure exactly 15. Let's do this systematically:
    # trunk_positions indexes: 0=head,1=neck,2=chest,3=lshpvt,4=rshpvt,5=pelvis,6=lhip,7=rhip
    # after appending to all_points in order, we have the same indexing in all_points.
    # We want exactly 15 final points. Currently, trunk_base has 8 points, we remove 1 => 7,
    # plus arms(4) => 11, plus legs(4) => 15 total. We only needed to remove one trunk point (chest).
    # So let's finalize that. The chest is removed. Good. That yields 7 trunk + 8 limbs = 15 total.

    # Now append limbs:
    for pt in rotated_left_arm:
        all_points.append(pt)
    for pt in rotated_right_arm:
        all_points.append(pt)
    for pt in rotated_left_leg:
        all_points.append(pt)
    for pt in rotated_right_leg:
        all_points.append(pt)
    
    # Now we have exactly 15 points. Return them as an Nx2 numpy array
    return np.array(all_points)

fig, ax = plt.subplots(figsize=(5, 5), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim([-1.0, 1.0])
ax.set_ylim([-0.5, 1.5])
ax.axis('off')

scatter = ax.scatter([], [], c='white', s=50)

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    pts = get_joint_positions(frame)
    scatter.set_offsets(pts)
    return (scatter,)

ani = FuncAnimation(
    fig, update, frames=FRAMES, 
    init_func=init, blit=True, 
    interval=1000 // FPS, repeat=True
)

plt.show()