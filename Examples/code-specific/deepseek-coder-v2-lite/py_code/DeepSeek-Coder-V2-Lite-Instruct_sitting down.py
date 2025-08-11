
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-0.5, 0.5, num_lights)
positions[:, 1] = 0.5

# Function to update the positions of the lights
def update_positions(frame_number, positions):
    angle = 2 * np.pi * frame_number / num_frames
    new_positions = np.zeros_like(positions)
    new_positions[:, 0] = positions[:, 0] * np.cos(angle) - positions[:, 1] * np.sin(angle)
    new_positions[:, 1] = positions[:, 0] * np.sin(angle) + positions[:, 1] * np.cos(angle)
    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(ax.add_patch(light))

# Function to initialize the background and lights
def init():
    for light in lights:
        light.set_visible(False)
    return lights

# Function to update the appearance of the lights in each frame
def update(frame_number):
    new_positions = update_positions(frame_number, positions)
    for i, light in enumerate(lights):
        light.center = (new_positions[i, 0], new_positions[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
