
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
background_color = 'black'
point_color = 'white'

# Initial positions and angles for the man's body parts in forward roll
initial_positions = np.array([
    [0, 0],     # Head
    [-0.2, 0.6], # Left Shoulder
    [0.2, 0.6],  # Right Shoulder
    [-0.2, 0.8], # Left Elbow
    [0.2, 0.8],  # Right Elbow
    [-0.2, 1],   # Left Wrist
    [0.2, 1],    # Right Wrist
    [0, 0.3],    # Chest
    [0, -0.3],   # Hip
    [-0.2, -0.6],# Left Knee
    [0.2, -0.6], # Right Knee
    [-0.2, -0.9],# Left Ankle
    [0.2, -0.9], # Right Ankle
    [-0.2, -1],  # Left Foot
    [0.2, -1]    # Right Foot
])

# Angles for forward roll
angles = np.linspace(0, 2 * np.pi, frames)

# Function to update positions for each frame
def update(frame):
    positions = initial_positions.copy()
    angle = angles[frame]
    
    # Rotate around the center of mass (approximated as the hip position)
    center_of_mass = np.mean(positions[8:], axis=0)
    rotated_positions = positions - center_of_mass
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = np.dot(rotated_positions, rotation_matrix.T)
    rotated_positions += center_of_mass
    
    # Update scatter plot data
    scatter.set_offsets(rotated_positions)
    return scatter,

# Set up figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor(background_color)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=point_color)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show animation
plt.show()
