
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
positions = np.array([
    [0, 0],
    [0.2, 0.2],
    [0.4, 0.4],
    [0.2, 0.6],
    [0.4, 0.8],
    [0.6, 0.6],
    [0.8, 0.8],
    [0.6, 1.0],
    [0.8, 1.2],
    [1.0, 1.0],
    [1.2, 1.2],
    [1.0, 1.4],
    [1.2, 1.6],
    [1.0, 1.8],
    [1.2, 2.0]
])


# Define the animation function
def animate(i):
    # Update positions based on time (i)
    # Simple sinusoidal motion for demonstration.  Replace with more complex model for realism
    updated_positions = positions.copy()
    updated_positions[:, 1] += 0.02 * np.sin(i * 0.1)  # Wave hand motion

    # Add some slight random jitter
    updated_positions += np.random.normal(scale=0.01, size=updated_positions.shape)

    #Plot 
    ax.clear()
    ax.set_xlim(-0.5, 2)
    ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.scatter(updated_positions[:, 0], updated_positions[:, 1], s=50, c='white')
    ax.set_xticks([])
    ax.set_yticks([])


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  #Black background

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()

