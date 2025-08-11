
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
ax.set_facecolor('black')

# Initialize the lights
lights = [plt.Circle((pos, 0), light_radius, color='white') for pos in positions[:, 0]]
for light in lights:
    ax.add_artist(light)

def update(frame):
    # Update positions of the lights
    for i, light in enumerate(lights):
        positions[i, 1] = np.sin(np.pi * (frame + i) / num_frames) * 0.5
        light.center = (positions[i, 0], positions[i, 1])

    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), blit=True, repeat=True)

# Display the animation
plt.show()
