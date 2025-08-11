
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial points for the point-light stimulus
points = np.array([
    [0, 1.7, 0],  # head
    [0, 1.6, 0],  # neck
    [-0.2, 1.5, 0.1],  # left shoulder
    [0.2, 1.5, 0.1],  # right shoulder
    [-0.4, 1.3, 0.1],  # left elbow
    [0.4, 1.3, 0.1],  # right elbow
    [-0.6, 1.1, 0.1],  # left wrist
    [0.6, 1.1, 0.1],  # right wrist
    [0, 1.2, 0],  # torso center
    [-0.1, 1.0, -0.1],  # left hip
    [0.1, 1.0, -0.1],  # right hip
    [-0.1, 0.7, -0.1],  # left knee
    [0.1, 0.7, -0.1],  # right knee
    [-0.1, 0.4, -0.1],  # left ankle
    [0.1, 0.4, -0.1],  # right ankle
])

# Set up figure and axis with black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')

# Create scatter plot for point-lights
scatter = ax.scatter(points[:,0], points[:,1], c='white', s=50)

# Update function for animation
def update(frame):
    t = frame / 60.0  # time in seconds, assuming 60 fps
    theta = 2 * np.pi * t  # rotation angle for turning around
    # Adjust arm positions for swinging motion
    points_local = points.copy()
    swing_amplitude = 0.2
    swing_frequency = 2 * np.pi * 1  # swing frequency
    z_swing_left = swing_amplitude * np.sin(swing_frequency * t)
    z_swing_right = swing_amplitude * np.sin(swing_frequency * t + np.pi)  # out of phase
    # Apply swing to left arm
    points_local[4, 2] += z_swing_left  # left elbow
    points_local[6, 2] += z_swing_left  # left wrist
    # Apply swing to right arm
    points_local[5, 2] += z_swing_right  # right elbow
    points_local[7, 2] += z_swing_right  # right wrist
    # Apply global rotation around y-axis
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    rotated_points = points_local @ R.T
    # Update scatter plot with new positions
    scatter.set_offsets(rotated_points[:, :2])
    return scatter,

# Create animation with 120 frames at 50ms interval
ani = FuncAnimation(fig, update, frames=120, interval=50, blit=True)
plt.show()
