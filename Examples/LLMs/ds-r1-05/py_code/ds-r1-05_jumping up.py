
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams

rcParams['font.family'] = 'monospace'

POSE_STANDING = [
    (0, 0.9),    # head
    (0, 0.7),    # shoulder_center
    (-0.2, 0.7), # shoulder_left
    (-0.2, 0.45),# elbow_left
    (-0.2, 0.2), # wrist_left
    (0.2, 0.7),  # shoulder_right
    (0.2, 0.45), # elbow_right
    (0.2, 0.2),  # wrist_right
    (0, 0),      # hip_center
    (-0.1, 0),   # hip_left
    (-0.1, -0.25),# knee_left
    (-0.1, -0.5),# ankle_left
    (0.1, 0),    # hip_right
    (0.1, -0.25),# knee_right
    (0.1, -0.5)  # ankle_right
]

POSE_CROUCH = [
    (0, 0.9),    # head
    (0, 0.7),    # shoulder_center
    (-0.2, 0.7), # shoulder_left
    (-0.3, 0.5), # elbow_left
    (-0.4, 0.5), # wrist_left
    (0.2, 0.7),  # shoulder_right
    (0.3, 0.5),  # elbow_right
    (0.4, 0.5),  # wrist_right
    (0, 0),      # hip_center
    (-0.1, 0),   # hip_left
    (-0.15, -0.15), # knee_left
    (-0.15, -0.4), # ankle_left
    (0.1, 0),    # hip_right
    (0.15, -0.15), # knee_right
    (0.15, -0.4) # ankle_right
]

POSE_UP = [
    (0, 0.9),    # head
    (0, 0.7),    # shoulder_center
    (-0.2, 0.7), # shoulder_left
    (-0.2, 0.85),# elbow_left
    (-0.2, 1.1), # wrist_left
    (0.2, 0.7),  # shoulder_right
    (0.2, 0.85), # elbow_right
    (0.2, 1.1),  # wrist_right
    (0, 0),      # hip_center
    (-0.1, 0),   # hip_left
    (-0.1, -0.25),# knee_left
    (-0.1, -0.5),# ankle_left
    (0.1, 0),    # hip_right
    (0.1, -0.25),# knee_right
    (0.1, -0.5)  # ankle_right
]

POSE_LAND = [
    (0, 0.9),    # head
    (0, 0.7),    # shoulder_center
    (-0.2, 0.7), # shoulder_left
    (-0.1, 0.5), # elbow_left
    (0, 0.5),    # wrist_left
    (0.2, 0.7),  # shoulder_right
    (0.1, 0.5),  # elbow_right
    (0, 0.5),    # wrist_right
    (0, 0),      # hip_center
    (-0.1, 0),   # hip_left
    (-0.15, -0.15), # knee_left
    (-0.15, -0.4), # ankle_left
    (0.1, 0),    # hip_right
    (0.15, -0.15), # knee_right
    (0.15, -0.4) # ankle_right
]

def interpolate_pose(pose1, pose2, weight):
    new_pose = []
    for i in range(len(pose1)):
        x1, y1 = pose1[i]
        x2, y2 = pose2[i]
        x = x1 + weight * (x2 - x1)
        y = y1 + weight * (y2 - y1)
        new_pose.append((x, y))
    return new_pose

def get_base_pose(t_mod):
    if t_mod < 24:
        weight = t_mod / 24.0
        return interpolate_pose(POSE_STANDING, POSE_CROUCH, weight)
    elif t_mod < 36:
        weight = (t_mod - 24) / 12.0
        return interpolate_pose(POSE_CROUCH, POSE_UP, weight)
    elif t_mod < 84:
        if t_mod < 60:
            return POSE_UP
        else:
            weight = (t_mod - 60) / 24.0
            return interpolate_pose(POSE_UP, POSE_LAND, min(weight, 1.0))
    else:
        if t_mod < 108:
            weight = (t_mod - 84) / 24.0
            return interpolate_pose(POSE_LAND, POSE_CROUCH, weight)
        else:
            weight = (t_mod - 108) / 12.0
            return interpolate_pose(POSE_CROUCH, POSE_STANDING, weight)

def calculate_root_y(t_mod):
    crouch_depth = 0.2
    land_crouch_depth = 0.15
    if t_mod < 24:
        return -crouch_depth * (t_mod / 24.0)
    elif t_mod < 36:
        return -crouch_depth + crouch_depth * ((t_mod - 24) / 12.0)
    elif t_mod < 84:
        t_flight = t_mod - 36
        return (4 * 0.5 * t_flight * (48 - t_flight)) / (48 * 48)
    else:
        if t_mod < 108:
            return -land_crouch_depth * ((t_mod - 84) / 24.0)
        else:
            return -land_crouch_depth + land_crouch_depth * ((t_mod - 108) / 12.0)

def update(frame):
    t_mod = frame % 120
    y_root = calculate_root_y(t_mod)
    base_pose = get_base_pose(t_mod)
    shifted_pose = [(x, y + y_root) for (x, y) in base_pose]
    x_data = [x for (x, y) in shifted_pose]
    y_data = [y for (x, y) in shifted_pose]
    scatter.set_offsets(np.c_[x_data, y_data])
    return scatter,

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

scatter = ax.scatter([], [], s=70, c='white', edgecolors='none')

ani = FuncAnimation(fig, update, frames=120, interval=33.3, blit=False, repeat=True)

plt.tight_layout()
plt.show()
