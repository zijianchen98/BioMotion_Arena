
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the coordinates of the points representing the sad woman with heavy weight walking
def initialize_positions():
    positions = np.array([
        [0.5, 0.8],  # Head
        [0.4, 0.7],  # Shoulder left
        [0.6, 0.7],  # Shoulder right
        [0.3, 0.5],  # Elbow left
        [0.7, 0.5],  # Elbow right
        [0.2, 0.3],  # Hand left
        [0.8, 0.3],  # Hand right
        [0.4, 0.4],  # Hip left
        [0.6, 0.4],  # Hip right
        [0.3, 0.2],  # Knee left
        [0.7, 0.2],  # Knee right
        [0.2, 0.1],  # Foot left
        [0.8, 0.1],  # Foot right
        [0.4, 0.6],  # Torso left
        [0.6, 0.6]   # Torso right
    ])
    return positions

# Update function for the animation
def update(frame):
    global positions
    positions += np.array([np.sin(frame / 10.0) * 0.02, np.cos(frame / 10.0) * 0.02])
    
    # Simulate walking by moving feet in opposite directions
    positions[11][0] += np.sin(frame / 5.0) * 0.05  # Left foot
    positions[12][0] -= np.sin(frame / 5.0) * 0.05  # Right foot
    
    # Adjust arms to move opposite to legs
    positions[5][0] -= np.sin(frame / 5.0) * 0.05  # Left hand
    positions[6][0] += np.sin(frame / 5.0) * 0.05  # Right hand
    
    scat.set_offsets(positions)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes
positions = initialize_positions()
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

plt.show()
