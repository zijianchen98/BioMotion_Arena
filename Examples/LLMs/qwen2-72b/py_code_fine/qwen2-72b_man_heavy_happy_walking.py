
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the figure size
num_points = 15
fig, ax = plt.subplots(figsize=(8, 8))

# Set the background color to black
ax.set_facecolor('black')

# Remove the axis labels and ticks
ax.axis('off')

# Define the initial positions and velocities of the points
positions = np.random.uniform(low=-100, high=100, size=(num_points, 2))
velocities = np.random.uniform(low=-1, high=1, size=(num_points, 2))

# Define the function to update the positions of the points at each frame
def update(frame):
    global positions, velocities
    
    # Update the positions based on the velocities
    positions += velocities
    
    # Keep the points within the bounds of the screen
    positions = np.clip(positions, -100, 100)
    
    # Update the scatter plot with the new positions
    scat.set_offsets(positions)
    
    return scat,

# Create the scatter plot of the points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Define the animation object
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
