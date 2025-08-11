
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 marker names of a 'sadman' (human) in order
MARKERS = [
    'Head',
    'Neck',
    'Right Shoulder',
    'Left Shoulder',
    'Right Elbow',
    'Left Elbow',
    'Right Wrist',
    'Left Wrist',
    'Right Hip',
    'Left Hip',
    'Right Knee',
    'Left Knee',
    'Right Ankle',
    'Left Ankle',
    'Weight'
]

# Skeletal structure connections (for realism, but only points are drawn)
SKELETON = [
    (0, 1),  # Head to Neck
    (1, 2), (1, 3),  # Neck to Shoulders
    (2, 4), (3, 5),  # Shoulders to Elbows
    (4, 6), (5, 7),  # Elbows to Wrists
    (1, 8), (1, 9),  # Neck to Hips
    (8, 10), (9, 11),  # Hips to Knees
    (10, 12), (11, 13),  # Knees to Ankles
    (6, 14), (7, 14)  # Wrists to "Heavy Weight"
]

def sadman_laying_down_posture(frame, total_frames):
    """
    Returns the 15x2 array of marker positions at the specified frame.
    The figure is lying down (body horizontal), with 'straining' and 'weight' oscillating a little
    to give perception of heavy weight lifting: the wrists are up, holding the weight.

    The figure is centered horizontally and moving arms slightly up/down as if attempting to lift.
    """
    # Scale: space in pixels (for 0-1 in X and Y)
    length_unit = 0.15  # size of head/body segment in normalized units
    
    # origin (lying center)
    center_x = 0.5
    center_y = 0.45
    
    # Frequency and amplitude of  "weight movement" (tired/strained/ineffective attempts)
    T = total_frames
    t = frame
    arm_motion = 0.04 * np.sin(2 * np.pi * t / T * 1.0)        # slow up and down
    wrist_lag = 0.02 * np.sin(2 * np.pi * t / T * 1.0 + np.pi/3)
    weight_bounce = 0.03 * np.abs(np.sin(2 * np.pi * t / T * 1.0))  # only up (gravity stops downwards)
    body_sag = -0.01 * np.abs(np.sin(2 * np.pi * t / T * 0.5)) # body sags from effort

    # Positions (body is horizontal!)
    # Head-neck-shoulders-elbows-wrists sequence is along X
    head_x = center_x - 3.5 * length_unit
    head_y = center_y

    neck_x = head_x + length_unit
    neck_y = head_y + body_sag

    r_shoulder_x = neck_x + length_unit
    l_shoulder_x = neck_x + length_unit
    r_shoulder_y = neck_y - 0.05
    l_shoulder_y = neck_y + 0.05

    # Elbows offset down
    r_elbow_x = r_shoulder_x + length_unit
    l_elbow_x = l_shoulder_x + length_unit
    r_elbow_y = r_shoulder_y - 0.04 + arm_motion/2
    l_elbow_y = l_shoulder_y + 0.04 - arm_motion/2

    # Wrists forward and a bit lifted due to the weight
    r_wrist_x = r_elbow_x + length_unit
    l_wrist_x = l_elbow_x + length_unit
    r_wrist_y = r_elbow_y + 0.09 + arm_motion + wrist_lag
    l_wrist_y = l_elbow_y - 0.09 - arm_motion - wrist_lag

    # Hips and down
    r_hip_x = neck_x + 0.6 * length_unit
    l_hip_x = neck_x + 0.6 * length_unit
    r_hip_y = neck_y - 0.04
    l_hip_y = neck_y + 0.04

    r_knee_x = r_hip_x + length_unit
    l_knee_x = l_hip_x + length_unit
    knee_bend = 0.10 * np.abs(np.sin(2 * np.pi * t / T * 0.33))
    r_knee_y = r_hip_y - 0.07 - knee_bend
    l_knee_y = l_hip_y + 0.07 + knee_bend

    r_ankle_x = r_knee_x + length_unit
    l_ankle_x = l_knee_x + length_unit
    r_ankle_y = r_knee_y - 0.07
    l_ankle_y = l_knee_y + 0.07

    # Weight is above/below wrists, connecting both (moves with wrists) -- heavy object
    weight_x = (r_wrist_x + l_wrist_x) / 2
    weight_y = (r_wrist_y + l_wrist_y) / 2 + weight_bounce

    positions = np.array([
        [head_x, head_y],               # 0 Head
        [neck_x, neck_y],               # 1 Neck
        [r_shoulder_x, r_shoulder_y],   # 2 RShoulder
        [l_shoulder_x, l_shoulder_y],   # 3 LShoulder
        [r_elbow_x, r_elbow_y],         # 4 RElbow
        [l_elbow_x, l_elbow_y],         # 5 LElbow
        [r_wrist_x, r_wrist_y],         # 6 RWrist
        [l_wrist_x, l_wrist_y],         # 7 LWrist
        [r_hip_x, r_hip_y],             # 8 RHip
        [l_hip_x, l_hip_y],             # 9 LHip
        [r_knee_x, r_knee_y],           # 10 RKnee
        [l_knee_x, l_knee_y],           # 11 LKnee
        [r_ankle_x, r_ankle_y],         # 12 RAnkle
        [l_ankle_x, l_ankle_y],         # 13 LAnkle
        [weight_x, weight_y],           # 14 HeavyWeight
    ])
    return positions

# ---- Animation setup ----
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
plt.axis('off')

points, = ax.plot([], [], 'wo', markersize=10)

total_frames = 100

def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0.12, 0.87)
    points.set_data([], [])
    return points,

def animate(frame):
    coords = sadman_laying_down_posture(frame, total_frames)
    x, y = coords[:,0], coords[:,1]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(
    fig, animate, frames=total_frames, interval=38, blit=True, init_func=init, repeat=True
)

plt.show()
