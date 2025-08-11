
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis.
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axes for better visualization.

# Initial positions for the 15 point-lights representing the sadman bowing.
positions = np.array([
    [5, 9],  # Head
    [4, 8],  # Shoulder left
    [6, 8],  # Shoulder right
    [3.5, 7],  # Elbow left
    [6.5, 7],  # Elbow right
    [3, 6],  # Hand left
    [7, 6],  # Hand right
    [5, 7],  # Chest
    [5, 6],  # Waist
    [4, 5],  # Hip left
    [6, 5],  # Hip right
    [3.5, 4],  # Knee left
    [6.5, 4],  # Knee right
    [3, 3],  # Foot left
    [7, 3]   # Foot right
])

# Scatter plot for the point-lights.
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

def update(num):
    global positions
    # Bowing motion simulation.
    amplitude = 0.1
    frequency = 0.05
    phase_shift = num * frequency
    
    # Apply a sine wave transformation to simulate the bowing action.
    positions[:, 1] -= amplitude * np.sin(phase_shift + np.linspace(0, np.pi, len(positions)))
    
    # Update scatter plot data.
    scat.set_offsets(positions)

# Create the animation.
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
