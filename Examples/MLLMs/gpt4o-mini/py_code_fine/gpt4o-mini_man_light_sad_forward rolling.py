
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the point lights (body joints in a forward rolling position)
initial_positions = np.array([
    [0, 3],   # Head
    [-1, 2],  # Left shoulder
    [1, 2],   # Right shoulder
    [-1, 1],  # Left elbow
    [1, 1],   # Right elbow
    [-1, 0],  # Left wrist
    [1, 0],   # Right wrist
    [0, 1],   # Chest
    [-0.5, -1], # Left hip
    [0.5, -1],  # Right hip
    [-0.5, -2], # Left knee
    [0.5, -2],  # Right knee
    [-0.5, -3], # Left ankle
    [0.5, -3],  # Right ankle
    [0, 0],   # Center of the body
    [0, -1]   # Center of rolling axis
])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create point light objects
points, = ax.plot([], [], 'wo', markersize=10)

# Initialize function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    # Calculate new positions based on rolling motion
    # Here we simulate a basic rolling motion
    rolling_angle = np.radians(frame * 10)  # Angle to simulate rolling
    rolling_radius = 2
    y_offset = -0.1 * frame  # Simulate downward rolling
    new_positions = initial_positions.copy()
    
    # Update positions for rolling effect
    new_positions[:, 0] += rolling_radius * np.sin(rolling_angle)
    new_positions[:, 1] += y_offset
    
    # Set new data for the points
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

plt.show()
