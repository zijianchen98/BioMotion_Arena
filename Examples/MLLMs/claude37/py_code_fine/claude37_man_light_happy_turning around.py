
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Define the positions of the points
# 5 positions for head, arms, torso, and legs
# You may adjust these points to create a more realistic representation
initial_positions = np.array([
    [0, 1.5],   # Head
    [-0.5, 1],  # Left Arm 1
    [0.5, 1],   # Right Arm 1
    [0, 0.5],   # Torso
    [-0.5, 0],  # Left Leg
    [0.5, 0],   # Right Leg
    [0, 0.5],   # Calf 1
    [-0.5, 0.7],  # Left Hand
    [0.5, 0.7],   # Right Hand
    [0, 1],      # Neck
    [-0.3, 0.6],  # Left Foot
    [0.3, 0.6],   # Right Foot
    [0, 0.5],    # Hip Position
    [0, 0.9],    # Upper Body Pass
    [-0.5, 0.5],  # Lower Body Pass
    [0.5, 0.5]    # Lower Body Pass
])

# Animation function
def update(frame):
    plt.clf()
    angle = np.radians(frame % 360)  # Rotate 360 degrees
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])

    rotated_positions = initial_positions @ rotation_matrix.T  # Apply rotation
    plt.scatter(rotated_positions[:, 0], rotated_positions[:, 1], s=100, c='white')
    plt.xlim(-2, 2)
    plt.ylim(-1, 2)
    plt.gca().set_facecolor('black')  # Set background to black
    plt.axis('off')  # Hide axes

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=360, interval=50)

# Show the animation
plt.show()
