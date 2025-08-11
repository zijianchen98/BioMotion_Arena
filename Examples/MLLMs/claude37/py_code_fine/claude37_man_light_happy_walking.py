
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Set the number of point lights and frames
num_lights = 15
num_frames = 100

# Initialize the positions of point lights (x, y)
# Using an array of [x, y] coordinates for walking motion
light_positions = np.zeros((num_lights, 2, num_frames))

# Define positions for a simple walking motion
for t in range(num_frames):
    # Simple left-right walking motion with some up and down movement
    light_positions[:, 0, t] = np.sin(t / 10) * 0.1 + np.linspace(-0.2, 0.2, num_lights)  # X positions
    light_positions[:, 1, t] = np.cos(t / 10) * 0.05 + np.linspace(-0.5, 0.5, num_lights)  # Y positions

# Create a figure for the animation
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.75, 0.75)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    x_data = light_positions[:, 0, frame]
    y_data = light_positions[:, 1, frame]
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
