
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial positions of the point lights representing the sad woman
points = np.zeros((15, 2))

# Initial velocities for horizontal and vertical motion
velocities = np.zeros((15, 2))
velocities[:, 0] = np.linspace(1, -1, num=15)
velocities[:, 1] = np.linspace(-1, 1, num=15)

# Generate initial positions based on velocities
for i in range(15):
    points[i] = (velocities[i, 0]*5, velocities[i, 1]*5)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)

def init():
    lines = [line.set_data([], []) for line in ax.get_lines()]
    return lines

def animate(i):
    # Update positions based on velocities
    new_points = points + velocities * i
    # Update lines
    for line, point in zip(ax.get_lines(), new_points):
        line.set_data(point[0], point[1])
    return ax.get_lines()

# Create the animation
animate = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

plt.show()
