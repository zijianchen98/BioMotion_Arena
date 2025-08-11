
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [0, 4],
    [1, 4],
    [-2, 3],
    [-1, 3],
    [0, 3],
    [1, 3],
    [2, 3],
    [-1, 2],
    [0, 2],
    [1, 2],
    [0, 1],
    [-0.5, 0],
    [0.5, 0]
])


# Animation function
def animate(i):
    # Define the positions of the points for each frame
    # This is where you would implement your biomechanically plausible motion
    # For this example, I'm using simple sinusoidal motion for demonstration purposes
    
    new_positions = initial_positions.copy()
    
    # Simulate waving hand motion
    new_positions[3, 0] += 2 * np.sin(i * 0.1)
    new_positions[4, 0] += 1.5 * np.sin(i * 0.1 + 0.2)
    new_positions[2, 0] += 1 * np.sin(i * 0.1 + 0.4)
    new_positions[1, 0] += 0.5 * np.sin(i * 0.1 + 0.6)
    
    #Adding slight sway to the body
    new_positions[0:5, 1] += 0.3 * np.sin(i* 0.05)
    new_positions[5:10, 1] += 0.2 * np.sin(i * 0.05 + 0.1)
    new_positions[10:15, 1] += 0.1 * np.sin(i * 0.05 + 0.2)


    # Update the point positions
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

