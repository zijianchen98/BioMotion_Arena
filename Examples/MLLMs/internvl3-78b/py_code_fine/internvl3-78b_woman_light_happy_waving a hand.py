
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 640)
ax.set_ylim(0, 480)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')  # Hide axes for a clear view
fig.patch.set_facecolor('black')  # Set background color to black

# Number of points
n_points = 15
# Initialize with random positions
positions = np.random.rand(n_points, 2) * [640, 480]

# Create a list of scatter plots (points)
points = [ax.scatter(x, y, color='white') for x, y in positions]

# Function to update the positions of the points
def update(frame):
    global positions
    # Use random walks with some constraint to simulate realistic motion
    movement = np.random.normal(loc=0, scale=3, size=(n_points, 2))  # random noise
    positions = (positions + movement) % [640, 480]  # keep within bounds by modulo

    # Update the scatter plot every frame
    for i, point in enumerate(points):
        point.set_offsets([positions[i]])
    return points

# Create an animation object
ani = animation.FuncAnimation(fig, update, frames=400, interval=50, blit=True)

# Display the animation
plt.show()
