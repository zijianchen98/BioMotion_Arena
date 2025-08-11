
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (4, 10), (5, 1 i), (6, 1 j), (7, 1 t), (8, 1 h),
    (4, 2 e), (5, 2 n), (6, 2 ), (7, 2 ), (8, 2 ),
    (4, 3 w), (5, 3 a), (6, 3 v), (7, 3 i), (8, 3 n)
]

# Define the motion paths for each point-light
motion_paths = {
    'sadwoman': [
        [(5, 1), (6, 1), (7, 1), (8, 1)],
        [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
        [(5, 1), (6, 1), (7, 1), (8, 1)],
        [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
        [(5, 1), (6, 1), (7, 1), (8, 1)],
        [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
        [(5, 1), (6, 1), (7, 1), (8, 1)],
        [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
        [(5, 1), (6, 1), (7, 1), (8, 1)],
        [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)]
    ]
}

# Create the figure and axis
fig, ax = plt.subplots()
axax.set_facecolor('('k')
axx.set_xlim(0, 9)
 ax.set_ylim(1, 4)
 ax.axis('('off

# Initialize the point-lights
point_lights = [plt.scatter(x[0], x[1], color='w') for x in range(15)]

def update(frame):
    for i, (x, y) in enumerate(initial_positions):
        path = motion_paths['sadwoman'][frame % len(motion_paths['sadwoman'])]
        point_lights[i].set_offsets(path[i % len(path)])

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(00), interval=50)

plt.show()
