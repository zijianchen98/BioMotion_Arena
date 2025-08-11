
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the initial positions of the point-lights
def initialize_points():
    # Define coordinates for the 15 points representing the human body lying down
    points = np.array([
        [0, 2],  # head
        [-1, 1], [1, 1],  # shoulders
        [-1.5, 0], [0, 0], [1.5, 0],  # arms
        [-0.5, -1], [0.5, -1],  # torso
        [-0.5, -2], [0.5, -2],  # hips
        [-1, -3], [1, -3],  # legs
        [-1.5, -4], [1.5, -4],  # feet
    ])
    return points

# Update function to animate points
def update(frame, points, scat):
    # Example movement: slight oscillation along the vertical axis to simulate breathing or natural movement
    y_offset = 0.1 * np.sin(frame / 10)
    animated_points = points + np.array([0, y_offset])
    scat.set_offsets(animated_points)
    return scat,

# Setting up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 3)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initializing points and scatter plot
initial_points = initialize_points()
scat = ax.scatter(initial_points[:, 0], initial_points[:, 1], color='white', s=100)

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), fargs=(initial_points, scat),
                              interval=50, blit=True)

# Display the animation
plt.show()
