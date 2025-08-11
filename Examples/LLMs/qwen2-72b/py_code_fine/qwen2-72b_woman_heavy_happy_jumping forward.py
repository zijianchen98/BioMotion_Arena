
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions of the points
np.random.seed(0)
positions = np.random.uniform(-1, 1, (15, 2))

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_facecolor('black')

# Create scatter plot
points = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Animation function
def animate(i):
    global positions
    
    # Simulate jumping motion
    if i % 2 == 0:
        positions[:, 1] += 0.05
    else:
        positions[:, 1] -= 0.05
    
    # Update the scatter plot
    points.set_offsets(positions)

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
