
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15  # Number of point lights
duration = 300   # Duration of animation in frames
fps = 30         # Frames per second
weight_positions = np.array([
    [0, 1], # Head
    [-0.5, 0.5], [0.5, 0.5], # Shoulders
    [-0.7, 0], [0.7, 0], # Hips
    [-1.0, -0.5], [1.0, -0.5], # Knees
    [-1.5, -1], [1.5, -1], # Feet
])

# Generate running motion
def create_running_motion(frame):
    motion = []
    for i in range(num_points):
        x_offset = np.sin((frame + i) * 0.2) * 0.1
        y_offset = np.cos((frame + i) * 0.3) * (0.1 + 0.5) - 1.0
        motion.append(weight_positions[i % weight_positions.shape[0]] + [x_offset, y_offset])
    return np.array(motion)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    motion = create_running_motion(frame)
    points.set_data(motion[:, 0], motion[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=duration, init_func=init, blit=True, interval=1000/fps)

# Display the animation
plt.show()
