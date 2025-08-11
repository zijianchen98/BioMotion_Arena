
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the 15 points that make up the "happyman" running animation
points = {
    'head': [0 for w in range(15) for t in (0, 6 ) ],
    'torso': [ w for w in range(15) for t in ( 1, 4, 7, 10 ) ],
    'left_arm': [ w for w in range(15) for t in ( 2, 9 ) ],
    'right_arm': [ w for w in range(15) for t in ( 3, 8 ) ],
    'left_leg': [ w for w in range(15) for t in ( 5, 12 ) ],
    'right_leg': [ w for w in range(15) for t in ( 0, 13 ) ]
}

# Define the x function to update the positions of the points
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 16)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    # Update each point's position based on the frame number
    for name, positions in points.items():
        x = positions[frame % len(positions)]
        if name == 'head':
            ax.scatter([x], [y], color='w', s=100)
        elif name in ['left_arm', 'right_arm', 'left_leg', 'right_leg']:
            ax.scatter([x], [y], color='w', s=50)
        else:
            ax.scatter([x], [y], color='w', s=50)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 3))

# Set the background to black
ax.set_facecolor('k')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0), interval=100, blit=False)

# Show the animation
plt.show()
