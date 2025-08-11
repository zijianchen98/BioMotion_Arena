
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

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = [plt.Circle((pos[0], pos[1]), light_radius, color='white') for pos in positions]
for light in lights:
    ax.add_artist(light)

# Function to update the positions of the lights
def update(frame):
    for i in range(num_lights):
        positions[i, 1] -= 0.02  # Move the light downwards
        if positions[i, 1] < -0.5:
            positions[i, 1] = 0.5  # Reset position when it goes out of bounds
    for light, pos in zip(lights, positions):
        light.center = (pos[0], pos[1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
