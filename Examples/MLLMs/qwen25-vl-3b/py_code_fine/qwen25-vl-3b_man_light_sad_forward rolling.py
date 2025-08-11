
import numpy as np
import matplotlib.pyplot as plt

# Define the number of points
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Generate random positions for the points
positions = np.random.rand(num_points, 2)

# Plot the points in white
ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Animate the points to simulate forward rolling
for i in range(10):
    # Rotate the points around their center
    rotation_matrix = np.array([[np.cos(i * np.pi / 4), -np.sin(i * np.pi / 4)],
                                [np.sin(i * np.pi / 4), np.cos(i * np.pi / 4)]])
    
    # Apply the rotation matrix to the positions
    new_positions = np.dot(rotation_matrix, positions)
    
    # Update the positions of the points
    positions = new_positions
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the updated positions
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Show the plot
plt.show()
