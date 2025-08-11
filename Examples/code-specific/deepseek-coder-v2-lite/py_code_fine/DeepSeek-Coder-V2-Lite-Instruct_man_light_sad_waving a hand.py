
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

# Function to update the positions of the lights
def update_positions(frame_number, positions):
    angle = 2 * np.pi * frame_number / num_frames
    positions[:, 1] = 1 - 0.5 * np.cos(angle)
    positions[:, 0] = np.sin(angle) * 0.5
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(ax.add_patch(light))

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, fargs=(positions,), frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
