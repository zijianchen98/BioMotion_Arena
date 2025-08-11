
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the parameters for the animation
num_points = 15
num_frames = 100
turn_angle = 2 * np.pi  # Total angle to rotate (360 degrees)

# Generate initial positions for the point-lights (torso, head, limbs)
def initialize_points():
    return np.array([
        [0, 3],  # head
        [-1, 2], [1, 2],  # shoulder
        [-1, 1], [1, 1],  # elbow
        [0, 0],  # torso
        [-1, -1], [1, -1],  # hips
        [-0.5, -2], [0.5, -2],  # knees
        [-0.5, -3], [0.5, -3],  # feet
        [-1, 2.5], [1, 2.5],  # upper arms
        [-1, 1.5], [1, 1.5],  # lower arms
    ])

# Update function for animation
def update(frame):
    plt.clf()  # Clear the figure
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    
    # Create rotation matrix
    angle = frame * turn_angle / num_frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    
    points_rotated = np.dot(points, rotation_matrix)

    # Plot the point-lights
    plt.scatter(points_rotated[:, 0], points_rotated[:, 1], color='white')

    # Set background color
    plt.gca().set_facecolor('black')
    plt.axis('off')  # Turn off the axis

# Initialize points and set up animation
points = initialize_points()
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Display the animation
plt.show()
