
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 4], [ -1, 3], [0, 3], [1, 3], [-1.5, 2], [-0.5, 2], [0.5, 2], [1.5, 2],
    [-1, 1], [0, 1], [1, 1], [-0.5, 0], [0.5, 0], [-0.3, -1], [0.3, -1]
])

# Function to update the animation
def animate(i):
    #Simulate jumping motion. Adjust parameters for different jump height and duration
    t = i / 100  #Time scaling factor
    jump_height = 2  #Maximum jump height
    
    # Simple sinusoidal jump motion
    y_offset = jump_height * np.sin(np.pi * t)

    # Apply vertical jump offset to each point
    new_positions = initial_positions + np.array([0, y_offset])
    
    #add slight random noise to simulate subtle body movements
    noise = np.random.normal(0, 0.1, size=new_positions.shape)
    new_positions += noise

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Show the animation
plt.show()

