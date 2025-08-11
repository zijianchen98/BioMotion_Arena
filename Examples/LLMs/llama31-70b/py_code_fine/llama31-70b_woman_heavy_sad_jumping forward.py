
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights positions for a sad woman with heavy weight
# Each row represents a point-light, and each column represents a 3D coordinate (x, y, z)
# The z-coordinate is fixed at 0 for a 2D representation
points = np.array([
    [-0.5, -0.5, 0],  # left foot
    [0.5, -0.5, 0],   # right foot
    [-0.3, -0.3, 0],  # left knee
    [0.3, -0.3, 0],   # right knee
    [-0.2, 0, 0],     # left hip
    [0.2, 0, 0],      # right hip
    [0, -0.2, 0],     # pelvis
    [0, 0.5, 0],      # torso
    [-0.3, 0.7, 0],   # left shoulder
    [0.3, 0.7, 0],    # right shoulder
    [-0.4, 1.0, 0],   # left hand
    [0.4, 1.0, 0],    # right hand
    [-0.1, 1.2, 0],   # left eye
    [0.1, 1.2, 0],    # right eye
    [0, 1.5, 0]       # head
])

# Define the movement for each point-light
# Each row represents a point-light, and each column represents a frame in the animation
# The movement is designed to simulate a sad woman with heavy weight jumping forward
def get_frame(t):
    frame = np.zeros((15, 2))
    frame[0] = [-0.5 + 0.1 * np.sin(t), -0.5 + 0.1 * np.sin(2 * t)]  # left foot
    frame[1] = [0.5 + 0.1 * np.sin(t), -0.5 + 0.1 * np.sin(2 * t)]  # right foot
    frame[2] = [-0.3 + 0.1 * np.sin(t), -0.3 + 0.2 * np.sin(2 * t)]  # left knee
    frame[3] = [0.3 + 0.1 * np.sin(t), -0.3 + 0.2 * np.sin(2 * t)]  # right knee
    frame[4] = [-0.2 + 0.1 * np.sin(t), 0 + 0.1 * np.sin(2 * t)]  # left hip
    frame[5] = [0.2 + 0.1 * np.sin(t), 0 + 0.1 * np.sin(2 * t)]  # right hip
    frame[6] = [0 + 0.1 * np.sin(t), -0.2 + 0.1 * np.sin(2 * t)]  # pelvis
    frame[7] = [0 + 0.1 * np.sin(t), 0.5 + 0.2 * np.sin(2 * t)]  # torso
    frame[8] = [-0.3 + 0.1 * np.sin(t), 0.7 + 0.1 * np.sin(2 * t)]  # left shoulder
    frame[9] = [0.3 + 0.1 * np.sin(t), 0.7 + 0.1 * np.sin(2 * t)]  # right shoulder
    frame[10] = [-0.4 + 0.1 * np.sin(t), 1.0 + 0.1 * np.sin(2 * t)]  # left hand
    frame[11] = [0.4 + 0.1 * np.sin(t), 1.0 + 0.1 * np.sin(2 * t)]  # right hand
    frame[12] = [-0.1 + 0.1 * np.sin(t), 1.2 + 0.1 * np.sin(2 * t)]  # left eye
    frame[13] = [0.1 + 0.1 * np.sin(t), 1.2 + 0.1 * np.sin(2 * t)]  # right eye
    frame[14] = [0 + 0.1 * np.sin(t), 1.5 + 0.1 * np.sin(2 * t)]  # head
    return frame

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points_plot = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Animation function
def animate(t):
    frame = get_frame(t)
    points_plot.set_offsets(frame)
    return points_plot,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 128), interval=50)

plt.show()
