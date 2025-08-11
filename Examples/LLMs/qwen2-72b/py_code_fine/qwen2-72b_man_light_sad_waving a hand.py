
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))

# Define the initial positions of the points to form a waving hand
# Here, we manually set the positions for simplicity.
# In a real scenario, these positions would be calculated based on a model.
points[0] = [100, 100]
points[1] = [100, 120]
points[2] = [100, 140]
points[3] = [100, 160]
points[4] = [100, 180]
points[5] = [100, 200]
points[6] = [120, 190]
points[7] = [140, 180]
points[8] = [160, 170]
points[9] = [180, 160]
points[10] = [200, 150]
points[11] = [220, 140]
points[12] = [240, 130]
points[13] = [260, 120]
points[14] = [280, 110]

# Scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation function
def animate(i):
    global points
    
    # Simulate waving by adjusting y-coordinates of points
    # This is a simple oscillation for demonstration purposes
    for j in range(num_points):
        points[j, 1] += 3 * np.sin(0.1 * i + j * 0.1)
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.show()
