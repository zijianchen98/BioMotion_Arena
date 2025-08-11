
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to animate the sadman rolling forward
def animate_forward_rolling():
    # Generate initial positions
    positions = np.array([
        [0, 0], [0, 1], [1, 1], [1, 2], [2, 2],
        [3, 2], [4, 2], [5, 2], [6, 2], [6, 3],
        [6, 4], [5, 4], [4, 4], [3, 4], [2, 4]
    ])

    def update(frame):
        # Apply slow sine wave for realistic rolling
        x_positions = positions[:, 0] + np.sin(frame / 100)
        y_positions = positions[:, 1] + np.cos(frame / 100)
        ax.clear()
        ax.scatter(x_positions, y_positions, c='white', s=250, alpha=1)
        ax.set_xlim(-0.5, 7)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update, frames=1000, interval=50)

    plt.show()

# Run the animation
animate_forward_rolling()
