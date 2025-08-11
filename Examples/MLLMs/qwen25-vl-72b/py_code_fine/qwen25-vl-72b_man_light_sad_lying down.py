
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Define the initial positions of the points
initial_positions = [
    (5, 9), (4, 8), (6, 8), (3, 7), (7, 7),
    (2, 6), (8, 6), (1, 5), (9, 5), (0, 4),
    (10, 4), (1, 3), (9, 3), (2, 2), (8, 2)
]

for i, pos in enumerate(initial_positions):
    points[i].set_data(pos)

def update(frame):
    # Update the positions of the points to simulate lying down motion
    new_positions = [
        (5, 9 - frame * 0.1), (4, 8 - frame * 0.1), (6, 8 - frame * 0.1),
        (3, 7 - frame * 0.1), (7, 7 - frame * 0.1), (2, 6 - frame * 0.1),
        (8, 6 - frame * 0.1), (1, 5 - frame * 0.1), (9, 5 - frame * 0.1),
        (0, 4 - frame * 0.1), (10, 4 - frame * 0.1), (1, 3 - frame * 0.1),
        (9, 3 - frame * 0.1), (2, 2 - frame * 0.1), (8, 2 - frame * 0.1)
    ]
    
    for i, pos in enumerate(new_positions):
        points[i].set_data(pos)
    
    return points

ani = animation.FuncAnimation(fig, update, frames=range(100), blit=True, interval=50)
plt.show()
