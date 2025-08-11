
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the number of point lights
n_points = 15

# Define the initial positions of the point lights
initial_positions = np.array([
    [-0.2, -0.2, 0.0],
    [-0.2, 0.0, 0.0],
    [-0.2, 0.2, 0.0],
    [-0.1, -0.2, 0.0],
    [-0.1, 0.0, 0.0],
    [-0.1, 0.2, 0.0],
    [0.0, -0.2, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0],
    [0.1, -0.2, 0.0],
    [0.1, 0.0, 0.0],
    [0.1, 0.2, 0.0],
    [0.2, -0.2, 0.0],
    [0.2, 0.0, 0.0],
    [0.2, 0.2, 0.0]
])

# Define the final positions of the point lights
final_positions = np.array([
    [-0.2, -0.2, 0.0],
    [-0.2, 0.0, 0.0],
    [-0.2, 0.2, 0.0],
    [-0.1, -0.2, 0.0],
    [-0.1, 0.0, 0.0],
    [-0.1, 0.2, 0.0],
    [0.0, -0.2, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0],
    [0.1, -0.2, 0.0],
    [0.1, 0.0, 0.0],
    [0.1, 0.2, 0.0],
    [0.2, -0.2, 0.0],
    [0.2, 0.0, 0.0],
    [0.2, 0.2, 0.0]
])

# Define the movement paths for the point lights
def movement_path(t, initial_position, final_position):
    return initial_position + (final_position - initial_position) * t

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_axis_off()
    
    t = i / 100.0  # animation time
    positions = np.array([movement_path(t, initial_positions[j], final_positions[j]) for j in range(n_points)])
    
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='w', s=100)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animate the movement
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, repeat=False)

# Display the animation
plt.show()
