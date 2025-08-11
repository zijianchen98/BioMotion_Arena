
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for the jump
target_positions = np.array([[0.5, 0.8], [0.4, 0.7], [0.3, 0.6], [0.2, 0.5], [0.1, 0.4],
                            [0.2, 0.3], [0.3, 0.2], [0.4, 0.1], [0.5, 0], [0.6, 0.1],
                            [0.7, 0.2], [0.8, 0.3], [0.9, 0.4], [0.8, 0.5], [0.7, 0.6]])

# Define the time points for the animation
time_points = np.linspace(0, 1, num=50)

# Define the interpolation function
def interpolate_positions(initial, target, t):
    return initial + (target - initial) * t

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the point-lights
points, = ax.plot([], [], 'o', color='white', markersize=5)

# Define the update function for the animation
def update(frame):
    t = frame / len(time_points)
    current_positions = interpolate_positions(initial_positions, target_positions, t)
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(time_points), blit=True, repeat=False)

# Show the animation
plt.show()
