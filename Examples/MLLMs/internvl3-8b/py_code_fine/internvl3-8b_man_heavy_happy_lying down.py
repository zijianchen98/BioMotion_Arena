
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define points for the human figure
def init_positions():
    return np.array([[1.0, 2.0], [1.0, 3.0], [1.0, 4.0], [1.0, 5.0],
                     [2.0, 6.0], [3.0, 6.0], [4.0, 6.0], [5.0, 6.0],
                     [6.0, 6.0], [7.0, 6.0], [8.0, 6.0], [9.0, 6.0],
                     [10.0, 6.0], [11.0, 6.0], [12.0, 6.0]])

# Initialize positions
positions = init_positions()

def update_positions(i):
    positions[0] = [1.0, 2.0 + i / 1000.0]  # Lying down movement
    positions[1] = [1.0, 3.0]
    positions[2] = [1.0, 4.0]
    positions[3] = [1.0, 5.0]
    positions[4] = [2.0, 6.0]
    positions[5] = [3.0, 6.0]
    positions[6] = [4.0, 6.0]
    positions[7] = [5.0, 6.0]
    positions[8] = [6.0, 6.0]
    positions[9] = [7.0, 6.0]
    positions[10] = [8.0, 6.0]
    positions[11] = [9.0, 6.0]
    positions[12] = [10.0, 6.0]
    positions[13] = [11.0, 6.0]
    positions[14] = [12.0, 6.0]
    return positions

fig, ax = plt.subplots()
ax.set_facecolor('black')

sc = plt.scatter(*positions.T, color='white')

def animate(i):
    sc.set_offsets(update_positions(i))
    return sc,

ani = FuncAnimation(fig, animate, frames=range(1000), interval=50, blit=True)
plt.axis('off')
plt.show()

