
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim((-500, 500)
ax.set_ylim((-400, 400))
ax.set_facecolor('black')
ax.axis('off')

# Create the points (representing the body parts of the happy man
points = np.array([
    [-51, -150], [-90, -150], [80, -150],
    [160, -150], [240, -150], [320, -150],
    [370, -150], [420, -150], [450, -150],
    [460, -150], [470, -150], [420, -150],
    [370, -150], [250, -150], [140, -150],
    [50, -150], [-100, -150], [-210, -150]
])

def animate(i):
    # Smoothly move the points
    points[:, 0] += np.random.normal(scale=10, size=points.shape[0])
    points[:, 1] += np.random.normal(scale=10, size=points.shape[0])

    # Draw lines between points to form the body parts
    for j in range(points.shape[0]):
        if j < points.shape[0] - 1:
            ax.plot([points[j, 0], points[j + 1, 0]], [points[j, 1], points[j + 1, 1]], 'w-', linewidth=3)

    # Add a light source at the top
    ax.scatter(0, 400, color='white', s=200)

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 5, 0.1), interval=20)

plt.show()

