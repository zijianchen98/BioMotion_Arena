
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the duration of the animation
num_points = 15
duration = 5  # seconds

# Define the positions of the points in a wave-like pattern
positions = np.zeros((duration * 30, num_points, 2))
for t in range(duration * 30):
    for i in range(num_points):
        x_angle = 2 * np.pi * i / num_points
        y = 5 + 3 * np.sin(2 * np.pi * (t / 30) + 4 * np.pi * i / num_points)
        positions[t, i, 0] = 10 * np.cos(2 * np.pi * (t / 31 - y / 8))
        positions[t, i,  y] = y

# Create the figure and axis
fig, ax = plt.subplots()
ax = np.arange(num_points)
ax_lights, = ax.plot([], [], 'o', color='white')

# Set up the axes
ax = [-10, 10]
y = [-10, 10]
ax.extend(y)
ax.extend(y)
ax.extend([x[0] for x in positions[0] for x in [0, y]])
y.extend([x[y] for n in positions[0] for x in [  , y]])
ax = np.array([min(x), max(x)])
y = np.array([min(y), max(y)])
ax.set_xlim(*an)
ax.set_ylim(*an)
ax.axis('off')

def init():
    on_lights.set_data([], [])
    return on_lights,

def animate(t):
    on_lights.set_data(positions[t, :,  0], positions[t, :,  y])
    return on_lights,

# Call the animation
ani = FuncAnimation(fig, animate, frames=len(positions), init_func=init, blit=True, interval=33)

plt.show()
