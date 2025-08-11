
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
np.random.seed(0)
positions = np.random.uniform(low=-1, high=1, size=(15, 2))

# Define the velocities of the point-lights
velocities = np.random.uniform(low=-0.05, high=0.05, size=(15, 2))

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Create scatter plot for the points
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

def update(frame):
    global positions, velocities
    # Update positions based on velocities
    positions += velocities
    
    # Bounce off the walls by reversing velocity if necessary
    positions[positions > 1] = 2 - positions[positions > 1]
    positions[positions < -1] = -2 - positions[positions < -1]
    
    velocities[positions > 1] *= -1
    velocities[positions < -1] *= -1
    
    # Update the scatter plot
    scatter.set_offsets(positions)

ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
