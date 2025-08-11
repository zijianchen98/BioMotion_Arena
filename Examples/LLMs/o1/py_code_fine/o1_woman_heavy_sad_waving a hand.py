import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
NUM_POINTS = 15

fig = plt.figure(figsize=(6,6), facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot for the 15 white points
scatter = ax.scatter([], [], c='white', s=50)

def get_points(t):
    """
    Returns an array of shape (15, 2) representing
    the (x, y) positions of the 15 point-lights at time t.
    """

    # Base posture (stooped/sad stance) in neutral positions:
    # Indices: [Head, Neck, RightShoulder, RightElbow, RightWrist,
    #           LeftShoulder, LeftElbow, LeftWrist,
    #           RightHip, RightKnee, RightAnkle,
    #           LeftHip, LeftKnee, LeftAnkle, TorsoCenter]

    base_positions = np.array([
        [ 0.0,  1.6],   # Head
        [ 0.0,  1.2],   # Neck
        [ 0.3,  1.2],   # Right Shoulder
        [ 0.5,  0.8],   # Right Elbow
        [ 0.6,  0.5],   # Right Wrist
        [-0.3,  1.2],   # Left Shoulder
        [-0.5,  0.8],   # Left Elbow
        [-0.6,  0.5],   # Left Wrist
        [ 0.2,  0.4],   # Right Hip
        [ 0.2, -0.4],   # Right Knee
        [ 0.2, -1.0],   # Right Ankle
        [-0.2,  0.4],   # Left Hip
        [-0.2, -0.4],   # Left Knee
        [-0.2, -1.0],   # Left Ankle
        [ 0.0,  0.8],   # Torso Center
    ])

    # Simulate a bounce to convey a "heavy" stance
    bounce = 0.05 * np.sin(t)
    base_positions[:, 1] += bounce

    # Slight forward stoop to appear "sad"
    stoop_angle = np.radians(10)
    cos_a, sin_a = np.cos(stoop_angle), np.sin(stoop_angle)
    # Rotate points around the hips (approx y=0.4) to stoop forward
    pivot_y = 0.4
    base_positions[:, 1] -= pivot_y
    rot_x = base_positions[:, 0]*cos_a - base_positions[:, 1]*sin_a
    rot_y = base_positions[:, 0]*sin_a + base_positions[:, 1]*cos_a
    base_positions = np.column_stack([rot_x, rot_y + pivot_y])

    # Animate waving of the right arm:
    # We'll rotate elbow & wrist about the shoulder
    shoulder_idx, elbow_idx, wrist_idx = 2, 3, 4
    shoulder = base_positions[shoulder_idx].copy()
    wave_angle = 0.3 * np.sin(2.0 * t)  # wave motion
    for idx in [elbow_idx, wrist_idx]:
        rel = base_positions[idx] - shoulder
        c, s = np.cos(wave_angle), np.sin(wave_angle)
        rx = rel[0]*c - rel[1]*s
        ry = rel[0]*s + rel[1]*c
        base_positions[idx] = shoulder + [rx, ry]

    return base_positions

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    points = get_points(frame * 0.1)
    scatter.set_offsets(points)
    return scatter,

ani = FuncAnimation(
    fig, update, frames=200, init_func=init, interval=50, blit=True
)

plt.show()