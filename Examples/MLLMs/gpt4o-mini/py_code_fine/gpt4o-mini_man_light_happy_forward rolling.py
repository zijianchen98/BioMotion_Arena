
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initial positions of the points
initial_positions = np.array([
    [0, 3], [1, 4], [-1, 4], [1, 2], [-1, 2],
    [0, 0], [0.5, -1], [-0.5, -1], [0.5, -3],
    [-0.5, -3], [1, -2], [-1, -2], [0, -4],
    [1.5, -2], [-1.5, -2], [0, -5]
])

# Base positions for rolling motion
def update(frame):
    # Create a forward rolling effect by moving points
    roll_offset = np.array([0, -0.1 * frame])  # roll down
    updated_positions = initial_positions + roll_offset
    points.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
