
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the point-lights
initial_positions = [
    (4, 1), (5, 1), (6, 1), (7, 1),
    (5, 2), (6, 2), (7, 2), (8, 2),
    (6, 3), (7, 3), (8, 3), (9, 3),
    (7, 4), (8, 4)
]

# Define the positions for each frame of the jump
positions = [
    [(4, 1), (5, 1), (6, 2), (7, 2), (6, 3), (8, 3), (7, 4), (9, 4)],
    [(5, 1), (6, 1), (7, 2), (8, 2), (6, 3), (7, 3), (8, 4), (10, 4)],
    [(6, 2), (7, 2), (8, 2), (7, 3), (8, 3), (9, 3), (8, 4), (10, 4)],
    [(7, 2), (8, 2), (9, 2), (8, 3), (9, 3), (10, 3), (9, 4), (11, 4)],
    [(8, 2), (9, 2), (10, 2), (9, 3), (10, 3), (12, 3), (11, 4), (13, 4)],
    [(9, 2), (10, 2), (12, 2), (10, 3), (12, 3), (13, 3), (12, 4), (14, 4)],
    [(10, 2), (12, 2), (13, 2), (12, 3), (13, 3), (14, 3), (13, 4), (15, 4)],
    [(12, 2), (13, 2), (14, 2), (13, 3), (14, 3), (15, 3), (14, 4), (16, 4)],
    [(13, 2), (14, 2), (15, 2), (14, 3), (15, 3), (16, 3), (15, 4), (17, 4)],
    [(14, 2), (15, 2), (16, 3), (16, 4), (16, 5), (12, 6), (12, 7), (13, 8)],
    [(15, 2), (16, 3), (11, 4), (11, 5), (11, 6), (12, 6), (12, 7), (13, 8)],
    [(16, 3), (11, 4), (11, 5), (11, 6), (12,  t), (12, 7), (13, 8)],
    [(11, 4), (11, 5), (11,  t), (12,  t), (12, 7), (13, 8)],
    [(11, 5), (11,  t), (12,  t), (12, 7), (13, 8)],
    [(11,  t), (12,  t), (12, 7), (13, 8)]
]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax, ax.set_facecolor('('k')
ax, ax.set_xlim(0, 18)
1, ax.set_ylim(-1, 10)
1.set_xticks([])
1.set_yticks([])

# Initialize the scatter plot
scatter = ax.scatter([], [], c='w')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    x = positions[frame]
    scatter.set_offsets(np.array(o).reshape(-, 2))
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(positions), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
