
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
lights = [plt.Circle((0, 0), light_radius, color='white')]
for i in range(1, num_lights):
    lights.append(plt.Circle((0, 0), light_radius, color='white'))
ax.add_artist(lights[0])

# Function to update the position of the lights
def update(frame):
    t = frame / (num_frames - 1)
    for i in range(num_lights):
        x = jump_distance * np.sin(np.pi * t)
        y = jump_height * (1 - np.cos(np.pi * t)) - jump_height
        lights[i].center = (x + i * 0.2, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Set the background to black
ax.set_facecolor('black')

# Show the animation
plt.show()
