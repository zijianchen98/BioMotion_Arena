
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 30
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0.2, 0.8, num_lights)
positions[:, 1] = 0.1

# Function to update the positions of the lights
def update_positions(frame_number, positions):
    for i in range(num_lights):
        positions[i, 1] = 0.1 + 0.2 * np.sin(0.5 * np.pi * (frame_number / num_frames))
    return positions,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 0.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=light_radius*50)

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, fargs=(positions,), interval=50, blit=True)

# Display the animation
plt.show()
