
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent key joints of the human body
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.6],  # Left shoulder
    [0.6, 0.6],  # Right shoulder
    [0.3, 0.4],  # Left elbow
    [0.7, 0.4],  # Right elbow
    [0.2, 0.2],  # Left wrist
    [0.8, 0.2],  # Right wrist
    [0.5, 0.5],  # Hips
    [0.3, 0.3],  # Left knee
    [0.7, 0.3],  # Right knee
    [0.2, 0.1],  # Left ankle
    [0.8, 0.1],  # Right ankle
    [0.4, 0.7],  # Left hip
    [0.6, 0.7],  # Right hip
    [0.5, 0.9]   # Chin
])

# Define the range of motion for each joint (to simulate lying down)
motion_amplitude = 0.02  # Small amplitude to reflect heaviness
motion_frequency = 0.1   # Low frequency to reflect slow, sad movement

# Function to update the positions of the points over time
def update(frame):
    global positions
    # Apply small oscillations to simulate lying down with heaviness
    for i in range(len(positions)):
        # Add sinusoidal motion to each point
        positions[i][0] += motion_amplitude * np.sin(motion_frequency * frame + i)
        positions[i][1] += motion_amplitude * np.cos(motion_frequency * frame + i)
    
    # Update the scatter plot data
    scatter.set_offsets(positions)

# Initialize the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look
positions = initial_positions.copy()

# Create a scatter plot for the points
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create the animation
animation = FuncAnimation(fig, update, frames=range(100), interval=50, blit=False)

# Show the animation
plt.show()
