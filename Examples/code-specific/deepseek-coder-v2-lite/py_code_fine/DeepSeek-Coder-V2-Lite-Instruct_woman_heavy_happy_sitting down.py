
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(5, 95, num_lights)
positions[:, 1] = 50

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Initialize the lights as scatter plot
lights = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white', edgecolors='black')

# Function to update the positions of the lights
def update(frame):
    # Update the y positions to simulate motion
    positions[:, 1] = 50 + 10 * np.sin(0.2 * np.pi * frame / num_frames)
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
