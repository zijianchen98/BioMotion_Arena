
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the size of the plot
num_points = 15
plot_size = 10

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-plot_size, plot_size])
ax.set_ylim([-plot_size, plot_size])
ax.set_facecolor('black')

# Generate random starting positions for the points
positions = np.random.uniform(-plot_size, plot_size, (num_points, 2))

# Function to update the position of each point
def update(frame):
    global positions
    # Move each point in a random direction
    positions += np.random.normal(0, 0.1, (num_points, 2))
    # Clear the previous frame
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim([-plot_size, plot_size])
    ax.set_ylim([-plot_size, plot_size])
    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
