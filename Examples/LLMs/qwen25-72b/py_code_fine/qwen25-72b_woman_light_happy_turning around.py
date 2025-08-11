
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the key joints of a human body
points = [
    (0, 0),  # Hip center
    (-0.1, 0.1),  # Left hip
    (-0.2, 0.2),  # Left knee
    (-0.3, 0.3),  # Left ankle
    (0.1, 0.1),  # Right hip
    (0.2, 0.2),  # Right knee
    (0.3, 0.3),  # Right ankle
    (0, 0.5),  # Waist
    (-0.1, 0.6),  # Left shoulder
    (-0.2, 0.7),  # Left elbow
    (-0.3, 0.8),  # Left wrist
    (0.1, 0.6),  # Right shoulder
    (0.2, 0.7),  # Right elbow
    (0.3, 0.8),  # Right wrist
    (0, 1.0)  # Head
]

# Convert points to a numpy array
points = np.array(points)

# Define the rotation angle for turning around
angle = np.linspace(0, 2 * np.pi, 100)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot for the point-lights
sc = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

def update(frame):
    # Rotate the points around the origin
    rotation_matrix = np.array([
        [np.cos(angle[frame]), -np.sin(angle[frame])],
        [np.sin(angle[frame]), np.cos(angle[frame])]
    ])
    rotated_points = np.dot(points, rotation_matrix.T)
    
    # Update the scatter plot data
    sc.set_offsets(rotated_points)
    return sc,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(angle), interval=50, blit=True)

# Display the animation
plt.show()
