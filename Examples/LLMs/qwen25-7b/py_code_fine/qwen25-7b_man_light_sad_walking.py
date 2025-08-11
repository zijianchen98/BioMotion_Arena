
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the duration of the animation
num_points = 15
duration = 10  # seconds

# Define the walking motion parameters
step_length = 0.5  # meters
step_time = 1.2  # seconds per step
stride_length = step_length * 1.2  # meters
swing_time = step_time / 2
stance_time = step_time - swing_time
stride_time = stride_length / (2 * step_length)

# Define the walking pattern
def walking_pattern(t):
    x_x = []
    y_y = []
    phase = t % stride_time
    if phase < swing_time:
        x_x.append(stride_length * (phase / swing_time) - step_length)
        y_y.append(0.1 * np.sin(np.pi * (phase / swing_time - 0.5)))
    else:
        x_x.append(stride_length - step_length + (phase - swing_time) * step_length / (stride_time - swing_time))
        y_y.append(0.1 * np.sin(np.pi * ((phase - swing_time) / (stride_time - swing_time) - 1)))
    return np.array([x for x_x, y_y in zip(x_x, y_y) for x_x in [x_x]]), np.array([y for y_y in y_y])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal'
points, = ax.plot([], [], 'o', color='white')

# Initialization function to set the initial state
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    x, y = walking_pattern(i / 30)
    points.set_data(x, y)
    return points,

# Call the animator
ani = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, duration * 30, blit=True)

# Show the animation
plt.show()
