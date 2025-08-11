
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights and their initial positions
num_points = 15
point_positions = np.array([
    [0, 2],    # Head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.5, 1], [0.5, 1],       # Elbows
    [-0.5, 0.5], [0.5, 0.5],   # Wrists
    [0, 0],    # Torso
    [-0.75, -0.5], [0.75, -0.5],  # Hips
    [-0.5, -1], [0.5, -1],       # Knees
    [-0.25, -1.5], [0.25, -1.5],  # Ankles
    [-0.5, -2], [0.5, -2],       # Feet
])

# Function to create the jumping motion
def update(frame):
    plt.clf()  # Clear the current figure
    plt.xlim(-2, 2)
    plt.ylim(-3, 3)
    plt.axis('off')  # Turn off the axis

    # Update Y positions for jumping motion
    jump_height = 1.5 * np.sin(np.pi * frame / 20)  # Smooth sine wave for jumping effect
    positions = point_positions.copy()
    positions[:, 1] += jump_height  # Apply jump height to the Y positions

    # Plot the points
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Setup the figure and axis for the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=40, interval=50)

# Set a black background color
fig.patch.set_facecolor('black')

# Display the animation
plt.show()
