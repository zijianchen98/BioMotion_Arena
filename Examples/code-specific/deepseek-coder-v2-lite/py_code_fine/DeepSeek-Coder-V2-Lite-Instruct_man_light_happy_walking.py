
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

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(ax.add_patch(light))

# Function to update the positions of the lights
def update(frame):
    for i in range(num_lights):
        positions[i, 1] += 0.02  # Simple vertical movement
        if positions[i, 1] > 1:
            positions[i, 1] = -1
        lights[i].center = (positions[i, 0], positions[i, 1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=True)

# Show the animation
plt.show()
