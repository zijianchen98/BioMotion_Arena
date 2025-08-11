
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


# Define the animation function
def animate(i):
    # Define the bowing motion (adjust parameters for different styles)

    # Example motion parameters, adjust these to fine-tune the animation
    amplitude = 1.5  # Adjust for bowing depth
    frequency = 0.1  # Adjust for bowing speed
    weight_factor = 0.7 #Simulate weight effect


    # Apply motion to points
    x = initial_positions[:, 0] + np.sin(i * frequency) * amplitude * np.random.rand(num_points)
    y = initial_positions[:, 1] + np.cos(i * frequency) * amplitude * weight_factor * np.random.rand(num_points)
    #Slightly random movement to simulate weight and subtle variations

    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

