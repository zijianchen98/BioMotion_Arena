
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Define initial positions for 15 points
points = np.array([
    [50, 50], [40, 55], [60, 55], [45, 60], [55, 60], 
    [50, 65], [35, 70], [45, 70], [55, 70], [65, 70], 
    [40, 75], [50, 75], [60, 75], [45, 80], [55, 80]
])

# Define the jump motion function
def jump_motion(points, t):
    # Define oscillating motion for jumping
    y_offset = 10 * np.sin(t * 2 * np.pi / 50)
    points[:, 1] = points[:, 1] + y_offset
    return points

# Create scatter plot for point lights
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

def animate(t):
    global points
    points = jump_motion(points, t)
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=50, interval=50, blit=True)

plt.show()
