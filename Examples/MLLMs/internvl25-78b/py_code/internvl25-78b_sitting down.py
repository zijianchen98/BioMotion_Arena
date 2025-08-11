
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points for the sitting down motion
initial_positions = np.array([
    [0.0, 1.0], [0.5, 1.0], [-0.5, 1.0],
    [0.0, 0.5], [0.5, 0.5], [-0.5, 0.5],
    [0.0, 0.0], [0.5, 0.0], [-0.5, 0.0],
    [0.0, -0.5], [0.5, -0.5], [-0.5, -0.5],
    [0.0, -1.0], [0.5, -1.0], [-0.5, -1.0]
])

# Frame by frame update function
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-2, 2)
    ax.axis('off')

    # Calculate new positions
    factor = 0.2 * frame / 10.0
    new_positions = initial_positions * [1, 1 + factor]

    # Plot the new positions
    ax.scatter(new_positions[:, 0], new_positions[:, 1], c='white')

# Animation setup
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=20, interval=100, repeat=False)

plt.show()
