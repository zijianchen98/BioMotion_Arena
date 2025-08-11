
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_points = 15

# Define initial positions of point lights (x, y) coordinates
points = np.array([
    [0, 3], [1, 4], [-1, 4], [0, 5], [1, 5], [-1, 5],
    [0, 1], [1, 1], [-1, 1], [0,-1], [1,-1], [-1,-1],
    [0, -2], [1, -2], [-1, -2]
])

# Define jump trajectory parameters
jump_height = 3
jump_duration = 20
frames = 100

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create a scatter plot for the point lights
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Define the update function for the animation
def update(frame):
    # Calculate the vertical position based on a simple sinusoidal function
    t = frame / frames * np.pi * 2  # Normalize frame to [0, 2*pi]
    y_offset = jump_height * np.sin(t) - 1  # Jump height and start y position
    
    # Update point lights' vertical positions
    new_positions = points.copy()
    new_positions[:, 1] += y_offset  # Update only the y-coordinate

    # Update the scatter plot's data
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
