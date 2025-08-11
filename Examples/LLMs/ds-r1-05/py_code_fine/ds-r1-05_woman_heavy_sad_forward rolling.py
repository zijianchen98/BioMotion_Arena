
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import CubicSpline

# Define key poses
keyframes = [0, 30, 60, 90, 120, 150]  # Frame indices
n_points = 15
n_keyframes = len(keyframes)

# Standing pose
standing = np.array([
    [0.0, 1.7],    # head
    [0.0, 1.5],    # neck
    [-0.4, 1.5],   # left shoulder
    [0.4, 1.5],    # right shoulder
    [-0.5, 1.2],   # left elbow
    [0.5, 1.2],    # right elbow
    [-0.6, 0.9],   # left wrist
    [0.6, 0.9],    # right wrist
    [0.0, 1.2],    # torso
    [-0.3, 0.9],   # left hip
    [0.3, 0.9],    # right hip
    [-0.3, 0.5],   # left knee
    [0.3, 0.5],    # right knee
    [-0.3, 0.1],   # left ankle
    [0.3, 0.1]     # right ankle
])

# Crouching pose
crouching = np.array([
    [0.0, 1.3],    # head
    [0.0, 1.2],    # neck
    [-0.3, 1.2],   # left shoulder
    [0.3, 1.2],    # right shoulder
    [-0.3, 0.9],   # left elbow
    [0.3, 0.9],    # right elbow
    [-0.3, 0.6],   # left wrist
    [0.3, 0.6],    # right wrist
    [0.0, 1.0],    # torso
    [-0.2, 1.0],   # left hip
    [0.2, 1.0],    # right hip
    [-0.2, 0.4],   # left knee
    [0.2, 0.4],    # right knee
    [-0.2, 0.1],   # left ankle
    [0.2, 0.1]     # right ankle
])

# Tuck pose (initiate roll)
tuck = np.array([
    [0.2, 0.6],    # head
    [0.2, 0.7],    # neck
    [-0.1, 0.7],   # left shoulder
    [0.5, 0.7],    # right shoulder
    [-0.2, 0.4],   # left elbow
    [0.4, 0.4],    # right elbow
    [-0.2, 0.0],   # left wrist
    [0.4, 0.0],    # right wrist
    [0.2, 0.5],    # torso
    [-0.1, 0.6],   # left hip
    [0.5, 0.6],    # right hip
    [-0.1, 0.3],   # left knee
    [0.5, 0.3],    # right knee
    [-0.1, 0.1],   # left ankle
    [0.5, 0.1]     # right ankle
])

# Mid roll pose (rolling)
mid_roll = np.array([
    [1.0, 0.3],    # head
    [1.0, 0.4],    # neck
    [0.7, 0.5],    # left shoulder
    [1.3, 0.5],    # right shoulder
    [0.6, 0.7],    # left elbow
    [1.2, 0.7],    # right elbow
    [0.5, 0.9],    # left wrist
    [1.1, 0.9],    # right wrist
    [1.0, 0.6],    # torso
    [0.7, 0.6],    # left hip
    [1.3, 0.6],    # right hip
    [0.7, 0.2],    # left knee
    [1.3, 0.2],    # right knee
    [0.7, 0.0],    # left ankle
    [1.3, 0.0]     # right ankle
])

# End roll pose (finishing roll)
end_roll = np.array([
    [1.7, 0.6],    # head
    [1.7, 0.7],    # neck
    [1.4, 0.7],    # left shoulder
    [2.0, 0.7],    # right shoulder
    [1.3, 0.4],    # left elbow
    [1.9, 0.4],    # right elbow
    [1.2, 0.1],    # left wrist
    [1.8, 0.1],    # right wrist
    [1.7, 0.5],    # torso
    [1.4, 0.6],    # left hip
    [2.0, 0.6],    # right hip
    [1.4, 0.3],    # left knee
    [2.0, 0.3],    # right knee
    [1.4, 0.1],    # left ankle
    [2.0, 0.1]     # right ankle
])

# Standing again (final pose)
standing_again = standing + np.array([2.0, 0.0])  # Shifted forward

# Combine poses into keyframes array
keyframe_poses = np.array([standing, crouching, tuck, mid_roll, end_roll, standing_again])
all_frames = 180
frames = np.zeros((all_frames, n_points, 2))

# Interpolate using cubic spline
for i in range(n_points):
    for coord in [0, 1]:  # x and y coordinates
        x = np.array(keyframes)
        y = keyframe_poses[:, i, coord]
        cs = CubicSpline(x, y)
        x_new = np.arange(all_frames)
        y_interp = cs(x_new)
        frames[:, i, coord] = y_interp

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.set_xlim(-1, 3)
ax.set_ylim(-0.1, 2.0)
point_plot, = ax.plot([], [], 'wo', markersize=8, alpha=0.8)

def init():
    point_plot.set_data([], [])
    return (point_plot,)

def update(frame):
    x = frames[frame, :, 0]
    y = frames[frame, :, 1]
    point_plot.set_data(x, y)
    return (point_plot,)

ani = FuncAnimation(fig, update, frames=all_frames, init_func=init, 
                   blit=True, interval=1000/60)
plt.title('Biological Motion: Forward Roll')
plt.axis('off')
plt.show()
