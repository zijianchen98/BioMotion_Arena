
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the number of frames in the animation
n_frames = 100

# Define the positions of the point-lights at each frame
# These positions are based on a simplified model of a person turning around
positions = np.zeros((n_points, 2, n_frames))

# Positions of the head, shoulders, elbows, hands, hips, knees, and feet
positions[0, :, :] = np.array([0, 0])  # Head
positions[1, :, :] = np.array([-0.5, 0.5])  # Left shoulder
positions[2, :, :] = np.array([0.5, 0.5])  # Right shoulder
positions[3, :, :] = np.array([-0.5, 0])  # Left elbow
positions[4, :, :] = np.array([0.5, 0])  # Right elbow
positions[5, :, :] = np.array([-0.5, -0.5])  # Left hand
positions[6, :, :] = np.array([0.5, -0.5])  # Right hand
positions[7, :, :] = np.array([0, -1])  # Hips
positions[8, :, :] = np.array([-0.5, -1.5])  # Left knee
positions[9, :, :] = np.array([0.5, -1.5])  # Right knee
positions[10, :, :] = np.array([-0.5, -2])  # Left foot
positions[11, :, :] = np.array([0.5, -2])  # Right foot
positions[12, :, :] = np.array([-0.2, -0.5])  # Weight
positions[13, :, :] = np.array([0.2, -0.5])  # Weight
positions[14, :, :] = np.array([0, -0.5])  # Weight

# Add some motion to the positions
for i in range(n_points):
    for j in range(2):
        positions[i, j, :] += np.sin(np.linspace(0, 2 * np.pi, n_frames)) * 0.1

# Add rotation to the positions
for i in range(n_points):
    for k in range(n_frames):
        x, y = positions[i, 0, k], positions[i, 1, k]
        angle = np.linspace(0, 2 * np.pi, n_frames)[k]
        positions[i, 0, k] = x * np.cos(angle) - y * np.sin(angle)
        positions[i, 1, k] = x * np.sin(angle) + y * np.cos(angle)

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Set the aspect ratio of the plot to 'equal' so the point-lights appear as points
ax.set_aspect('equal')

# Set the limits of the plot to the size of the point-lights
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Initialize the plot with the first frame
points = ax.scatter(positions[:, 0, 0], positions[:, 1, 0], s=50, c='white')

# Define the update function for the animation
def update(frame):
    points.set_offsets(positions[:, :, frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50)

plt.show()
