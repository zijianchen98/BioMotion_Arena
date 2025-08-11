import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 keypoints for "sadwoman" standing posture (slightly slumped).
stand_positions = np.array([
    [ 0.0, 1.6],  # Head
    [ 0.2, 1.4],  # RShoulder
    [ 0.4, 1.2],  # RElbow
    [ 0.5, 1.0],  # RWrist
    [-0.2, 1.4],  # LShoulder
    [-0.4, 1.2],  # LElbow
    [-0.5, 1.0],  # LWrist
    [ 0.0, 1.3],  # Chest
    [ 0.0, 1.0],  # Pelvis
    [ 0.1, 1.0],  # RHip
    [ 0.1, 0.6],  # RKnee
    [ 0.1, 0.2],  # RAnkle
    [-0.1, 1.0],  # LHip
    [-0.1, 0.6],  # LKnee
    [-0.1, 0.2],  # LAnkle
])

# Define 15 keypoints for "sadwoman" sitting posture.
sit_positions = np.array([
    [ 0.0, 1.1],  # Head
    [ 0.2, 0.8],  # RShoulder
    [ 0.4, 0.7],  # RElbow
    [ 0.5, 0.6],  # RWrist
    [-0.2, 0.8],  # LShoulder
    [-0.4, 0.7],  # LElbow
    [-0.5, 0.6],  # LWrist
    [ 0.0, 0.75], # Chest
    [ 0.0, 0.6],  # Pelvis
    [ 0.1, 0.6],  # RHip
    [ 0.1, 0.4],  # RKnee
    [ 0.1, 0.2],  # RAnkle
    [-0.1, 0.6],  # LHip
    [-0.1, 0.4],  # LKnee
    [-0.1, 0.2],  # LAnkle
])

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim([-1.0, 1.0])
ax.set_ylim([0.0, 2.0])
ax.axis('off')

# Scatter plot to hold the point-lights (white dots).
scatter = ax.scatter([], [], c='white', s=40)

# Total frames in one full cycle (stand -> sit -> stand).
num_frames = 60

def interpolate_positions(t):
    """
    Interpolate between stand_positions and sit_positions with parameter t in [0,1].
    t=0 -> fully standing, t=1 -> fully sitting.
    """
    return (1 - t) * stand_positions + t * sit_positions

def init():
    # Initialize scatter with no data.
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # We move from standing to sitting in first half, then back up in second half.
    half = num_frames // 2
    if frame < half:
        t = frame / float(half)
    else:
        t = 1.0 - (frame - half) / float(half)
    new_positions = interpolate_positions(t)
    scatter.set_offsets(new_positions)
    return (scatter,)

ani = animation.FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50, repeat=True
)

plt.show()