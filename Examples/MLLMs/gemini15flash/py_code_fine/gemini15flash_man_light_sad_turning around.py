
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],  # Head
    [-1, 3], [0, 3], [1, 3],  # Shoulders
    [-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1],  # Torso
    [-1, -1], [1, -1],  # Hips
    [-1.5, -3], [1.5, -3], #Legs
    [0,-5] #Feet

])

# Function to update the points' positions for each frame
def animate(i):
    # Define the rotation angle
    angle = i * np.pi / 180 #increase the rotation speed by increasing the factor multiplied with i

    # Rotate the points around the center
    rotated_positions = np.dot(initial_positions, np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]))

    # Update the points' data
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])

    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)


# Show the animation
plt.show()

