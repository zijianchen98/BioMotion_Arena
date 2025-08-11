
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_lights = 15

# Initial positions of the point-lights forming a sadman
positions = np.array([
    [50, 50],  # Head
    [45, 60],  # Left Shoulder
    [55, 60],  # Right Shoulder
    [40, 70],  # Left Elbow
    [60, 70],  # Right Elbow
    [35, 80],  # Left Hand
    [65, 80],  # Right Hand
    [50, 70],  # Spine
    [48, 80],  # Left Hip
    [52, 80],  # Right Hip
    [45, 90],  # Left Knee
    [55, 90],  # Right Knee
    [43, 95],  # Left Foot
    [57, 95],  # Right Foot
    [50, 90]    # Pelvis
])

# Create scatter plot for point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white')

# Function to update the positions of the point-lights for turning around motion
def update(frame):
    angle = np.radians(frame * 2)
    center = positions[0]  # Rotate around the head position
    positions[:, 0:2] = (positions[:, 0:2] - center) * np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) + center
    scat.set_offsets(positions)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 180), interval=50, blit=False)

# Display the animation
plt.show()
