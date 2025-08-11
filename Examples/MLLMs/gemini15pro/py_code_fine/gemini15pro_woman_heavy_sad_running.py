
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights for a single frame
# (Replace these with actual coordinates based on motion capture data or manual specification)

# Example coordinates (adjust as needed)
# This example depicts a static pose, you'll need to change these for animation.
x = np.array([1, 2, 3, 1.5, 2.5, 1, 2, 3, 1.5, 2.5, 1.5, 2.5, 0.5, 3.5, 2])
y = np.array([5, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0])

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 4)  # Set x-axis limits
ax.set_ylim(0, 6)  # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black')  # Set background color to black
scatter = ax.scatter(x, y, s=30, c='white')  # Initialize scatter plot

# Animation update function
def animate(i):
    # Update the coordinates of the point-lights for each frame
    # Example: Simple vertical oscillation (replace with your motion logic)
    # Here, 'i' represents the frame number
    y_new = y + 0.1 * np.sin(2 * np.pi * i / 20) #Example motion
    scatter.set_offsets(np.c_[x, y_new])  # Update the scatter plot data
    return scatter,  # Return the updated artist


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()

