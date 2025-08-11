
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
hand_movement = np.linspace(0, 2 * np.pi, num_frames)

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the scatter plot for the lights
points, = ax.plot([], [], 'wo', ms=10)

# Function to update the points for each frame
def update(frame):
    theta = hand_movement[frame]
    positions = np.array([np.sin(theta) * 0.5, np.cos(theta) * 0.5]).T
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True, repeat=True)

# Set the background to black
ax.set_facecolor('black')

# Show the animation
plt.show()
