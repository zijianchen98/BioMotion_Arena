
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
    point, = ax.plot(x[i], y[i], 'o', color='white')
    points.append(point)

def animate(i):
    global x, y
    # Update the positions of the points
    for j in range(15):
        x[j] += np.random.normal(0, 0.1)
        y[j] += np.random.normal(0, 0.1)
        points[j].set_data(x[j], y[j])
    return points

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
