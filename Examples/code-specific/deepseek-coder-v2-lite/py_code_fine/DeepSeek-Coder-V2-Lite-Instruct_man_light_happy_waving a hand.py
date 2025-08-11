
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
light_radius = 0.1
animation_duration = 5  # seconds
fps = 30
num_frames = fps * animation_duration

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
lights = ax.scatter(positions[:, 0], positions[:, 1], s=light_radius*1000, c='white')

def update(frame):
    # Update positions of the lights
    positions[:, 1] += 0.01  # Move lights downwards
    if positions[-1, 1] > 1:  # Reset positions when lights go out of bounds
        positions[:, 1] = 0.5
        positions[:, 0] = np.linspace(0, 1, num_lights)

    # Update the scatter plot
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
