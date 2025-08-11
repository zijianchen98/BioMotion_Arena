
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15  # Total number of point-lights
frames = 100  # Number of frames in the animation
background_color = 'black'  # Background color
point_color = 'white'  # Point light color

# Initialize points for the "sad woman" in a T-Pose
points = np.array([
    [0, 3],   # Head
    [-1, 1],  # Left shoulder
    [1, 1],   # Right shoulder
    [-1, 0],  # Left elbow
    [1, 0],   # Right elbow
    [-1, -1], # Left wrist
    [1, -1],  # Right wrist
    [0, 2],   # Chest
    [-1, -2], # Left hip
    [1, -2],  # Right hip
    [-1, -3], # Left knee
    [1, -3],  # Right knee
    [-1, -4], # Left ankle
    [1, -4],  # Right ankle
    [0, -5],  # Pelvis
    [0, -6]   # Foot
])

# Define rotation function
def rotate(points, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor(background_color)
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 3)
ax.axis('off')  # Turn off the axis

# Initialize scatter plot
scatter = ax.scatter([], [], color=point_color)

# Update function for animation
def update(frame):
    ax.clear()
    ax.set_facecolor(background_color)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-7, 3)
    ax.axis('off')
    
    # Compute the angle for rotation
    angle = frame * (2 * np.pi / frames)
    rotated_points = rotate(points, angle)
    
    # Update scatter plot data
    scatter = ax.scatter(rotated_points[:, 0], rotated_points[:, 1], color=point_color)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=False, interval=50)

# Show the animation
plt.show()
