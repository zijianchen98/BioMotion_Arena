
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing key joints of a human body
points = np.array([
    [0, 0],  # Pelvis
    [0, 1],  # Right Hip
    [1, 2],  # Right Knee
    [1, 3],  # Right Ankle
    [0, -1], # Left Hip
    [-1, -2],# Left Knee
    [-1, -3],# Left Ankle
    [0, 2],  # Spine
    [0, 3],  # Chest
    [0, 4],  # Neck
    [0.5, 5],# Right Shoulder
    [1.5, 6],# Right Elbow
    [2.5, 7],# Right Wrist
    [-0.5, 5],# Left Shoulder
    [-1.5, 6],# Left Elbow
    [-2.5, 7] # Left Wrist
])

# Define the angles for the turning motion
angles = np.linspace(0, 2 * np.pi, 100)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

def update(frame):
    # Rotate the points around the origin
    angle = angles[frame]
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_points = np.dot(points, rotation_matrix.T)
    
    # Update the scatter plot
    scat.set_offsets(rotated_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(angles), interval=50, blit=True)

# Display the animation
plt.show()
