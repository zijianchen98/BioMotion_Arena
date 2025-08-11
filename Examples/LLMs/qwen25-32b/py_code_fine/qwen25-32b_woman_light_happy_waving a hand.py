
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights in the initial frame
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.6],  # Shoulder Left
    [0.6, 0.6],  # Shoulder Right
    [0.3, 0.4],  # Elbow Left
    [0.7, 0.4],  # Elbow Right
    [0.2, 0.2],  # Hand Left (Waving Hand)
    [0.8, 0.2],  # Hand Right
    [0.5, 0.5],  # Torso
    [0.4, 0.3],  # Hip Left
    [0.6, 0.3],  # Hip Right
    [0.3, 0.1],  # Knee Left
    [0.7, 0.1],  # Knee Right
    [0.2, 0.0],  # Foot Left
    [0.8, 0.0],  # Foot Right
    [0.5, 0.9]   # Top of head
])

# Create figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Function to update the position of the waving hand
def update(frame):
    # Define the waving motion for the left hand (index 5)
    angle = np.radians(-45 * np.sin(np.radians(frame)))
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    offset = np.array([0.1, 0.1]) * np.sin(np.radians(frame))
    
    # Apply transformation to the left hand
    initial_positions[5] = np.dot(rotation_matrix, initial_positions[5] - [0.5, 0.2]) + [0.5, 0.2] + offset
    
    scatter.set_offsets(initial_positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

plt.show()
