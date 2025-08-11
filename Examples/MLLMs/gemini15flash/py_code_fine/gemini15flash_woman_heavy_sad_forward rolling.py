
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
num_lights = 15
x = np.random.rand(num_lights) * 20 - 10
y = np.random.rand(num_lights) * 20 - 10
points, = ax.plot(x, y, 'wo', markersize=8)


# Function to update the point lights' positions at each frame
def animate(i):
    global x, y
    # Simulate forward rolling motion.  This is a simplified example.
    # For a realistic animation, you'd need a more sophisticated model of human movement.
    dx = np.random.normal(0, 0.5, num_lights)  # Add some noise for natural movement
    dy = np.random.normal(0, 0.5, num_lights)
    x += dx
    y += dy
    # Wrap around the edges of the screen for continuous motion
    x = np.where(x > 10, x - 20, x)
    x = np.where(x < -10, x + 20, x)
    y = np.where(y > 10, y - 20, y)
    y = np.where(y < -10, y + 20, y)
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Save the animation as a GIF (optional)
ani.save('biological_motion.gif', writer='pillow', fps=20)

# Show the animation
plt.show()

