
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1)
points, = ax.plot([], [], 'w.', ms=10)

# Initial positions for 15 point-lights representing a woman sitting down
initial_positions = np.array([
    [-0.2, 0.8], [0.2, 0.8], [-0.4, 0.6], [0, 0.6], [0.4, 0.6],
    [-0.3, 0.4], [0.3, 0.4], [-0.5, 0.2], [0, 0.2], [0.5, 0.2],
    [-0.4, 0], [0, 0], [0.4, 0], [-0.3, -0.5], [0.3, -0.5]
])

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation frame by frame
def animate(i):
    # Simulate sitting down motion
    positions = np.copy(initial_positions)
    positions[:, 1] -= 0.01 * i
    
    x = positions[:, 0]
    y = positions[:, 1]
    
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=80, init_func=init, blit=True, repeat=False)

plt.axis('off')
plt.show()
