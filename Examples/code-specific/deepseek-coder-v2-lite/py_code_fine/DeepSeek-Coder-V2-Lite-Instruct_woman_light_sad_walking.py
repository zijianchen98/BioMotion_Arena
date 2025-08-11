
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-1, 1, num_lights)
positions[:, 1] = 1

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axis

# Initialize the lights as scatter plot
lights = ax.scatter(positions[:, 0], positions[:, 1], s=light_radius*1000, color='white')

# Function to update the positions of the lights
def update(frame):
    # Update the y positions to simulate walking
    positions[:, 1] -= 0.05  # Move lights down
    if positions[0, 1] < -1:  # Reset positions when lights go out of view
        positions[:, 1] = 1
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
