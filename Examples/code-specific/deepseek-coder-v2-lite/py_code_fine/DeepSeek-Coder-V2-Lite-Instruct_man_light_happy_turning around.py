
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Initialize the point-lights
points = np.array([[0, 0] for _ in range(15)])
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Function to update the position of the lights
def update(frame):
    angle = frame / 30.0 * 2 * np.pi  # Convert frame to angle in radians
    for i in range(15):
        radius = 1.5  # Radius of the circle
        points[i, 0] = radius * np.cos(angle + i * 2 * np.pi / 15)
        points[i, 1] = radius * np.sin(angle + i * 2 * np.pi / 15)
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 30), blit=True, repeat=True)

# Set up the background
ax.set_facecolor('black')

# Show the animation
plt.show()
