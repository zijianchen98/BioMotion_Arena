
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define parameters
num_points = 15
frames = 100  # Total frames of the animation
weight = np.array([0, -1])  # Direction of the heavy weight

# Initial positions (x, y) of the 15 points representing the body
initial_positions = np.array([
    [0, 2],   # Head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.5, 1], [0.5, 1],  # Elbows
    [-1, 0.5], [1, 0.5],  # Hands
    [-0.5, 0], [0.5, 0],  # Waist
    [-1, -1], [1, -1],  # Knees
    [-0.5, -2], [0.5, -2],  # Feet
    [0, -1]  # Weight position
])

# Function to update the positions for each frame
def update(frame):
    plt.clf()
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    
    # Compute the rotation angle
    angle = frame * (2 * np.pi / frames)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate and translate the points
    rotated_positions = np.dot(initial_positions, rotation_matrix)
    weight_position = rotated_positions[-1] + weight  # Adjust weight position
    all_positions = np.vstack((rotated_positions, weight_position))

    # Plot points
    plt.scatter(all_positions[:, 0], all_positions[:, 1], color='white')
    plt.gca().set_facecolor('black')

# Create animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# Show the animation
plt.show()
