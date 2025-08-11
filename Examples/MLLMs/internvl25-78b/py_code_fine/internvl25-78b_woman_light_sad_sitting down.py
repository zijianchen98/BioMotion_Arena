
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Coordinates for a sad woman sitting down motion
initial_coords = [
    [0, 4], [0, 5], [0, 6], [0, 7], [0, 8],
    [-1, 5], [-1, 6], [1, 5], [1, 6],
    [-2, 7], [2, 7],
    [-1, 8], [1, 8], [-2, 9], [2, 9],
]

def update(frame):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(3, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    for i, (x, y) in enumerate(initial_coords):
        # Adjust positions over frames to simulate sitting down
        new_x = x + 0.05 * np.sin(frame / 5.0)
        new_y = y - 0.02 * frame
        ax.plot(new_x, new_y, 'wo')

fig, ax = plt.subplots(facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
