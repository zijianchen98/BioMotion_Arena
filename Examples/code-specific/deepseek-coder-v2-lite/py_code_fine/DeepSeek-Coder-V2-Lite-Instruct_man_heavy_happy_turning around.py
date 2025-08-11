
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
radius = 0.1
speed = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    angle = 2 * np.pi * i / num_lights
    positions[i, 0] = np.cos(angle)
    positions[i, 1] = np.sin(angle)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=radius*100)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    global positions
    positions += [speed * np.cos(frame / 50), speed * np.sin(frame / 50)]
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    lights.set_data(x, y)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 300), init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
