
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define body-fixed coordinates (15 points, each [x_b, y_b, z_b])
points_b = np.array([
    [0, 1.6, 0],  # head
    [0.2, 1.4, 0],  # left shoulder
    [-0.2, 1.4, 0],  # right shoulder
    [0.4, 1.3, -0.1],  # left elbow
    [-0.4, 1.3, -0.1],  # right elbow
    [0.6, 1.2, -0.2],  # left wrist
    [-0.6, 1.2, -0.2],  # right wrist
    [0.65, 1.15, -0.25],  # left hand
    [-0.65, 1.15, -0.25],  # right hand
    [0.1, 0.9, 0],  # left hip
    [-0.1, 0.9, 0],  # right hip
    [0.1, 0.5, 0],  # left knee
    [-0.1, 0.5, 0],  # right knee
    [0.1, 0.1, 0],  # left ankle
    [-0.1, 0.1, 0]   # right ankle
])

# Number of frames
num_frames = 100
# Total time in seconds
T = 2

# Create figure and axes
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(0, 1.8)
ax.set_axis_off()

# Create scatter plot
scatter = ax.scatter([], [], color='white', s=10)

# Animation function
def animate(frame):
    t = frame * T / num_frames
    theta = 2 * np.pi * t / T
    offset = 0.05 * np.sin(4 * np.pi * t / T)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    x_w = points_b[:, 0] * cos_theta - points_b[:, 2] * sin_theta
    y_w = points_b[:, 1] + offset
    scatter.set_offsets(np.column_stack((x_w, y_w)))
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=20, blit=True)

# Show the animation
plt.show()
