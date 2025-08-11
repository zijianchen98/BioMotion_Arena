
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = [plt.plot([], [], 'wo', markersize=10)[0] for _ in range(num_lights)]

def init():
    for light in lights:
        light.set_data([], [])
    return lights

def update(frame):
    for i in range(num_lights):
        positions[i, 1] = 0.5 + 0.1 * np.sin(0.2 * np.pi * (frame + i))
    for i, light in enumerate(lights):
        light.set_data(positions[i, 0], positions[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
