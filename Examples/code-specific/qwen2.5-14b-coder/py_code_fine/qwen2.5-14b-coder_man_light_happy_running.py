
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.array([
    [0.1, 0.1], [0.2, 0.1], [0.3, 0.1], [0.4, 0.1], [0.5, 0.1],
    [0.6, 0.1], [0.7, 0.1], [0.8, 0.1], [0.9, 0.1], [0.1, 0.2],
    [0.5, 0.2], [0.9, 0.2], [0.1, 0.3], [0.5, 0.3], [0.9, 0.3]
])

# Define the target positions for each frame
def get_target_positions(frame):
    t = frame / 100.0
    x = 0.1 + 0.8 * np.sin(2 * np.pi * (t + 0.5))
    y = 0.1 + 0.2 * np.cos(2 * np.pi * (t + 0.5))
    return np.array([[x, y] for _ in range(num_lights)])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'o', color='white')

# Update function for the animation
def update(frame):
    target_positions = get_target_positions(frame)
    points.set_data(target_positions[:, 0], target_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
