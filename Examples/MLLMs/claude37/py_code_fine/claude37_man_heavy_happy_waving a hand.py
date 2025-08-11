
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point-lights
num_lights = 15

# Initialize positions for the point-lights
# The following coordinates need to be structured to represent a person with arms
# Defined for a waving motion
original_positions = np.array([
    [0, 0.5],   # Head
    [-0.1, 0.4],  # Left shoulder
    [0.1, 0.4],  # Right shoulder
    [-0.2, 0.3],  # Left elbow
    [0.2, 0.3],   # Right elbow
    [-0.3, 0.2],  # Left hand
    [0.3, 0.2],   # Right hand
    [0, 0],       # Torso
    [-0.5, -0.5], # Left foot
    [0.5, -0.5],  # Right foot
    [0, -0.3],    # Pelvis
    [-0.1, -0.2], # Left knee
    [0.1, -0.2],  # Right knee
    [-0.15, 0.2], # Left wrist
    [0.15, 0.2],  # Right wrist
    [-0.25, 0.1]  # Left lowered hand (for waving)
])

# Prepare a point-light scatter object
points, = ax.plot([], [], 'wo', markersize=12)

# Update function for animation
def update(frame):
    # Basic waving motion based on sine wave for smoothness
    y_offset = 0.1 * np.sin(frame * 0.1)
    
    # Adjust wrist positions for waving
    current_positions = np.copy(original_positions)
    current_positions[13, 1] += y_offset   # Right wrist swinging
    
    # Update points
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Display the animation
plt.show()
