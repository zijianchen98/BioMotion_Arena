
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-light positions
num_points = 15
x = np.random.rand(num_points) * 20 - 10
y = np.random.rand(num_points) * 20 - 10
points, = ax.plot(x, y, 'wo', markersize=10)


# Animation update function
def animate(i):
    global x, y
    # Simulate movement. Replace with actual biomechanical model for better realism
    dx = np.random.randn(num_points) * 0.5
    dy = np.random.randn(num_points) * 0.5
    x += dx
    y += dy
    # Keep points within bounds
    x = np.clip(x, -10, 10)
    y = np.clip(y, -10, 10)
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)


# Save the animation as a GIF (optional)
ani.save('biological_motion.gif', writer='pillow', fps=20)

# Show the animation
plt.show()

