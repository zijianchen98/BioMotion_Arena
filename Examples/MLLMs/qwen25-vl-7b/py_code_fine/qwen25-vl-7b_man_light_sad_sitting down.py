
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Left knee
    [0, -3],  # Right hip
    [-2, -3],  # Right knee
]

# Define the initial positions
x, y = zip(*positions)

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 0)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter(x, y, c='w', s=100)

def update(frame):
    # Update the positions based on the sadman sitting down
    x[0] -= frame / 100  # Head moves slightly forward
    x[1] += frame / 100  # Left shoulder moves slightly backward
    x[2] += frame / 100  # Right shoulder moves slightly backward
    x[3] -= frame / 100  # Left hip moves slightly forward
    x[4] -= frame / 100  # Left knee moves slightly forward
    x[5] -= frame / 100  # Right hip moves slightly forward
    x[6] -= frame / 100  # Right knee moves slightly forward
    
    y[0] -= frame / 100  # Head moves slightly downward
    y[1] -= frame / 100  # Left shoulder moves slightly downward
    y[2] -= frame / 100  # Right shoulder moves slightly downward
    y[3] -= frame / 100  # Left hip moves slightly downward
    y[4] -= frame / 100  # Left knee moves slightly downward
    y[5] -= frame / 100  # Right hip moves slightly downward
    y[6] -= frame / 100  # Right knee moves slightly downward
    
    scatter.set_offsets(np.column_stack((x, y)))
    return scatter,

ani = FuncAnimation(fig, update, frames=np.arange(0, 1000), interval=20, blit=True)
plt.show()
