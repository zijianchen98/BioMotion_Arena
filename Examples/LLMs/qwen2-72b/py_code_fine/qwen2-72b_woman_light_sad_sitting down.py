
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_facecolor('black')

# Create data for 15 points
n_points = 15
x = np.random.rand(n_points)
y = np.random.rand(n_points)

# Scatter plot for initial positions
scat = ax.scatter(x, y, c='white', s=100)

def update(frame_number):
    # Update the position of each point
    x[:] = x + np.random.uniform(-0.1, 0.1, n_points)
    y[:] = y + np.random.uniform(-0.1, 0.1, n_points)
    
    # Set the new data
    scat.set_offsets(np.column_stack([x, y]))
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

# Show the animation
plt.show()
