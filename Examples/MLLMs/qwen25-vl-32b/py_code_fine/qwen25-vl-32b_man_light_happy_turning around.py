
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions represent a standing pose
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.2], # Left shoulder
    [0.1, -0.2],  # Right shoulder
    [-0.2, -0.4], # Left elbow
    [0.2, -0.4],  # Right elbow
    [-0.3, -0.6], # Left wrist
    [0.3, -0.6],  # Right wrist
    [0.0, -0.8],  # Torso
    [-0.1, -1.0], # Left hip
    [0.1, -1.0],  # Right hip
    [-0.2, -1.2], # Left knee
    [0.2, -1.2],  # Right knee
    [-0.3, -1.4], # Left ankle
    [0.3, -1.4],  # Right ankle
    [0.0, -1.6]   # Feet center
])

# Define the range of angles for the turning motion
angles = np.linspace(0, 2 * np.pi, 100)  # Full rotation

# Function to rotate a point around the origin
def rotate_point(point, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(rotation_matrix, point)

# Function to update the positions based on the current angle
def update_positions(positions, angle):
    # Rotate the entire body around the torso (center of mass)
    torso_position = positions[7]  # Torso position
    rotated_positions = []
    for point in positions:
        relative_point = point - torso_position
        rotated_point = rotate_point(relative_point, angle)
        rotated_positions.append(rotated_point + torso_position)
    return np.array(rotated_positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.0, 0.5)
ax.axis('off')  # Hide axes
ax.set_aspect('equal')

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white', edgecolors='none')

# Animation function
def animate(i):
    angle = angles[i]
    updated_positions = update_positions(initial_positions, angle)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(angles), interval=50, blit=True)

# Display the animation
plt.show()
