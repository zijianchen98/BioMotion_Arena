
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0.2, 0.8, num_lights)
positions[:, 1] = 0.2

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the lights
lights = [plt.Circle((pos[0], pos[1]), light_radius, color='white') for pos in positions]
for light in lights:
    ax.add_artist(light)

# Function to update the positions of the lights
def update(frame):
    for i in range(num_lights):
        positions[i, 1] += 0.01 * (0.5 - np.random.rand())  # Random jitter for natural movement
        lights[i].center = (positions[i, 0], positions[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
