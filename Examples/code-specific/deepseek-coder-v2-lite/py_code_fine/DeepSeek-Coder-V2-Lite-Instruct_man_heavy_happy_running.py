
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
light_radius = 0.2
black_background = np.zeros((60, 60))

# Initial positions of the lights
positions = np.random.rand(num_lights, 2) * 50

# Define the running trajectory
trajectory = np.linspace(0, 2 * np.pi, 100)
x_trajectory = np.cos(trajectory) * 20 + 30
y_trajectory = np.sin(trajectory) * 20 + 30

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 60)
ax.set_ylim(0, 60)

# Initialize the lights
lights = [plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white') for i in range(num_lights)]
for light in lights:
    ax.add_artist(light)

def init():
    for light in lights:
        light.center = (positions[lights.index(light), 0], positions[lights.index(light), 1])
    return lights

def update(frame):
    for i in range(num_lights):
        positions[i, 0] = x_trajectory[frame] + np.cos(trajectory[frame] + i * 0.1) * 5
        positions[i, 1] = y_trajectory[frame] + np.sin(trajectory[frame] + i * 0.1) * 5
        lights[i].center = (positions[i, 0], positions[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
