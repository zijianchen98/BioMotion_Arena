
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
points = np.array([
    [0.0, 0.0], [0.2, 0.1], [0.4, 0.0], [0.2, -0.1],
    [0.2, 0.3], [0.4, 0.2], [0.6, 0.3], [0.4, 0.1],
    [0.4, -0.1], [0.6, -0.2], [0.4, -0.3], [0.2, -0.2],
    [0.2, -0.4], [0.0, -0.3], [0.2, -0.4]
])

# Function to generate wave motion
def wave_motion(t):
    angle = np.sin(t / 10)
    points[:, 0] = 0.2 * np.cos(angle) + 0.2 * np.random.randn(15)
    points[:, 1] += 0.1 * np.sin(t / 10) * (np.random.rand(15) - 0.5)
    return points

# Update function for the animation
def update(frame):
    global points
    points = wave_motion(frame)
    scatter.set_offsets(points)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-1.0, 0.5)
ax.axis('off')
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
