
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the sad woman's joints
# The coordinates are based on a simplified human skeleton model
# Each point-light is defined by its x, y, and z coordinates
point_lights = np.array([
    [0, 0, 0],  # Head
    [-0.5, 0.5, 0],  # Left shoulder
    [0.5, 0.5, 0],  # Right shoulder
    [-1, 1, 0],  # Left elbow
    [1, 1, 0],  # Right elbow
    [-1.5, 1.5, 0],  # Left wrist
    [1.5, 1.5, 0],  # Right wrist
    [0, -0.5, 0],  # Hip
    [-0.5, -1, 0],  # Left knee
    [0.5, -1, 0],  # Right knee
    [-1, -1.5, 0],  # Left ankle
    [1, -1.5, 0],  # Right ankle
    [-0.25, 0.25, 0],  # Left breast
    [0.25, 0.25, 0],  # Right breast
    [0, -1, 0],  # Tailbone
])

# Define the animation frames
# Each frame represents a specific position of the point-lights in 3D space
# The movement is based on a simplified jumping motion
frames = []
for i in range(60):  # 60 frames
    frame = np.copy(point_lights)
    # Simulate the jumping motion
    frame[:, 1] += np.sin(i / 10.0) * 0.5  # Vertical movement
    frame[:, 0] += np.sin(i / 5.0) * 0.25  # Horizontal movement
    # Add some randomness to the movement to make it look more natural
    frame += np.random.uniform(-0.05, 0.05, size=frame.shape)
    frames.append(frame)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.scatter(frame[:, 0], frame[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

plt.show()
