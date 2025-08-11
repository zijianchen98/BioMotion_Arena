
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Initial positions of point-lights (skeleton-like)
initial_positions = np.array([
    [0, 1],     # Head
    [-0.5, 0.8],  # Left shoulder
    [0.5, 0.8],   # Right shoulder
    [-0.5, 0.5],  # Left elbow
    [0.5, 0.5],   # Right elbow
    [-0.5, 0],    # Left hand
    [0.5, 0],     # Right hand
    [-0.5, -0.5], # Left hip
    [0.5, -0.5],  # Right hip
    [-0.5, -1],   # Left knee
    [0.5, -1],    # Right knee
    [-0.5, -1.5], # Left foot
    [0.5, -1.5],  # Right foot
    [0, 0],       # Center of mass
    [0, 0.5],     # Torso position
    [0, -1.5]     # Lower back
])

# Update function for animation
def update(frame):
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_facecolor('black')

    # Incremental movements to simulate sitting down
    downward_movement = frame * 0.02
    for i in range(num_points):
        plt.scatter(initial_positions[i, 0], initial_positions[i, 1] - downward_movement, color='white', s=100)

# Creating the figure
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 50), interval=50)

# Display the animation
plt.show()
