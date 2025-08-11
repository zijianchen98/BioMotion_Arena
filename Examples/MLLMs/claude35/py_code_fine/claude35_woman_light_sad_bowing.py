
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points representing the body
num_points = 15
# Initial positions of the points in a 2D bowing pose
initial_positions = np.array([
    [0, 1], [0.5, 0.75], [-0.5, 0.75],   # Head and shoulders
    [0, 0.5], [0.5, 0.25], [-0.5, 0.25],  # Elbows
    [0, 0], [0.5, -0.5], [-0.5, -0.5],   # Hands
    [0, -1], [0.5, -1.5], [-0.5, -1.5],  # Feet                          ]
    [0.25, 0], [-0.25, 0], [0.25, -0.5]  # Additional points for realism
])

# Update function to create bowing motion
def update(frame):
    # Calculate the transformation for the bowing effect
    bow_angle = -np.pi / 12 * np.sin(frame * np.pi / 30)
    transformation = np.array([[np.cos(bow_angle), -np.sin(bow_angle)],
                               [np.sin(bow_angle), np.cos(bow_angle)]])
    
    # New positions based on transformations
    new_positions = initial_positions @ transformation.T

    # Clear the axes and plot the new points
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_facecolor('black')
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white')
    ax.axis('off')

# Create a figure for the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60), interval=100)

# Display the animation
plt.show()
