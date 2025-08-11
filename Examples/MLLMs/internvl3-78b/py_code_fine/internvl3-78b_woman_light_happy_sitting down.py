
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial positions of the points (simplified representation)
initial_positions = np.array([
    [4, 6],  # head
    [5, 6],  # head
    [3, 5],  # upper body
    [4, 5],  # upper body
    [5, 5],  # upper body
    [6, 5],  # upper body
    [2, 4],  # left arm
    [3, 4],  # left arm
    [4, 4],  # body center
    [5, 4],  # body center
    [6, 4],  # right arm
    [7, 4],  # right arm
    [3, 3],  # left leg
    [4, 3],  # left leg
    [5, 3],  # right leg
])

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
points, = ax.plot([], [], 'bo')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    positions = initial_positions.copy()
    # Example movements: moving down
    amplitude = 0.1
    positions[:, 1] += amplitude * np.sin(0.2 * frame)
    
    # Update points' positions
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = FuncAnimation(fig, animate, frames=range(100), init_func=init, blit=True)

plt.axis('off')  # Hide the axes
plt.show()
