
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the forward rolling motion as a sequence of x, y coordinates
def forward_roll_motion(frames):
    points = []
    for i in range(frames):
        t = i / frames * 2 * np.pi
        x = np.array([-3, -2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, 2, 1])
        y = np.array([0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1.5, 1])
        x = x * np.cos(t) - y * np.sin(t)
        y = x * np.sin(t) + y * np.cos(t)
        points.append(np.vstack((x, y)).T)
    return points

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis([-5, 5, -5, 5])
ax.axis('off')

# Create scatter plot
scat = ax.scatter([], [])

# Update function for animation
def update(frame):
    scat.set_offsets(forward_roll_motion(60)[frame])

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=100, blit=False)

# Show the animation
plt.show()
