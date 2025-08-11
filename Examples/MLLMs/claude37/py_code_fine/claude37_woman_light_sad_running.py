
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of points
num_points = 15

# Initial positions of the point-lights
point_positions = np.array([
    [0, 0],  # Main body
    [0.1, 0.3],  # Head
    [-0.1, 0.3],  # Head
    [0.1, 0.2],  # Right shoulder
    [-0.1, 0.2],  # Left shoulder
    [0.05, 0.15],  # Right elbow
    [-0.05, 0.15],  # Left elbow
    [0.1, 0.0],  # Right hip
    [-0.1, 0.0],  # Left hip
    [0.15, -0.2],  # Right knee
    [-0.15, -0.2],  # Left knee
    [0.1, -0.4],  # Right ankle
    [-0.1, -0.4],  # Left ankle
    [0.15, -0.3],  # Right foot
    [-0.15, -0.3],  # Left foot
    [0, -0.5]   # Center of mass
])

# Create points
points, = ax.plot([], [], 'o', color='white', markersize=8)

# Function to initialize the background
def init():
    points.set_data([], [])
    return points,

# Function to update the points for each frame
def update(frame):
    # Simulate running motion with a simple sine wave transformation
    y_offset = np.sin(frame / 10.0) * 0.1
    # Update the y-coordinates for motion
    updated_positions = point_positions + np.array([[0], [y_offset]])
    points.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=100, init_func=init, interval=50, blit=True
)

# Show the animation
plt.show()
