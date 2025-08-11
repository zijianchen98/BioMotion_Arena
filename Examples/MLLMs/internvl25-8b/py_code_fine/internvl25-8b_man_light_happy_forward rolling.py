
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(-1, 1)
ax.set_axis_off()

# Define initial positions of the points
x = np.zeros(num_points)
y = np.zeros(num_points)
speed = np.ones(num_points)
positions = np.column_stack((x, y))
direction = np.array([[0.5, 0], [0.8, 0.1], [0.5, -0.5], [0.4, 0.7],
                      [0.3, -0.3], [0.1, -0.3], [0.6, 0.4], [0.3, 0.1],
                      [0.5, 0.5], [0.1, 0.4], [0.0, 0.2], [0.4, 0.1],
                      [0.2, -0.2], [0.7, -0.1], [0.3, 0]])

# Update function for the animation
def update(i):
    dt = 0.05
    for j in range(num_points):
        direction[j] = 0.9 * direction[j] + 0.1 * speed[j]
        speed[j] += direction[j]
        global positions
        pos = positions[j] + speed[j] * dt
        positions[j] = pos

    line.set_data(positions[:,0], positions[:,1])

    return line,


# Create the animation
line, = ax.plot(positions[:, 0], positions[:, 1], 'o', color="white", markersize=1, ms=6)
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
