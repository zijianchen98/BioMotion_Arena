
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights (simplified representation of key points)
joints = np.array([
    [0, 1],   # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Hips
    [-0.5, -0.5], [0.5, -0.5],  # Knees
    [-0.5, -1], [0.5, -1],  # Feet
    [0, 0.75],  # Hand Right
    [0, -0.75],  # Hand Left
    [-0.5, 0.5], [0.5, 0.5],  # Elbows (for increased realism)
    [-0.25, 0.25], [0.25, 0.25]   # Before/after the action
])

# Define the animation function
def update(frame):
    # Clear the plot
    plt.clf()
    
    # Adjust the positions of the points to simulate motion (lying down smoothly)
    offset = 0.05 * np.sin(frame / 10.0)  # smooth vertical oscillation
    plt.scatter(joints[:, 0], joints[:, 1] + offset, color='white')
    
    # Set the limits and aspect of the plot
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_facecolor('black')  # Background color
    plt.axis('off')  # Turn off the axis

# Initialize the figure
fig = plt.figure()

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), interval=50)

# Show the animation
plt.show()
