
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a forward roll
def get_forward_roll_keypoints(frame):
    # Define the key points for a forward roll (simplified for demonstration)
    keypoints = np.array([
        [0.5, 0.9],  # Head
        [0.4, 0.8],  # Neck
        [0.3, 0.7],  # Left Shoulder
        [0.6, 0.7],  # Right Shoulder
        [0.2, 0.6],  # Left Elbow
        [0.7, 0.6],  # Right Elbow
        [0.1, 0.5],  # Left Hand
        [0.8, 0.5],  # Right Hand
        [0.4, 0.4],  # Left Hip
        [0.6, 0.4],  # Right Hip
        [0.3, 0.3],  # Left Knee
        [0.7, 0.3],  # Right Knee
        [0.2, 0.2],  # Left Foot
        [0.8, 0.2],  # Right Foot
        [0.5, 0.1]   # Center of Mass
    ])

    # Apply a simple transformation to simulate the forward roll
    angle = frame * 0.1  # Rotation angle
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    transformed_keypoints = np.dot(keypoints, rotation_matrix.T)

    # Adjust positions to simulate the forward roll
    transformed_keypoints[:, 1] += frame * 0.01  # Move down slightly
    transformed_keypoints[:, 0] += frame * 0.02  # Move right slightly

    return transformed_keypoints

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Initialize the points
points = ax.scatter([], [], color='white', s=100)

# Update function for the animation
def update(frame):
    keypoints = get_forward_roll_keypoints(frame)
    points.set_offsets(keypoints)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
