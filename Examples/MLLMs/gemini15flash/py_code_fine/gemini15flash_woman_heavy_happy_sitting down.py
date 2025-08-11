
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
points, = ax.plot(x, y, 'wo', markersize=8)


# Animation update function
def animate(i):
    global x, y
    # Simulate movement -  replace with more sophisticated biomechanical model if needed.
    dx = np.random.randn(num_points) * 0.2
    dy = np.random.randn(num_points) * 0.2

    # Gravity effect (downward)
    dy -= 0.05

    # Simple collision detection with ground
    y = np.maximum(y + dy, -9)

    # update positions
    x += dx
    
    # keep points within bounds
    x = np.clip(x,-9,9)
    y = np.clip(y,-9,9)
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=30, blit=True)

# Show the animation
plt.show()

