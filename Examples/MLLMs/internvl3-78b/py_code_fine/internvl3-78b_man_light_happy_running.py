
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Number of points and the total duration of the animation in frames
n_points = 15
n_frames = 500

# Create random initial positions for the point lights
positions = np.random.uniform(-5, 5, (n_points, 2))

# Function to update the positions of the points for each frame
def update(frame):
    for i in range(n_points):
        # Update position with some motion
        positions[i, 0] += np.random.uniform(-0.1, 0.1)
        positions[i, 1] += np.random.uniform(-0.1, 0.1)
        dot = ax.scatter(positions[i, 0], positions[i, 1], s=100, color='white')
    return dot,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=15, blit=False, repeat=False)

# Disable the axis
plt.axis('off')

# Show the plot with animation
plt.show()
