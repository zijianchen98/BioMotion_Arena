
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initialize the scatter plot
points = ax.scatter([], [], c='white', s=100)

# Generate initial positions
n_points = 15
x = np.random.uniform(0, 10, n_points)
y = np.random.uniform(0, 10, n_points)

def update(frame_number):
    global x, y
    
    # Update positions (simple random walk)
    dx = np.random.uniform(-1, 1, n_points)
    dy = np.random.uniform(-1, 1, n_points)
    
    x += dx
    y += dy
    
    # Wrap around the edges of the plot
    x = np.mod(x + 10, 10)
    y = np.mod(y + 10, 10)
    
    # Update the scatter plot
    points.set_offsets(np.c_[x, y])
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
