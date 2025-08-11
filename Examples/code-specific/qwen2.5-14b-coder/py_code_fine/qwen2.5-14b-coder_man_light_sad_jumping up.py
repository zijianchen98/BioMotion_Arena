
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and the total number of frames
num_lights = 15
total_frames = 60

# Define the initial positions of the lights
initial_positions = np.random.rand(num_lights, 2) * 10

# Define the jump trajectory for each light
def jump_trajectory(t):
    # Simple quadratic function for jumping up and down
    return 2 * np.sin(np.pi * t / total_frames)

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create a list to hold the scatter plot objects
lights = [ax.scatter([], [], color='white', s=10) for _ in range(num_lights)]

# Define the update function for the animation
def update(frame):
    for i, light in enumerate(lights):
        x, y = initial_positions[i]
        y += jump_trajectory(frame)
        light.set_offsets([x, y])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, blit=True, repeat=False)

# Show the animation
plt.show()
