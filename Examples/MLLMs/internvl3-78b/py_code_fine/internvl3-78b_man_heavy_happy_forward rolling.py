
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 white point-lights
# These coordinates represent the initial state of the happyman in its forward rolling motion
points = [
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],  # Legs
    [1, 1], [2, 1], [3, 1],  # Torso
    [1.5, 2],  # Head
    [0, 1], [-1, 0],  # Left Arm and Leg
    [3, 1], [5, 0],  # Right Arm and Leg
    [1.5, 3], [2.5, 2.5]  # Accessories
]

# Function to update the status of the point-lights for each frame
def update(frame):
    ax.clear()

    # Calculate the displacement for the current frame
    displacement = [0.1 * frame, 0]

    # Apply the displacement to each point
    updated_points = [[x + displacement[0], y + displacement[1]] for x, y in points]

    # Draw the points
    for point in updated_points:
        ax.scatter(point[0], point[1], color='white')

    # Set the background to black
    ax.set_facecolor('black')
    ax.set_xlim([-1, 6])
    ax.set_ylim([-1, 4])

# Set up the plot
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, repeat=True)

# Display the plot
plt.show()
