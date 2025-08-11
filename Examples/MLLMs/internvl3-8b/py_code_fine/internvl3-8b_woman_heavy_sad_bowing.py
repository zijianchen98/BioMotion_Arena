
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the time of each frame in seconds
T = 2  # Total duration of the animation in seconds
fps = 60  # Frames per second

# Define the number of frames
num_frames = T * fps

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)  # Setting the x-axis limits
ax.set_ylim(0, 1)  # Setting the y-axis limits
ax.set_aspect('equal')  # Equal aspect ratio

# Create 15 points in a pattern representing the woman bowing
num_points = 15
angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
x = np.cos(angles)
y = np.sin(angles)

# Initialize the points
points, = ax.plot(x, y, 'o', color='white')

# Animation update function
def update(frame):
    t = frame / fps
    angle = np.pi / 2 + (1 - np.sin(np.pi * (2 * t)))  # Bowing motion
    x = np.cos(angles) * np.cos(angle)
    y = np.sin(angles) - 0.15 * np.sin(np.pi * (2 * t)) * np.cos(angles)  # Y displacement
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

# Save the animation
ani.save('sadwoman_bowing.gif', writer='imagemagick')

# Show the animation
plt.show()
