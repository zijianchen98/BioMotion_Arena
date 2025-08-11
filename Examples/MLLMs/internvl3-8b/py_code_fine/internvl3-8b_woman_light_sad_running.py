
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create the figure with a black background
fig, ax = plt.subplots()
ax.set_facecolor("black")

def initialize_points():
    # Create 15 points in the center of the figure
    points = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (0, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1),
              (0, -2), (0, -3), (0, -4),
              (0, 2), (0, 3), (0, 4)]
    return points

def update_points(n, points):
    for i in range(15):
        x, y = points[i]
        x += np.random.uniform(-0.5, 0.5)
        y += np.random.uniform(-0.5, 0.5)
        # Ensure points stay on screen
        if x < -2: x = -2
        if x > 2: x = 2
        if y < -5: y = -5
        if y > 5: y = 5
        points[i] = x, y
    return points

points = initialize_points()

sc = plt.scatter(*zip(*points), c='white')

def animate(i):
    update_points(i, points)
    sc.set_offsets(points)
    return sc,

ani = FuncAnimation(fig, animate, init_func=initialize_points, blit=True, interval=50)
plt.axis('off')
plt.show()
