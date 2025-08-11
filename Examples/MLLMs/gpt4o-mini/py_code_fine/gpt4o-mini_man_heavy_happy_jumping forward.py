
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of points
num_points = 15
# Define the starting positions of the point-lights for the happy man's figure
initial_positions = np.array([
    [0, 2], [1, 2], [-1, 2],
    [0, 1], [1, 1], [-1, 1],
    [0, 0], [0.5, 0], [-0.5, 0],
    [0, -1], [1, -1], [-1, -1],
    [0, -2], [1, -2], [-1, -2]
])

# Function to generate jumping forward motion
def update(frame):
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(-3, 3)
    plt.gca().set_facecolor('black')
    new_positions = initial_positions.copy()
    
    # Jumping motion modification
    jump_height = 1.5 * np.sin(frame / 10.0)  # Simple jumping sinusoidal motion
    forward_step = frame / 20  # Forward movement
    
    # Adjust positions for jumping forward
    new_positions[:, 0] += forward_step  # Move forward
    new_positions[:, 1] += jump_height  # Apply jump height

    plt.scatter(new_positions[:, 0], new_positions[:, 1], c='white', s=100)
    plt.axis('off')  # Hide axes

# Setting up the figure for animation
fig = plt.figure(figsize=(5, 8))
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
