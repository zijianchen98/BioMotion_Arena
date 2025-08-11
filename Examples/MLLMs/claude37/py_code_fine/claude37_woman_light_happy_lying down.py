
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup parameters for the animation
num_points = 15
duration = 200  # milliseconds
frames = 60

# Define initial positions of the point-lights for a "lying down" position
initial_positions = np.array([
    [0, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2],  # Upper Body
    [-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1],  # Lower Body
    [-1, 0], [1, 0]   # Feet
])

# Generate a sine wave motion for smooth movement
time = np.linspace(0, 2 * np.pi, frames)
x_offsets = 0.1 * np.sin(time)  # Side-to-side motion
y_offsets = -0.05 * np.cos(time)  # Up-down motion

# Prepare the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Update positions of the point lights
    new_positions = initial_positions + np.column_stack((x_offsets[frame]*np.ones(num_points),
                                                          y_offsets[frame]*np.ones(num_points)))
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames,
                              init_func=init, blit=True,
                              interval=duration / frames)

# Show the animation
plt.show()
