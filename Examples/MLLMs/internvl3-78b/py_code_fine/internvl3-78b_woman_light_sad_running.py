
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# Figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
plt.axis('off')  # Turn off axis

# Number of point-lights
num_points = 15

# Initial positions of the points
points, = ax.plot([], [], 'ko', ms=3)  # Black points with size 3

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation frame
def animate(i):
    # Generate new positions for each point
    x = np.sin(i) * 0.2 + np.random.rand(num_points) * 10  # Random x positions with a sinusoidal curve
    y = np.cos(i) * 0.2 + np.random.rand(num_points) * 5  # Random y positions with a cosine curve

    # Update data
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
