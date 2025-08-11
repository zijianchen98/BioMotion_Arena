
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

# Initialize positions for the point lights (these could represent a sad man running with a weight)
points = np.zeros((num_points, 2))
points[:, 0] = np.linspace(35, 65, num_points)  # X positions
points[:, 1] = 50  # Fixed Y position for a 2D representation

# Function to update the positions of the point lights
def update(frame):
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_facecolor('black')

    # Update vertical positions to simulate running
    for i in range(num_points):
        # Example movement pattern to represent running
        points[i, 1] = 50 + 10 * np.sin(np.radians(frame * 10 + i * 20))
    
    # Draw the point lights
    ax.plot(points[:, 0], points[:, 1], 'wo', markersize=10)
    return ax,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show animation
plt.show()
