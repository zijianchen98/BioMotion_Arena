
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_lights = 15
light_radius = 2
background_color = 'black'
light_color = 'white'
frame_rate = 30

# Define the positions of the lights
lights = np.zeros((num_lights, 2))
lights[:, 0] = np.random.uniform(0, 10, size=num_lights)
lights[:, 1] = np.random.uniform(0, 10, size=num_lights)

# Define the action (walking)
def walking(lights, frame):
    # Define the movement of each light
    for i in range(num_lights):
        if i < 5:
            lights[i, 0] += 0.5 * np.sin(frame * 0.1 + i * 0.1)
            lights[i, 1] += 0.5 * np.cos(frame * 0.1 + i * 0.1)
        elif i < 10:
            lights[i, 0] -= 0.5 * np.sin(frame * 0.1 + (i - 5) * 0.1)
            lights[i, 1] -= 0.5 * np.cos(frame * 0.1 + (i - 5) * 0.1)
        else:
            lights[i, 0] += 0.5 * np.sin(frame * 0.1 + (i - 10) * 0.1)
            lights[i, 1] += 0.5 * np.cos(frame * 0.1 + (i - 10) * 0.1)

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_axis_off()

# Plot the lights
light_patches = []
for i in range(num_lights):
    light = plt.Circle((lights[i, 0], lights[i, 1]), light_radius, color=light_color)
    ax.add_patch(light)
    light_patches.append(light)

# Animate the plot
def animate(frame):
    walking(lights, frame)
    for i in range(num_lights):
        light_patches[i].center = (lights[i, 0], lights[i, 1])
    return light_patches

ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=True, interval=1000 // frame_rate)

plt.show()
