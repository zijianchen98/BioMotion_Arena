
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.axis('off')

# Define the initial positions of the point lights
num_points = 15
point_lights = np.array([
    [5, 8],  # Head
    [4, 7], [5, 7], [6, 7],  # Shoulders
    [3.5, 6], [5, 6], [6.5, 6],  # Arms
    [4, 4], [5, 4], [6, 4],  # Torso
    [4.5, 3], [5.5, 3],  # Hips
    [4.25, 1], [5.25, 1],  # Legs
    [4.5, 0], [5.5, 0]   # Feet
])

# Function to update point light positions for animation
def update(frame):
    # Clear points
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_facecolor('black')

    # Define motion by slightly moving point lights down for each frame
    for i in range(num_points):
        point_lights[i, 1] -= 0.05  # Move down

        # Reset if the point has moved off the bottom
        if point_lights[i, 1] < 0:
            point_lights[i, 1] = 0

    # Plot the updated positions
    ax.scatter(point_lights[:, 0], point_lights[:, 1], s=100, c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

# Display the animation
plt.show()
