
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
num_frames = 200
walk_period = 8  # seconds
background_color = 'black'
point_color = 'white'
point_size = 50
fig, ax = plt.subplots()

# Initialize the scatter plot
scatter = ax.scatter([], [], s=point_size, c=point_color)

# Set the background color
ax.set_facecolor(background_color)

# Adjust the limits of the plot
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
ax.axis('off')  # Hide the axes

# Initialize the positions of the points
def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

# Animation update function
def update(frame):
    t = frame / num_frames * walk_period * 2 * np.pi
    x = 8 * np.sin(2 * t)
    y = 0.5 * np.sin(4 * t) + 0.5
    positions = np.column_stack((x, y))
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
