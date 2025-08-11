
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(light)
    ax.add_artist(light)

# Function to update the positions of the lights
def update(frame):
    for i in range(num_lights):
        positions[i, 1] += 0.05  # Move down the y-axis
        if positions[i, 1] > 1:
            positions[i, 1] = 0.5  # Reset y-position when it goes out of bounds
        lights[i].center = (positions[i, 0], positions[i, 1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=True)

# Show the animation
plt.show()
