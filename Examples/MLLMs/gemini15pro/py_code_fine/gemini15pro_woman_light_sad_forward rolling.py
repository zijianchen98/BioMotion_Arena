
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 points over time
# This is a simplified example and would need to be replaced with real motion capture data or similar
# for a realistic biological motion animation
num_frames = 60
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Simple vertical oscillations for each point
for i in range(15):
    y[i, :] = 5 * np.sin(2 * np.pi * np.linspace(0, 1, num_frames) + i/2) + i * 5 + 10
    x[i, :] = 5 * np.cos(2 * np.pi * np.linspace(0,1, num_frames) + i/2) + i * 2 + 15

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 50)  # Adjust limits as needed
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create point-light scatter plot
points = ax.scatter([], [], s=30, c='white')

# Update function for animation
def update(frame):
    points.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval = 100, repeat=True)

plt.show()

