
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of points
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions of the points (approximating a sad woman with heavy weight)
initial_positions = np.array([
    [0.0, 0.6], [0.1, 0.5], [0.2, 0.5], [0.1, 0.4], [0.0, 0.3],
    [0.3, 0.6], [0.4, 0.5], [0.5, 0.5], [0.4, 0.4], [0.3, 0.3],
    [-0.1, 0.5], [0.1, 0.2], [0.0, 0.1], [-0.1, 0.1], [0.1, 0.0]
])

points[:, :] = initial_positions

# Set parameters for the jump animation
amplitude = 0.2
frequency = 2.0
time = 0.0
dt = 0.02

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.1, 0.8)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

def update(frame):
    global time
    time += dt
    jump_height = amplitude * np.sin(2 * np.pi * frequency * time)
    points[:, 1] = initial_positions[:, 1] + jump_height
    sc.set_offsets(points)
    return sc,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

# Display the animation
plt.show()
