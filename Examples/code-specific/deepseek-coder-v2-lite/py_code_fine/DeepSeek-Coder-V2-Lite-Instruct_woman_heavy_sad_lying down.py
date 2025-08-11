
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0.2, 0.8, num_lights)
positions[:, 1] = 0.2

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights as scatter plot
lights = ax.scatter(positions[:, 0], positions[:, 1], s=light_radius*100, color='white')

def update(frame):
    # Update positions of the lights
    for i in range(num_lights):
        positions[i, 1] += 0.02 * (1 - positions[i, 0])  # Simple vertical movement
        if positions[i, 1] > 0.8:
            positions[i, 1] = 0.2

    # Update the scatter plot
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
