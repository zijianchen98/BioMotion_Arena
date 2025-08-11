
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create the initial positions of the points
x = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7]
y = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

points = []
for i in range(15):
    point, = ax.plot(x[i], y[i], 'w.', markersize=10)
    points.append(point)

def animate(i):
    global x, y
    # Update the positions of the points
    for j in range(15):
        x[j] += 0.1 * np.sin(i/10 + j/2)
        y[j] += 0.1 * np.cos(i/10 + j/2)
        points[j].set_data(x[j], y[j])
    return points

ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.show()
