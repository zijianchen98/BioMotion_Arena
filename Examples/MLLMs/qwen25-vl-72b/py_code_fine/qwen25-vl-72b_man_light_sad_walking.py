
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create the initial positions of the points
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 5, 5, 5, 5]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 5, 5, 5, 5, 5]

# Create the scatter plot of the points
points = ax.scatter(x, y, color='white')

# Define the update function for the animation
def update(frame):
    # Update the positions of the points
    x[0] += 0.1 * np.sin(frame / 10)
    x[1] += 0.1 * np.sin(frame / 10 + np.pi / 2)
    x[2] += 0.1 * np.sin(frame / 10 + np.pi)
    x[3] += 0.1 * np.sin(frame / 10 + 3 * np.pi / 2)
    x[4] += 0.1 * np.sin(frame / 10)
    x[5] += 0.1 * np.sin(frame / 10 + np.pi / 2)
    x[6] += 0.1 * np.sin(frame / 10 + np.pi)
    x[7] += 0.1 * np.sin(frame / 10 + 3 * np.pi / 2)
    x[8] += 0.1 * np.sin(frame / 10)
    x[9] += 0.1 * np.sin(frame / 10 + np.pi / 2)
    x[10] += 0.1 * np.sin(frame / 10 + np.pi)
    x[11] += 0.1 * np.sin(frame / 10 + 3 * np.pi / 2)
    x[12] += 0.1 * np.sin(frame / 10)
    x[13] += 0.1 * np.sin(frame / 10 + np.pi / 2)
    x[14] += 0.1 * np.sin(frame / 10 + np.pi)

    y[0] += 0.1 * np.cos(frame / 10)
    y[1] += 0.1 * np.cos(frame / 10 + np.pi / 2)
    y[2] += 0.1 * np.cos(frame / 10 + np.pi)
    y[3] += 0.1 * np.cos(frame / 10 + 3 * np.pi / 2)
    y[4] += 0.1 * np.cos(frame / 10)
    y[5] += 0.1 * np.cos(frame / 10 + np.pi / 2)
    y[6] += 0.1 * np.cos(frame / 10 + np.pi)
    y[7] += 0.1 * np.cos(frame / 10 + 3 * np.pi / 2)
    y[8] += 0.1 * np.cos(frame / 10)
    y[9] += 0.1 * np.cos(frame / 10 + np.pi / 2)
    y[10] += 0.1 * np.cos(frame / 10 + np.pi)
    y[11] += 0.1 * np.cos(frame / 10 + 3 * np.pi / 2)
    y[12] += 0.1 * np.cos(frame / 10)
    y[13] += 0.1 * np.cos(frame / 10 + np.pi / 2)
    y[14] += 0.1 * np.cos(frame / 10 + np.pi)

    points.set_offsets(np.c_[x, y])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
