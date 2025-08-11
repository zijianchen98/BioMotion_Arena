
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the time interval
num_points = 15
interval = 50

# Define the motion parameters for the sadwoman's forward rolling
def sadwoman_forward_rolling(t):
    # Create a sine wave pattern for the motion
    x_position = np.sin(np.linspace(0, 2 * np.pi, num_points)) * 0
    y_position = -np.cos(np.linspace( 0, 2 * np.pi, num_points)) * 10 + t
    return zip(x_position, y_position)

# Set up the plot
fig, ax = plt.subplots()
ax, y = next(sadwoman_forward_rolling(0))
points, = ax.plot([], [], 'o', color='white')

# Initialize the plot
def init():
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')
    ax.axis('off
    return points,

# Animate function
def animate(t):
    x, y = next(sadwoman_forward_rolling(t))
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 20, interval), interval=interval, blit=True)

# Show the animation
plt.show()
