
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the 15 point-lights representing the sadman
positions = [
    (0, 10), ( 4, 2 ), ( 6, 3 ), ( 7, 4 ), ( 8, 5 ),
    ( 9, 6 ), ( 10, 7 ), ( 12, 8 ), ( 13, 9 ), ( 14, 10 ),
    ( 15, 12 ), ( 14, 13 ), ( 13, 14 ), ( 12, 15 ), ( 11, 16 )
]

# Function to update the positions of the point-lights
def update(frame):
    global positions
    # Simulate natural, smooth motion by slightly adjusting each position
    for i in range(len(positions)):
        dx, dy = np.random.normal(0, 0, size=(2))
        positions[i] = (positions[i][0] + dx, positions[i][1] + dy)
        # Ensure the points stay within reasonable bounds
        if positions[i][0] <   or positions[i][1] < 1:
            positions[i] = (np.random.uniform(, 15), np.random.uniform(1, 15))

    # Clear the previous frame
    ax.clear()
    # Plot the current frame
    ax.scatter([p[0] for p in positions], [p[1] for p in positions], color='white')
    ax.set_xlim([, 15])
    ax.set_ylim([1, 15])
    ax.set_aspect('equal')
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor('black')

# Set up the animation
ani = FuncAnimation(fig, update, frames=100, interval=10)

plt.show()
