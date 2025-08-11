
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with actual motion capture data or a more sophisticated animation model
num_frames = 60
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Simple oscillating motion for each point
for i in range(15):
    x[i, :] = 50 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_frames) + i/2)
    y[i, :] = 100 - i * 5 + 2 * np.cos(np.linspace(0, 2*np.pi, num_frames) + i/2)


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 150)
ax.set_aspect('equal') # To maintain aspect ratio
ax.set_facecolor('black')  # Black background

# Initialize the point-lights as scatter plot
points = ax.scatter([], [], s=30, c='white')

# Animation update function
def update(frame):
    points.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)

# Save the animation as a GIF (optional)
# ani.save('running_animation.gif', writer='imagemagick')

# Display the animation
plt.show()

