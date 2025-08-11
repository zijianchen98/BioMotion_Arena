
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Initialize the lights as scatter plot
lights = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

# Function to update the positions of the lights
def update(frame):
    # Update the y positions to simulate bowing motion
    angle = (frame / num_frames) * np.pi
    positions[:, 1] = 0.5 + 0.2 * np.sin(angle)
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Set up plot
ax.set_facecolor('black')
plt.axis('off')
plt.show()
