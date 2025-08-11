
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Define the initial positions of the points
positions = np.random.rand(num_points, 2)

# Define the initial velocities of the points
velocities = np.zeros((num_points, 2))

# Define the acceleration due to gravity
g = -9.81

# Define the time step
dt = 0.01

# Define the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for the points
points, = ax.plot(positions[:, 0], positions[:, 1], 'o', color='white')

def update(frame):
    global positions, velocities
    
    # Update the positions based on the velocities
    positions += velocities * dt
    
    # Apply gravity to the velocities
    velocities[:, 1] += g * dt
    
    # Update the scatter plot data
    points.set_data(positions[:, 0], positions[:, 1])
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
