
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [2, -1], # Right shoulder
    [1, -2], # Left hip
    [2, -2], # Right hip
    [1, -3], # Left knee
    [2, -3], # Right knee
    [1, -4], # Left ankle
    [2, -4], # Right ankle
]

# Define the initial positions
initial_positions = np.array(positions)

# Define the function to update the positions
def update(frame):
    global positions
    # Simulate a sitting motion by adjusting the positions
    for i in range(len(positions)):
        if i == 0:  # Head
            positions[i][1] -= frame / 10  # Slightly move up
        elif i == 1 or i == 2:  # Shoulders
            positions[i][1] += frame / 10  # Slightly move down
        elif i == 3 or i == 4:  # Hips
            positions[i][1] += frame / 10  # Slightly move down
        elif i == 5 or i == 6:  # Knees
            positions[i][1] += frame / 10  # Slightly move down
        elif i == 7 or i == 8:  # Ankles
            positions[i][1] += frame / 10  # Slightly move down
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-5, 0)
ax.axis('off')

# Plot the initial positions
for pos in initial_positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Display the animation
plt.show()
