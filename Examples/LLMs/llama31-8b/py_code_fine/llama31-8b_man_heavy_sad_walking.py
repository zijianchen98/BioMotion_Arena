
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
N_POINTS = 15  # Number of points
FRAME_RATE = 30  # Frames per second
FRAME_DURATION = 1000 / FRAME_RATE  # Duration of each frame in milliseconds

# Define the point positions and movements
points = np.zeros((N_POINTS, 2))
points[:, 0] = np.linspace(0.2, 0.8, N_POINTS)  # x-coordinates
points[:, 1] = np.linspace(0.2, 0.8, N_POINTS)  # y-coordinates

# Define the movement parameters
amplitude = 0.1
frequency = 1  # Hz
phase = np.linspace(0, 2 * np.pi, N_POINTS)

# Function to update the point positions
def update(frame):
    global points
    points[:, 0] = np.sin(frame * frequency + phase) * amplitude + 0.5  # x-coordinates
    points[:, 1] = np.cos(frame * frequency + phase) * amplitude + 0.5  # y-coordinates
    return plt.plot(points[:, 0], points[:, 1], 'o-', markersize=10, color='white')

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set the background color to black
ax.set_xlim(0, 1)  # Set the x-axis limits
ax.set_ylim(0, 1)  # Set the y-axis limits
ax.set_aspect('equal')  # Set the aspect ratio to equal

# Animate the points
ani = animation.FuncAnimation(fig, update, frames=int(FRAME_RATE * 2), interval=FRAME_DURATION, repeat=True)

# Show the animation
plt.show()
