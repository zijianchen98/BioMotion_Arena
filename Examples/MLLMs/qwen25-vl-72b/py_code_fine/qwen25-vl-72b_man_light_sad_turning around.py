
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create the initial positions of the points
x = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7]
y = [8, 6, 6, 4, 4, 2, 2, 0, 0, -2, -2, -4, -4, -6, -6]

points, = ax.plot(x, y, 'w.', markersize=10)

def update(frame):
    global x, y
    angle = frame / 10
    new_x = []
    new_y = []
    for i in range(len(x)):
        r = np.sqrt(x[i]**2 + y[i]**2)
        theta = np.arctan2(y[i], x[i]) + angle
        new_x.append(r * np.cos(theta))
        new_y.append(r * np.sin(theta))
    x = new_x
    y = new_y
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, update, frames=range(0, 360), interval=50, blit=True)
plt.show()
