
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [1, 4],
    [-2, 3],
    [0, 3],
    [2, 3],
    [-2.5, 2],
    [-1.5, 2],
    [0, 2],
    [1.5, 2],
    [2.5, 2],
    [-1, 1],
    [1, 1],
    [-0.5, 0],
    [0.5, 0]
])


# Animation function
def animate(i):
    # Simulate movement (replace with more realistic motion model)
    new_positions = initial_positions.copy()
    
    # Example of simple periodic movement. Replace with more sophisticated biomechanical simulation.
    amplitude = 0.5  # Adjust amplitude for more or less pronounced motion
    frequency = 0.1 # Adjust frequency for faster or slower motion
    phase = i * frequency  
    
    new_positions[:,1] += amplitude * np.sin(phase + 2 * np.pi * np.arange(num_points)/num_points)

    # Set the new positions of the points

    points.set_data(new_positions[:,0], new_positions[:,1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

