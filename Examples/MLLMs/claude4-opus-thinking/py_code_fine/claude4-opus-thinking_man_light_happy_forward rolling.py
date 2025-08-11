
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_points = 15

# Define the initial positions of the point-lights
init_positions = np.array([
    [0, 5],    # Head
    [-1, 4], [1, 4],  # Shoulders
    [-2, 3], [0, 3], [2, 3],  # Arm positions
    [-1.5, 2], [1.5, 2],  # Elbow positions
    [-1, 1], [1, 1],  # Hand positions
    [-1, 0], [0, 0], [1, 0],  # Hips
    [-0.5, -1], [0.5, -1],  # Knee positions
    [0, -2]  # Feet position
])

# Function to update the positions for a forward roll
def update_positions(frame):
    # Clear previous position
    for i in range(num_points):
        line[i].set_data([], [])

    # Update the positions for a forward rolling motion
    phase = frame / 20  # Control the speed of animation
    y_offset = -1 * (0.1 * (frame%20))  # Create a downward motion
    for i in range(num_points):
        # Apply Y-axis transformations to simulate rolling
        current_positions[i] = init_positions[i] + np.array([0, y_offset])
        line[i].set_data(current_positions[i, 0], current_positions[i, 1])
    
    return line

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axes

# Create a list to hold line objects for point-lights
line = [ax.plot([], [], 'o', color='white')[0] for _ in range(num_points)]
current_positions = np.copy(init_positions)

# Create the animation
ani = FuncAnimation(fig, update_positions, frames=100, interval=100)  # 20 FPS

# Show the animation
plt.show()
