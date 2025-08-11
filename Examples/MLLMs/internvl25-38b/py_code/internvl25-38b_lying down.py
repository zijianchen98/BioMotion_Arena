
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Initialize positions of the points
np.random.seed(0)
positions = np.random.rand(num_points, 2) - 0.5

# Define the time steps
num_frames = 200

# Generate the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

dots, = ax.plot([], [], 'wo', markersize=10)

def init():
    dots.set_data([], [])
    return dots,

def animate(frame):
    global positions
    if frame == 0:
        np.random.seed(0)
        positions = np.random.rand(num_points, 2) - 0.5
    theta = np.linspace(0, 2 * np.pi, num_points)
    radius = 0.5 * np.sin(0.1 * frame) + 0.2
    new_positions = np.array([radius * np.cos(theta), radius * np.sin(theta)]).T
    positions += new_positions
    positions %= 1
    positions -= 0.5
    dots.set_data(positions[:, 0], positions[:, 1])
    return dots,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=50, blit=True)

plt.show()
