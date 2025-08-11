
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.axis('off')  # Turn off the axis

# Create point-light positions
n_points = 15
points = np.zeros((n_points, 2))

# Initial positions of point-lights (roughly in the shape of a body)
# You can adjust these based on your specific needs.
initial_positions = np.array([
    [0, 6], [1, 7], [-1, 7],  # Head
    [0, 5], [1, 6], [-1, 6],  # Shoulders
    [0, 4], [1, 5], [-1, 5],  # Hips
    [0, 3], [1, 4], [-1, 4],  # Thighs
    [0, 2], [1, 3], [-1, 3],  # Calves
    [0, 1]  # Ground/weight position
])

# Update function for animation
def update(frame):
    ax.clear()
    ax.axis('off')
    
    # Simulate jumping motion - a simple upward and downward oscillation
    vertical_offset = np.sin(frame / 10)  # Vertical movement based on sine function
    
    # Apply vertical offset to positions
    points[:, 0] = initial_positions[:, 0]
    points[:, 1] = initial_positions[:, 1] + vertical_offset
    
    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)  # s=100 for point size
    ax.set_facecolor('black')  # Set background color

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Show the animation
plt.show()
