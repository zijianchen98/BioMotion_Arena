
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()

# Set the background to black
ax.set_facecolor('black')

# Set the axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(0, 10)

# Initialize the point-lights
points = np.zeros((15, 2))
for i in range(15):
    points[i, 0] = np.random.uniform(-8, 8)
    points[i, 1] = np.random.uniform(1, 5)

# Initialize the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the scatter plot for each frame
def update(frame):
    global points
    points[:, 0] += 0.1  # Move the points to the right
    if points[-1, 0] > 8:  # Reset the points when they move out of the screen
        points = np.zeros((15, 2))
        for i in range(15):
            points[i, 0] = np.random.uniform(-8, 8)
            points[i, 1] = np.random.uniform(1, 5)
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
