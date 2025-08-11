
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the points representing the bowing man
def get_positions(t):
    # Define the base positions of the points
    positions = np.array([
        [0.5, 1],  # Head
        [0.4, 0.8], [0.6, 0.8],  # Shoulders
        [0.5, 0.7],  # Chest
        [0.5, 0.3],  # Pelvis
        [0.3, 0.5], [0.7, 0.5],  # Hips
        [0.3, 0.7], [0.3, 0.4], [0.3, 0.1],  # Left arm
        [0.7, 0.7], [0.7, 0.4], [0.7, 0.1],  # Right arm
        [0.5, 0.1]  # Feet
    ])
    
    # Modify the positions to show a bowing motion
    angle = np.sin(t / 10)
    positions[:, 1] -= angle * 0.2  # Move vertically down
    positions[0, 1] += angle * 0.1  # Head moves slightly up
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes

points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    x, y = get_positions(i).T
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100, 0.1), init_func=init, interval=20, blit=True)

plt.show()
