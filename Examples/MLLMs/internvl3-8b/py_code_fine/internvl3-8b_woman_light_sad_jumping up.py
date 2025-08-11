
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_positions():
    # Define the positions of the lights for jumping up
    positions = [
        [(i, j) for j in range(4, 5)] if i == 5 else 
        [(i, j) for j in range(4, 3)] if i == 6 else 
        [(i, j) for j in range(4, 2)] if i == 7 else 
        [(i, j) for j in range(4, 1)] if i == 8 else 
        [(i, j) for j in range(3, 0)] if i == 9 else
        [(i, j) for j in range(2, -1)] if i == 10 else
        [(i, j) for j in range(1, -2)] if i == 11 else
        [(i, j) for j in range(0, -3)] if i == 12 else
        [(i, j) for j in range(-1, -4)] if i == 13 else
        [(i, j) for j in range(-2, -5)] if i == 14 else
        [(i, j) for j in range(-3, -6)] if i == 15 else []
        for i in range(20)
    ]
    return positions

def update_positions(frames):
    # Get positions for the current frame
    positions = generate_positions()
    # Make sure we only get positions up to the current frame number
    positions = positions[:frames]
    # Convert list of tuples to array for plotting
    x = np.array([pos[0] for pos in positions])
    y = np.array([pos[1] for pos in positions])
    return x, y

fig, ax = plt.subplots()
ax.set_axis_off()
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)

x, y = update_positions(0)
scatter = ax.scatter(x, y, color='white', s=200)

def animate(frame):
    x, y = update_positions(frame)
    scatter.set_offsets(np.c_[x, y])
    return scatter,

ani = FuncAnimation(fig, animate, frames=200, interval=50)
plt.show()
