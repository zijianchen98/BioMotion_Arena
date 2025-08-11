
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
frames = 100

# Point-light positions for a happy woman sitting down (simplified representation)
# Starting points (x, y) for 15 points
# These are rough points representing a sitting position
point_positions = np.array([
    [0, 3],   # Head
    [-1, 2],  # Left shoulder
    [1, 2],   # Right shoulder
    [-1, 1],  # Left elbow
    [1, 1],   # Right elbow
    [-1.5, 0.5], # Left hand
    [1.5, 0.5],  # Right hand
    [-0.5, 0],  # Left hip
    [0.5, 0],   # Right hip
    [-1, -1],   # Left knee
    [1, -1],    # Right knee
    [-0.5, -2], # Left foot
    [0.5, -2],  # Right foot
    [0, 1.5],   # Neck
    [0, 3],     # Head top
    [0, 0]      # Center 
])

# Define the motion for sitting down. This is a simple linear movement as placeholder.
def get_positions(frame):
    # Create a oscillating sit down effect
    sit_down = point_positions.copy()
    sit_down[:, 1] -= 0.05 * frame  # Simulated downward motion
    return sit_down

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 4)
ax.set_facecolor('black')
lights, = ax.plot([], [], 'o', markersize=10, color='white')

# Initialization function
def init():
    lights.set_data([], [])
    return lights,

# Animation function
def animate(frame):
    positions = get_positions(frame)  # Get updated positions
    lights.set_data(positions[:, 0], positions[:, 1])  # Update point light positions
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=100, blit=True)

# Display the animation
plt.show()
