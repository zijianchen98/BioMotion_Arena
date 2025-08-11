
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define initial positions
positions = np.array([
    [ -1, 73 ], [ 0, 72 ], [ 1, 72 ], [ 10, 71 ],
    [ 4, 61 ], [ 9, 60 ], [ 7, 50 ], [ 8, 40 ],
    [ 2, 31 ], [ 5, 30 ], [ 12, 30 ], [ 6, 22 ],
    [ 13, 22 ], [ 3, 13 ], [ 14, 13 ]
])

# Function to update the positions
def update_positions(i):
    global positions, speed
    positions += speed
    return positions

# Generate an animation
def animate_motion():
    fig = plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, aspect='equal', xlim=(-5, 15), ylim=(0, 80), xticks=[], yticks=[])
    ax.set_facecolor('black')
    points, = ax.plot([], [], 'o', color='white', markersize=10)
        
    def init():
        points.set_data(positions[:, 0], positions[:, 1])
        return points,
        
    ani = FuncAnimation(fig, lambda i: update_positions(i), frames=len(positions), interval=20, init_func=init, blit=True)
    plt.show()
    ani.save('sadman_jump.gif', writer='imagemagick')

def start_animation():
    animate_motion()

if __name__ == "__main__":
    start_animation()
