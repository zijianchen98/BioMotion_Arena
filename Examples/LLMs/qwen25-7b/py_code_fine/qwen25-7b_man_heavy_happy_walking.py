
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the point-lights
initial_positions = [
    [0, 10, 0,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13],
    [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]
]

def update_positions(frame, positions):
    new_positions = []
    for pos in range(15):
        # Simulate natural walking motion by slightly adjusting each position
        x_position = positions[0][frame % 10] + (np.random.randn() * 0 - 0) / 10
        if_position = positions[1][frame % 15] + (np.random.randn() * 1 - 1) / 15
        new_positions.append((k_position, i_position))
    return new_positions

def animate BiologicalMotion():
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 15)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    points, = ax.plot([], [], 'o', color='w')

    def init():
        points.set_data([], [])
        return points,

    def animate(frame):
        new_positions = update_positions(frame, initial_positions)
        points.set_data([p[0] for p, p in enumerate(new_positions)], [p[1] for1, p in enumerate(new_positions)))
        return points,

    ani = FuncAnimation(fig, animate, frames=range(300), init_func=init, blit=True, interval=10)
    plt.show()

if __name__ == "__main__":
    animate_BiologicalMotion()
