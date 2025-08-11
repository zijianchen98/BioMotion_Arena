
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Body part coordinates for a sad jumping man represented by point lights
# Each tuple is (x, y) coordinates for a body part where index is the corresponding point-light
body_parts = np.array([
    [0, 0],  # head
    [-0.1, -0.1],  # left shoulder
    [0.1, -0.1],  # right shoulder
    [-0.15, -0.3],  # left elbow
    [0.15, -0.3],  # right elbow
    [-0.15, -0.5],  # left hand
    [0.15, -0.5],  # right hand
    [-0.1, -0.4],  # left hip
    [0.1, -0.4],  # right hip
    [-0.1, -0.7],  # left knee
    [0.1, -0.7],  # right knee
    [-0.05, -0.9],  # left foot
    [0.05, -0.9],  # right foot
    [0, -0.55],  # torso (center)
    [0, -0.4],  # neck
    [0, -0.8]   # center of mass
])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create point lights
points, = ax.plot([], [], 'wo', markersize=10)  # white points

def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    # Update point light positions based on a simple jumping behavior
    jump_height = 0.3 * np.sin(np.pi * i / 20)  # smooth jump
    y_offset = jump_height

    # Update body part positions
    new_positions = body_parts.copy()
    new_positions[:, 1] += y_offset

    # Set new data for points
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=40, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
