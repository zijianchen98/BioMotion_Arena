
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
num_frames = 100
radius = 10

# Point locations for a sad woman with 15 points
# These are made-up positions to give a basic structure of a human figure
initial_positions = np.array([
    [0, 5], [-1, 6], [1, 6],  # Head
    [-2, 4], [2, 4],         # Shoulders
    [-3, 2], [-1, 3], [0, 2], [1, 3], [3, 2],  # Arms
    [-2, 0], [0, 0], [2, 0],  # Body
    [-1, -2], [1, -2],        # Legs
    [0, -3]                   # Feet
])

# Create a function to update the positions for each frame
def update(frame):
    plt.clf()
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.title('Biological Motion - Sad Woman Turning Around')

    # A basic turning motion around the Y-axis
    angle = 2 * np.pi * frame / num_frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    rotated_positions = initial_positions @ rotation_matrix

    # Draw points
    plt.scatter(rotated_positions[:, 0], rotated_positions[:, 1], s=100, color='white')
    plt.gca().set_facecolor('black')
    plt.axis('off')

# Create the figure and axis
fig = plt.figure(figsize=(6, 6))
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Display the animation
plt.show()
