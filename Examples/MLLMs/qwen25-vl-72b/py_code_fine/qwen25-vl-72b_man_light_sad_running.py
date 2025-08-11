
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [plt.plot([], [], 'wo', markersize=5)[0] for _ in range(15)]

# Define the initial positions of the points based on the provided image
initial_positions = [
    (0, 1), (-1, 0), (1, 0), (-2, -1), (0, -1), (2, -1),
    (-3, -2), (-1, -2), (1, -2), (3, -2), (-2, -3), (0, -3), (2, -3),
    (-1, -4), (1, -4)
]

for i, pos in enumerate(initial_positions):
    points[i].set_data(pos)

def init():
    for point in points:
        point.set_data([], [])
    return points

def animate(frame):
    # Update the positions of the points to simulate running
    for i, point in enumerate(points):
        x, y = initial_positions[i]
        new_x = x + 0.1 * np.sin(frame / 10.0)
        new_y = y + 0.1 * np.cos(frame / 10.0)
        point.set_data(new_x, new_y)
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()
