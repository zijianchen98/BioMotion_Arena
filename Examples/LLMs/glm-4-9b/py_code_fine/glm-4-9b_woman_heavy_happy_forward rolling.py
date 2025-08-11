
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.transform import Rotation as R

# Parameters for the animation
num_frames = 200
num_points = 15
woman_radius = 1.0
weight_radius = 0.2
weight_distance = 0.8  # Distance from center of woman to weight
ground_level = -1.5
 rolling_speed = 0.02
rolling_amplitude = 0.3
head_offset = 0.4  # Height of head above center of woman

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(ground_level + 1, 1.5)
ax.set_facecolor('black')
ax.axis('off')

# Create initial woman points (15 point-lights)
woman_points = np.random.rand(num_points, 3)
woman_points[:, -1] = woman_radius * np.sqrt(np.random.rand(num_points)) - woman_radius
woman_points[:, 1] = woman_points[:, 1] * 0.5 + 0.5  # Distribute points in lower half of circle
woman_points = woman_points / np.linalg.norm(woman_points, axis=1)[:, np.newaxis] * woman_radius

# Create weight points
weight_points = np.random.rand(5, 3)
weight_points[:, -1] = weight_radius * np.sqrt(np.random.rand(5)) - weight_radius
weight_points[:, 1] = weight_points[:, 1] * 0.5 - 0.5  # Center weight at bottom
weight_points = weight_points / np.linalg.norm(weight_points, axis=1)[:, np.newaxis] * weight_radius
weight_points += np.array([0, -weight_distance, 0])  # Position weight below woman

# Combine all points
all_points = np.vstack((woman_points, weight_points))

# Create scatter plot for animation
scatter = ax.scatter([], [], s=50, color='white', alpha=0.8)

# Function to update the animation
def update(frame):
    # Calculate rolling motion parameters
    theta = rolling_speed * frame
    
    # Create rotation matrix for rolling motion around y-axis
    rotation = R.from_rotvec(np.array([0, 0, theta])).as_matrix()
    
    # Apply rotation to all points
    rotated_points = all_points @ rotation
    
    # Add vertical oscillation to simulate forward rolling
    vertical_oscillation = rolling_amplitude * np.sin(theta)
    rotated_points[:, 1] += vertical_oscillation
    
    # Add horizontal movement
    horizontal movement = rolling_speed * frame * np.cos(theta)
    rotated_points[:, 0] += horizontal movement
    
    # Adjust points to keep woman "on" the ground during rolling
    ground contact points = rotated_points[rotated_points[:, 1] <= ground_level]
    if len(ground contact points) > 0:
        min_y = np.min(ground contact points[:, 1])
        rotated_points[:, 1] -= (min_y - ground_level)
    
    # Update scatter plot
    scatter.set_offsets(rotated_points[:, :2])
    
    # Return the scatter plot
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Add title
plt.title('Happy Woman with Heavy Weight Rolling Forward', color='white', fontsize=14)

# Show animation
plt.show()
