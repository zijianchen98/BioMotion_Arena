
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 5)
ax.set_facecolor('black')
plt.axis('off')  # Turn off the axis

# Number of point-lights
num_points = 15
points = np.zeros((num_points, 2))  # Initialize point-light positions

# A simple function to update point positions to represent a jump
def update(frame):
    ax.clear()  # Clear the previous frame
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 5)
    ax.set_facecolor('black')
    plt.axis('off')  # Turn off the axis
    
    # Calculate new positions for point-lights to simulate jumping
    height = 2 + np.abs(1 - 1.5 * np.abs(np.sin(frame * np.pi / 30)))  # Jump height
    # Create a sadman body structure
    y_base = height if frame % 60 < 30 else 0  # Simulating upward and downward motion
    # Assign points vertically distributed
    for i in range(num_points):
        if i < 5:
            points[i] = [0, y_base + i * 0.3]  # Head and upper body points
        elif i < 10:
            points[i] = [0, y_base - (i-5) * 0.3]  # Lower body points
        else:
            points[i] = [0.2 * np.sin(np.pi * i / (num_points - 1)), y_base - (0.2 * (i-10) + 0.3)]  # Legs points

    # Plot the point lights
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(120), interval=50)
plt.show()
