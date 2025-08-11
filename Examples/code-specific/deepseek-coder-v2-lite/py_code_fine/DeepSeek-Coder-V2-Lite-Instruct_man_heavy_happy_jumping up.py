
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 2  # seconds
fps = 30
num_frames = duration * fps

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 1] = np.linspace(0, 1, num_lights)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the lights
lights = [plt.plot([], [], 'wo', markersize=10)[0] for _ in range(num_lights)]

def init():
    for light in lights:
        light.set_data([], [])
    return lights

def update(frame):
    t = frame / fps
    for i, light in enumerate(lights):
        # Simple harmonic motion for the x-coordinate
        positions[i, 0] = np.sin(t + i * 0.2)
        light.set_data(positions[i, 0], positions[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
