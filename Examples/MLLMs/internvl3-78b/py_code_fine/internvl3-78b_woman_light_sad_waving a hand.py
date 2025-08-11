
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

points = [ax.plot([], [], 'bo', lw=1)[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

# Constants
wave_height = 5
wave_speed = 0.1
x_coords = np.linspace(20, 80, 15)

def update(frame):
    y_coords = [wave_height * np.sin(x * 0.2 + frame * wave_speed) + 50 for x in x_coords]
    for i, point in enumerate(points):
        point.set_data(x_coords[i], y_coords[i])
    return points

ani = FuncAnimation(fig, update, frames=range(300), init_func=init, blit=True)
plt.show()
