
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These coordinates represent a person lying down
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.3, 0.7],  # Left elbow
    [0.7, 0.7],  # Right elbow
    [0.2, 0.6],  # Left wrist
    [0.8, 0.6],  # Right wrist
    [0.5, 0.5],  # Chest
    [0.4, 0.4],  # Left hip
    [0.6, 0.4],  # Right hip
    [0.3, 0.3],  # Left knee
    [0.7, 0.3],  # Right knee
    [0.2, 0.2],  # Left ankle
    [0.8, 0.2],  # Right ankle
    [0.5, 0.1]   # Feet (center)
])

# Define the number of frames for the animation
num_frames = 50

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Function to update the animation frame
def update(frame):
    # Define the motion pattern for lying down
    # Here, we'll slightly adjust the positions to simulate a natural lying-down posture
    positions = initial_positions.copy()
    
    # Smoothly adjust positions over time
    t = frame / num_frames  # Normalized time (0 to 1)
    
    # Adjust head position slightly
    positions[0, 1] = 0.9 - 0.05 * np.sin(t * 2 * np.pi)
    
    # Adjust shoulders and elbows to simulate relaxed arms
    positions[1, 0] += 0.05 * np.cos(t * 2 * np.pi)  # Left shoulder
    positions[2, 0] -= 0.05 * np.cos(t * 2 * np.pi)  # Right shoulder
    positions[3, 0] += 0.1 * np.cos(t * 2 * np.pi)   # Left elbow
    positions[4, 0] -= 0.1 * np.cos(t * 2 * np.pi)   # Right elbow
    
    # Adjust hips and knees to simulate legs spread out
    positions[8, 0] += 0.05 * np.sin(t * 2 * np.pi)  # Left hip
    positions[9, 0] -= 0.05 * np.sin(t * 2 * np.pi)  # Right hip
    positions[10, 0] += 0.1 * np.sin(t * 2 * np.pi)  # Left knee
    positions[11, 0] -= 0.1 * np.sin(t * 2 * np.pi)  # Right knee
    
    # Update scatter plot with new positions
    scatter.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Display the animation
plt.show()
