
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a list to store the point-lights
point_lights = [ax.plot([], [], 'wo')[0] for _ in range(15)]
positions = np.random.rand(15, 2) * 100

def init():
    for point in point_lights:
        point.set_data([], [])
    return point_lights

def animate(i):
    global positions
    positions += np.random.normal(size=(15, 2)) * 0.5
    positions = np.clip(positions, 0, 100)
    for point, pos in zip(point_lights, positions):
        point.set_data(pos[0], pos[1])
    return point_lights

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=50, blit=True)

plt.show()
