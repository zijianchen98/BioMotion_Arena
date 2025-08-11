
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(5, 95, num_lights)
positions[:, 1] = 50

# Define the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

lights = [plt.plot([], [], 'wo', markersize=10)[0] for _ in range(num_lights)]

def init():
    for light in lights:
        light.set_data([], [])
    return lights

def animate(i):
    for j, light in enumerate(lights):
        # Simple sinusoidal motion for each light
        positions[j, 1] = 50 + 5 * np.sin(0.2 * np.pi * (i / num_frames) + j * 0.2)
        light.set_data(positions[j, 0], positions[j, 1])
    return lights

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, blit=True, repeat=True)

plt.show()
