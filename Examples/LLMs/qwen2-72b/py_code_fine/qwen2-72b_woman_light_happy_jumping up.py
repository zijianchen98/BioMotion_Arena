
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the position of the points
num_frames = 100
num_points = 15
points = np.zeros((num_frames, num_points, 2))

# Generate the jumping motion
for i in range(num_frames):
    t = i / 20.0  # Time in seconds
    for j in range(num_points):
        # Simulate a jumping motion for each point
        x = np.sin(t + j * 0.2) * 50 + 100 * np.random.rand() - 50
        y = np.cos(t + j * 0.2) * 50 + 100 * np.random.rand() - 50
        points[i, j] = [x, y]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_facecolor('black')

# Function to update the animation frame
def update(frame):
    ax.clear()
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    ax.set_facecolor('black')
    for j in range(num_points):
        ax.plot(points[frame, j, 0], points[frame, j, 1], 'wo', markersize=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

plt.show()
