
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set the figure size
fig, ax = plt.subplots()
ax.axis('off')
ax.set_aspect('equal')

# Define the joint positions for a sad walking woman (15 points)
# These points are placeholders and may need adjustment for a realistic walking motion
joints = np.array([
    [0.0, 1.0],  # Head
    [-0.1, 0.5],  # Neck
    [-0.2, 0.0],  # Torso
    [-0.3, -0.5],  # Left Shoulder
    [-0.4, -1.0],  # Left Elbow
    [-0.5, -1.5],  # Left Hand
    [-0.2, -1.0],  # Left Hip
    [-0.3, -1.5],  # Left Knee
    [-0.4, -2.0],  # Left Foot
    [0.2, 0.0],   # Right Shoulder
    [0.4, -0.5],  # Right Elbow
    [0.5, -1.0],  # Right Hand
    [0.2, -1.0],  # Right Hip
    [0.3, -1.5],  # Right Knee
    [0.4, -2.0]   # Right Foot
])

# Scale the joints to fit the plot
joints *= 10

# Initialize scatter plot
scat = ax.scatter(joints[:, 0], joints[:, 1], s=100, c='white')

# Function to update the frame
def update(frame):
    global joints

    # Example walking motion: shifting coordinates slightly for a walking effect
    shift = np.sin(frame / 10.0) * 2.0
    joints[:, 0] = np.roll(joints[:, 0], 1) + shift

    # Update the scatter plot data
    scat.set_offsets(joints)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=100)

# Display the animation
plt.show()
