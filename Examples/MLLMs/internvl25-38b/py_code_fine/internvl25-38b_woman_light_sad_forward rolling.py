
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to generate initial positions of the points
def init_positions():
    np.random.seed(0)
    x = np.linspace(0, 1, 15)
    y = np.sin(x * 2 * np.pi) + np.random.normal(0, 0.1, 15)
    return x, y

# Function to update positions for the forward rolling motion
def update_positions(x, y, frame):
    angle = frame * 0.05
    y += 0.1 * np.sin(angle)
    x += 0.02 * np.cos(angle)
    return x, y

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_xlim(0, 1)
ax.set_ylim(-1, 1)

# Generate initial positions
x, y = init_positions()

# Initialize points
points, = ax.plot(x, y, 'wo', markersize=10)

# Update function for animation
def animate(i):
    x_new, y_new = update_positions(x, y, i)
    points.set_data(x_new % 1, y_new)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
