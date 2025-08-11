
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 30

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights as scatter plot
lights = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

def update(frame):
    # Update positions of the lights
    positions[:, 1] += 0.05  # Move lights down
    if positions[-1, 1] > 1:  # Reset if lights go out of bounds
        positions[:, 1] = 0.5
        positions[:, 0] = np.linspace(0, 1, num_lights)

    # Update the scatter plot
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

# Display the animation
plt.show()
