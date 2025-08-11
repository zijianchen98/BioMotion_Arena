
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Initialize positions of the point lights (simplified for demonstration)
positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.7],  # Left Shoulder
    [0.6, 0.7],  # Right Shoulder
    [0.3, 0.5],  # Left Elbow
    [0.7, 0.5],  # Right Elbow
    [0.2, 0.3],  # Left Wrist
    [0.8, 0.3],  # Right Wrist
    [0.5, 0.5],  # Chest
    [0.5, 0.3],  # Waist
    [0.4, 0.2],  # Left Hip
    [0.6, 0.2],  # Right Hip
    [0.3, 0.1],  # Left Knee
    [0.7, 0.1],  # Right Knee
    [0.4, 0.0],  # Left Ankle
    [0.6, 0.0]   # Right Ankle
])

# Function to update the positions of the point lights
def update(frame):
    # Simple forward rolling motion
    angle = np.radians(frame * 2)
    x_offset = 0.5 + 0.2 * np.sin(angle)
    y_offset = 0.5 - 0.2 * np.cos(angle)
    
    # Update positions based on the current frame
    new_positions = positions.copy()
    new_positions[:, 0] = positions[:, 0] + (x_offset - 0.5)
    new_positions[:, 1] = positions[:, 1] + (y_offset - 0.5)
    
    # Update scatter plot
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Turn off axis

# Create scatter plot of point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), blit=True, interval=30)

# Display the animation
plt.show()
