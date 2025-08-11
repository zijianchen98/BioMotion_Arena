
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [ -1, 4], [0, 4], [1, 4], [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2], [-1,1], [0, 1], [0, 0]
])


# Define the animation function
def animate(i):
    # Update positions based on a simple sine wave for demonstration.  Replace this with more sophisticated biomechanical model for realism.
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += np.sin(i * 0.1 + np.arange(15) * 0.2) * 0.2  # Vertical movement

    #Plot updated positions.
    ax.clear()
    ax.set_xlim([-3, 3])
    ax.set_ylim([-1, 7])
    ax.scatter(updated_positions[:, 0], updated_positions[:, 1], s=50, c='w')
    ax.set_facecolor('k') #Set background color to black.
    ax.axis('off')  #Remove axes


# Set up the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()

