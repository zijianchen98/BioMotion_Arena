
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_lights = 15
num_frames = 100
fps = 30

# Define the movement of each light
lights = np.zeros((num_lights, num_frames, 2))

# Define the movement of the sad woman bowing
# The lights will move in a sinusoidal pattern to represent the movement of the body
for i in range(num_lights):
    lights[i, :, 0] = np.sin(2 * np.pi * np.linspace(0, 1, num_frames) + i / num_lights * 2 * np.pi)

# Define the position of the lights at the beginning and end of the animation
lights[:, 0, 0] = np.random.uniform(-1, 1, num_lights)
lights[:, -1, 0] = np.sin(2 * np.pi * np.linspace(0, 1, num_lights))

# Define the height of the lights
lights[:, :, 1] = np.sin(2 * np.pi * np.linspace(0, 1, num_frames)) * 0.5 + 1

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_axis_off()

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_axis_off()
    for i in range(num_lights):
        ax.plot(lights[i, frame, 0], lights[i, frame, 1], 'o', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 // fps)

# Show the animation
plt.show()
