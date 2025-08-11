
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure for the animation
fig, ax = plt.subplots(figsize=(4, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Remove axes

# Define the initial positions for the 15 point-lights
points = np.array([
    [0.5, 0.8],  # Head
    [0.3, 0.7], [0.7, 0.7],  # Shoulders
    [0.2, 0.6], [0.8, 0.6],  # Arms
    [0.5, 0.4], [0.5, 0.3], [0.5, 0.2],  # Torso
    [0.2, 0.2], [0.8, 0.2],  # Hips
    [0.1, 0.1], [0.9, 0.1],  # Legs
    [0.1, 0.0], [0.9, 0.0],  # Feet
    [0.2, 0.05], [0.8, 0.05]   # Heavy weight
])

# Create scatter plot for the point-lights
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=30)


def update(frame):
    angle = np.radians(frame)
    center = np.array([0.5, 0.8])
    
    # Bowing motion transformation
    transform_matrix = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
    ])
    
    # Apply the transformation around the head (center of rotation)
    points_transformed = np.dot(points - center, transform_matrix) + center
    
    # Update scatter plot data
    scat.set_offsets(points_transformed)
    return scat,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 45, 120), interval=50, blit=True)

# Display the animation
plt.show()
