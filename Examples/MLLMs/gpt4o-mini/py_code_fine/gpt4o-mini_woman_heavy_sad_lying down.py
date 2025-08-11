
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Define the number of points
num_points = 15

# Initial positions of the point-lights
# Defining a "lying down" pose with slight weight
positions = np.array([
    [0, 0.5],   # Head
    [-0.2, 0.3],  # Left shoulder
    [0.2, 0.3],   # Right shoulder
    [-0.3, 0.1],  # Left hand
    [0.3, 0.1],   # Right hand
    [-0.1, -0.1], # Left elbow
    [0.1, -0.1],  # Right elbow
    [-0.2, -0.3], # Left hip
    [0.2, -0.3],  # Right hip
    [-0.15, -0.5],# Left knee
    [0.15, -0.5], # Right knee
    [-0.1, -0.7], # Left ankle
    [0.1, -0.7],  # Right ankle
    [0, 0.1],     # Center of mass
    [0, 0],       # Additional point for body motion
    [0, 0]        # Additional ground point
])

# Create point light objects
points, = ax.plot([], [], 'wo', markersize=12)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate
def animate(frame):
    # Update positions for each frame to simulate a smooth lying down motion
    global positions
    weights = np.array([-0.01, 0.01, -0.005, 0.005] * 3 + [0, 0])
    
    # Simulate slight upward motion
    positions += weights
    
    # Constrain positions to stay within viewing limits
    positions[:, 1] = np.clip(positions[:, 1], -1, 1)

    # Update the data of the points
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
