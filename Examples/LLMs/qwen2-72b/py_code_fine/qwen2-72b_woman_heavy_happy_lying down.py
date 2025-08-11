
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Create initial positions for the 15 points
n_points = 15
points = ax.scatter([], [], c='white', s=50)

def init():
    points.set_offsets([])
    return [points]

def animate(i):
    # Generate new random positions for the points
    x = np.random.uniform(-5, 5, size=n_points)
    y = np.random.uniform(-5, 5, size=n_points)
    offsets = np.column_stack([x, y])
    
    # Update the positions of the points
    points.set_offsets(offsets)
    return [points]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100,
                              init_func=init, blit=True)

plt.show()
