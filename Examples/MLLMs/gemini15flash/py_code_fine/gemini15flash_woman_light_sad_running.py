
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
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5], [ -2, 4], [-1,4], [1,4], [2,4],
    [-3,3], [-1.5,3],[0,3], [1.5,3], [3,3],
    [-1,1],[1,1],
    [-1,-1],[1,-1],
    [0,-3]
])

# Function to update the points' positions for each frame
def animate(i):
    #Simulate running motion. Adjust parameters for different speeds and styles.
    t = i / 10.0  # Adjust the speed here. Smaller value = slower animation.
    
    x_positions = initial_positions[:, 0] + np.sin(t + np.linspace(0, 2*np.pi, num_points)) *2
    y_positions = initial_positions[:, 1] + np.cos(t + np.linspace(0, 2*np.pi, num_points))  # Adjust vertical motion here

    # Update point positions
    points.set_data(x_positions, y_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

