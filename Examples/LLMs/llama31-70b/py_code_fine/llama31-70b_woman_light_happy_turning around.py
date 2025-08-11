
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the initial positions of the point-lights (happy woman)
# These positions are approximate and can be adjusted to better represent the action
initial_positions = np.array([
    [-0.5, -0.5],  # left foot
    [0.5, -0.5],   # right foot
    [-0.2, -0.3],  # left knee
    [0.2, -0.3],   # right knee
    [-0.1, -0.1],  # left hip
    [0.1, -0.1],   # right hip
    [-0.3, 0.2],   # left shoulder
    [0.3, 0.2],    # right shoulder
    [-0.2, 0.3],   # left elbow
    [0.2, 0.3],    # right elbow
    [-0.1, 0.4],   # left hand
    [0.1, 0.4],    # right hand
    [0, 0.6],      # head
    [-0.1, 0.5],   # left eye
    [0.1, 0.5]     # right eye
])

# Define the movement of the point-lights (turning around)
def animate(frame):
    positions = initial_positions.copy()
    angle = np.radians(frame)
    
    # Rotate the body around the vertical axis
    for i in range(n_points):
        if i not in [0, 1, 4, 5, 11, 12, 13, 14]:  # do not rotate feet, hips, and head
            positions[i, 0] = initial_positions[i, 0] * np.cos(angle) - initial_positions[i, 1] * np.sin(angle)
            positions[i, 1] = initial_positions[i, 0] * np.sin(angle) + initial_positions[i, 1] * np.cos(angle)
    
    # Update the positions of the point-lights
    scatter.set_offsets(positions)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=10, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(360), interval=50)

plt.show()
