
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))

# Set initial positions to represent a sitting person
points[0] = [0, 5]  # Head
points[1] = [-1, 4]  # Left shoulder
points[2] = [1, 4]   # Right shoulder
points[3] = [-1, 3]  # Left elbow
points[4] = [1, 3]   # Right elbow
points[5] = [-1, 2]  # Left wrist
points[6] = [1, 2]   # Right wrist
points[7] = [0, 2]   # Torso
points[8] = [-1, 1]  # Left hip
points[9] = [1, 1]   # Right hip
points[10] = [-1, 0] # Left knee
points[11] = [1, 0]  # Right knee
points[12] = [-1, -1] # Left ankle
points[13] = [1, -1]  # Right ankle
points[14] = [0, -2]   # Center of the sitting position

# Function to update point positions for the animation
def update(frame):
    # Clear previous frame
    plt.clf()
    # Set background
    plt.xlim(-5, 5)
    plt.ylim(-3, 6)
    plt.gca().set_facecolor('black')
    plt.axis('off')

    # Apply a simple downward motion to simulate sitting down
    motion_offset = -0.04 * frame

    # Update positions
    new_positions = points + np.array([[0, motion_offset]] * num_points)

    # Plot updated positions
    plt.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Generate animation
fig = plt.figure(figsize=(5, 10))
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)

# Display the animation
plt.show()
