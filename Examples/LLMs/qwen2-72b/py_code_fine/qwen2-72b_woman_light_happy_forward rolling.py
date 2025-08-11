
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Define initial positions of the point-lights
num_lights = 15
positions = np.random.rand(num_lights, 2) * 10

# Define function to update the position of each point-light
def update(frame):
    global positions
    ax.clear()
    ax.set_facecolor('black')
    
    # Simulate a forward roll by moving the points in a wave-like pattern
    positions[:, 0] += 0.1 * (np.sin(0.1 * frame) + 1)
    positions[:, 1] -= 0.1 * (np.cos(0.1 * frame) + 1)
    
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=40)

# Show the animation
plt.show()
