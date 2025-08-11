
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 60
light_radius = 0.2
jump_height = 1.0
jump_distance = 2.0
jump_duration = 1.0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)

# Initialize the lights
lights = [plt.Circle((0, 0), light_radius, color='white') for _ in range(num_lights)]
for light in lights:
    ax.add_patch(light)

# Function to update the positions of the lights
def update(frame):
    t = frame / (num_frames - 1)
    for i, light in enumerate(lights):
        # Calculate the position of the light
        x = jump_distance * np.sin(np.pi * t)
        y = jump_height * np.sin(np.pi * t)
        light.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
