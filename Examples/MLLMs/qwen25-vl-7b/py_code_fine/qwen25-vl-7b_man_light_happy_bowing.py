
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [0, -3],  # Right hip
    [1, -4],  # Left knee
    [-1, -4],  # Right knee
    [0, -5],  # Left ankle
    [0, -6],  # Right ankle
]

# Define the initial positions
x, y = zip(*positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-7, 1)
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter(x, y, c='w', s=100)

def update(frame):
    # Update the positions based on the frame number
    x_new = []
    y_new = []
    for i in range(len(positions)):
        if i == 0:  # Head
            x_new.append(0)
            y_new.append(0)
        elif i == 1 or i == 2:  # Shoulders
            x_new.append(np.cos(frame * 0.1))
            y_new.append(np.sin(frame * 0.1))
        elif i == 3 or i == 4:  # Hips
            x_new.append(np.cos(frame * 0.1) + 0.5)
            y_new.append(np.sin(frame * 0.1) - 0.5)
        elif i == 5 or i == 6:  # Knees
            x_new.append(np.cos(frame * 0.1) + 0.5)
            y_new.append(np.sin(frame * 0.1) - 1.5)
        elif i == 7 or i == 8:  # Ankles
            x_new.append(np.cos(frame * 0.1) + 0.5)
            y_new.append(np.sin(frame * 0.1) - 2.5)
    
    x, y = zip(*positions)
    scatter.set_offsets(list(zip(x_new, y_new)))
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
