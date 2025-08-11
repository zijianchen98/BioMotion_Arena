
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background color to black
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create 15 white points
points = [plt.Circle((np.random.uniform(-10, 10), np.random.uniform(-10, 10)), 0.5, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Animation function
def update(frame):
    for i, point in enumerate(points):
        # Update each point's position to simulate rolling motion
        angle = frame * 0.1 + i * 0.2
        point.center = (8 * np.cos(angle), 8 * np.sin(angle))
    return points

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show animation
plt.show()
