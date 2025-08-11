
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create the point lights as scatter plot
points = ax.scatter([], [], c='white', s=5)

# Function to update the frame
def update(frame):
    # Clear the previous points
    points.remove()
    
    # Generate new positions for the points
    n_points = 15
    x = np.random.uniform(-10, 10, n_points)
    y = np.random.uniform(-10, 10, n_points)
    
    # Update the scatter plot with new positions
    points = ax.scatter(x, y, c='white', s=5)
    
    # Optionally, add some rotation to simulate turning around
    angle = frame * 0.1  # Increase the angle with each frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    xy = np.column_stack((x, y))
    rotated_xy = np.dot(xy, rotation_matrix.T)
    x, y = rotated_xy.T
    
    # Update the scatter plot again with the rotated positions
    points.set_offsets(rotated_xy)
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, blit=True, interval=50)

# Show the animation
plt.show()
