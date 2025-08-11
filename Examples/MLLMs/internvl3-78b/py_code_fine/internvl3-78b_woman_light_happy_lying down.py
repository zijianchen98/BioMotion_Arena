
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
num_frames = 100
interval = 50  # Time between frames in milliseconds

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Function to initialize points
def init():
    point_positions.set_offsets(np.zeros((num_points, 2)))
    return point_positions,

# Function to update point positions
def animate(frame):
    t = frame * 0.05  # Time parameter for sine wave motion
    points = np.zeros((num_points, 2))

    # Define point positions for a lying motion
    for i in range(num_points):
        points[i, 0] = np.sin(i * 0.5 + t) * 0.3
        points[i, 1] = np.cos(i * 0.4 + t) * 0.3

    point_positions.set_offsets(points)
    return point_positions,

# Create scatter plot for point lights
point_positions = ax.scatter([], [], color='white')

# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=interval, blit=True)

# Display the animation
plt.show()
