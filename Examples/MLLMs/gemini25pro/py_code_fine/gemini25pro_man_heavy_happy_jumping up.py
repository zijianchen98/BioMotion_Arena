
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Main Configuration ---
TOTAL_FRAMES = 120
FRAME_INTERVAL = 30

# --- Skeleton Structure (limb lengths) ---
PELVIS_WIDTH = 3.0
TORSO_LENGTH = 4.0
NECK_LENGTH = 1.0
HEAD_OFFSET = 1.5
SHOULDER_WIDTH = 4.0
UPPER_ARM_LENGTH = 3.0
LOWER_ARM_LENGTH = 3.0
UPPER_LEG_LENGTH = 4.5
LOWER_LEG_LENGTH = 4.5

# --- Animation Keyframes for control parameters ---
KEYFRAME_TIMES = np.array([0, 25, 40, 60, 80, 100, 120])

PELVIS_Y_KFS = np.array([9.0, 5.0, 6.0, 13.0, 6.0, 4.0, 9.0])
TORSO_ANGLE_KFS = np.deg2rad(np.array([5, 30, 10, 5, 10, 35, 5]))
THIGH_ANGLE_KFS = np.deg2rad(np.array([-5, 45, -10, 0, -10, 50, -5]))
KNEE_ANGLE_KFS = np.deg2rad(np.array([170, 80, 180, 150, 180, 75, 170]))
SHOULDER_ANGLE_KFS = np.deg2rad(np.array([20, 10, 30, 20, 30, 10, 20]))
ELBOW_ANGLE_KFS = np.deg2rad(np.array([90, 80, 90, 90, 90, 80, 90]))

def ease_in_out_sine(t):
    return -(np.cos(np.pi * t) - 1) / 2

def interpolate_params(frame):
    """Interpolates all control parameters for a given frame."""
    if frame >= KEYFRAME_TIMES[-1]:
        frame = KEYFRAME_TIMES[-1] -1
        
    segment_idx = np.where(frame < KEYFRAME_TIMES)[0][0] - 1
    start_time = KEYFRAME_TIMES[segment_idx]
    end_time = KEYFRAME_TIMES[segment_idx + 1]
    
    t = (frame - start_time) / (end_time - start_time)
    eased_t = ease_in_out_sine(t)

    params = {}
    kfs_map = {
        'pelvis_y': PELVIS_Y_KFS,
        'torso_angle': TORSO_ANGLE_KFS,
        'thigh_angle': THIGH_ANGLE_KFS,
        'knee_angle': KNEE_ANGLE_KFS,
        'shoulder_angle': SHOULDER_ANGLE_KFS,
        'elbow_angle': ELBOW_ANGLE_KFS,
    }

    for name, kfs in kfs_map.items():
        start_val = kfs[segment_idx]
        end_val = kfs[segment_idx + 1]
        params[name] = start_val + (end_val - start_val) * eased_t
        
    return params

def get_pose(params):
    """Calculates the 15 point positions using forward kinematics."""
    points = {}
    
    points['pelvis'] = np.array([0.0, params['pelvis_y']])
    torso_rotation_matrix = np.array([
        [np.cos(params['torso_angle'] - np.pi/2), -np.sin(params['torso_angle'] - np.pi/2)],
        [np.sin(params['torso_angle'] - np.pi/2),  np.cos(params['torso_angle'] - np.pi/2)]
    ])
    
    torso_vec = torso_rotation_matrix @ np.array([0, 1])
    points['neck'] = points['pelvis'] + torso_vec * TORSO_LENGTH
    points['head'] = points['neck'] + torso_vec * HEAD_OFFSET

    for side in ['left', 'right']:
        sign = -1 if side == 'left' else 1
        points[f'hip_{side}'] = points['pelvis'] + np.array([sign * PELVIS_WIDTH / 2, 0])
        
        thigh_rotation_angle = params['thigh_angle'] * sign
        thigh_vec = np.array([np.sin(thigh_rotation_angle), -np.cos(thigh_rotation_angle)])
        points[f'knee_{side}'] = points[f'hip_{side}'] + thigh_vec * UPPER_LEG_LENGTH
        
        shin_rotation_angle = thigh_rotation_angle + (np.pi - params['knee_angle']) * sign
        shin_vec = np.array([np.sin(shin_rotation_angle), -np.cos(shin_rotation_angle)])
        points[f'ankle_{side}'] = points[f'knee_{side}'] + shin_vec * LOWER_LEG_LENGTH

    for side in ['left', 'right']:
        sign = -1 if side == 'left' else 1
        points[f'shoulder_{side}'] = points['neck'] + (torso_rotation_matrix @ np.array([sign * SHOULDER_WIDTH / 2, -0.5]))
        
        upper_arm_angle = params['torso_angle'] + params['shoulder_angle'] * sign
        upper_arm_vec = np.array([np.sin(upper_arm_angle), -np.cos(upper_arm_angle)])
        points[f'elbow_{side}'] = points[f'shoulder_{side}'] + upper_arm_vec * UPPER_ARM_LENGTH
        
        lower_arm_angle = upper_arm_angle + (np.pi - params['elbow_angle']) * sign
        lower_arm_vec = np.array([np.sin(lower_arm_angle), -np.cos(lower_arm_angle)])
        points[f'wrist_{side}'] = points[f'elbow_{side}'] + lower_arm_vec * LOWER_ARM_LENGTH

    ordered_points = [
        points['head'], points['neck'],
        points['shoulder_left'], points['shoulder_right'],
        points['elbow_left'], points['elbow_right'],
        points['wrist_left'], points['wrist_right'],
        points['pelvis'],
        points['hip_left'], points['hip_right'],
        points['knee_left'], points['knee_right'],
        points['ankle_left'], points['ankle_right']
    ]
    return np.array(ordered_points)

fig, ax = plt.subplots()
fig.set_size_inches(5, 7)
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-12, 12)
ax.set_ylim(-2, 22)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

initial_params = interpolate_params(0)
initial_pose = get_pose(initial_params)
scatter = ax.scatter(initial_pose[:, 0], initial_pose[:, 1], c='white', s=70)

def animate(frame):
    params = interpolate_params(frame)
    pose = get_pose(params)
    scatter.set_offsets(pose)
    return scatter,

ani = animation.FuncAnimation(
    fig, animate, frames=TOTAL_FRAMES, interval=FRAME_INTERVAL, blit=True, repeat=True)

plt.show()
