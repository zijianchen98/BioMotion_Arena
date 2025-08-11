
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (0, 12 ), ( 12, 12 ), ( 14, 12 ),
    ( 8, 10 ), ( 9, 11 ), ( 10, 11 ),
    ( 6, 10 ), ( 7, 11 ), ( 8, 11 ),
    ( 4, 10 ), ( 5, 11 ), ( 6, 11 ),
    ( 2, 10 ), ( 3, 11 ), ( 4, 11 )
]

def update_positions(positions):
    # Update the positions to simulate sitting down
    new_positions = []
    for x i in range(len(positions)):
        if i < 5:
            new_positions.append((positions[i][0] - 1, positions[i][1]))
        elif i < 10:
            new_positions.append((positions[i][0], positions[i][1] - 1))
        else:
            new_positions.append((positions[i][0], positions[i][1] + 1))
    return new_positions

def animate(frame, positions, scatter):
    new_positions = update_positions(positions)
    for i, pos in enumerate(new_positions):
        scatter[i].set_data(pos)
    return scatter

fig, ax = plt.subplots()
ax.set_xlim(0, 16)
ax.set_ylim(1, 13)
ax.scatter = [ax[plt.scatter([], []) for _ in range(15)]

ani = FuncAnimation(fig, animate, frames=30, fargs=(initial_positions, scatter), interval=100, blit=True)

plt.show()
