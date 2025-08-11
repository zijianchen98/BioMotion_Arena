
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Function to update the points in the animation
def update(num):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Coordinates of the point lights for the sitting motion
    seating_positions = [
        [-0.2, 0.8],   # Head
        [-0.4, 0.6],   # Left shoulder
        [0.4, 0.6],    # Right shoulder
        [-0.5, 0.4],   # Left elbow
        [0.5, 0.4],    # Right elbow
        [-0.6, 0.2],   # Left hand
        [0.6, 0.2],    # Right hand
        [-0.3, 0.1],   # Left hip
        [0.3, 0.1],    # Right hip
        [-0.2, -0.2],  # Left knee
        [0.2, -0.2],   # Right knee
        [-0.2, -0.4],  # Left ankle
        [0.2, -0.4],   # Right ankle
        [0.0, 0.7],    # Top middle Point
        [-0.4, 0.2],   # Middle left Point
        [0.4, 0.2]     # Middle right Point
    ]

    # Adjust the y-coordinates for realistic sitting action
    for i in range(15):
        seating_positions[i][1] -= np.sin(num * 0.2 + i) * 0.05  # Smooth vertical motion

    # Create a scatter plot for point lights
    points = np.array(seating_positions)
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)  # s is the size of points

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
