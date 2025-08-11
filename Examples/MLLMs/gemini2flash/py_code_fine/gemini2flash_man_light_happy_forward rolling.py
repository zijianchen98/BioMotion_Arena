
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (relative to the center)
initial_positions = np.array([
    [0, 1.8],  # Head
    [-0.3, 1.5],  # Left Shoulder
    [0.3, 1.5],  # Right Shoulder
    [-0.5, 1.2],  # Left Elbow
    [0.5, 1.2],  # Right Elbow
    [-0.7, 0.9],  # Left Wrist
    [0.7, 0.9],  # Right Wrist
    [-0.1, 1.0],  # Spine Upper
    [0.1, 1.0],  # Spine Upper
    [0, 0.6],  # Spine Lower
    [-0.2, 0.0],  # Left Hip
    [0.2, 0.0],  # Right Hip
    [-0.4, -0.6],  # Left Knee
    [0.4, -0.6],  # Right Knee
    [0, -1.0]   # Ankle
])

# Define the animation function
def update(frame):
    plt.clf()
    plt.axis('equal')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_facecolor('black')
    plt.xticks([])
    plt.yticks([])

    # Simulate rolling motion
    angle = frame * 0.05 * np.pi  # Adjust the speed of rolling here

    # Rotate and translate the points
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_positions = np.dot(initial_positions, rotation_matrix)
    translated_positions = rotated_positions + np.array([0, -angle * 0.5])  # Translate downward as it rolls

    # Plot the points
    plt.plot(translated_positions[:, 0], translated_positions[:, 1], 'wo', markersize=8)

    return plt.gca()

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=100, repeat=True)  # Adjust frames for longer/shorter animation

# Show the animation
plt.show()
