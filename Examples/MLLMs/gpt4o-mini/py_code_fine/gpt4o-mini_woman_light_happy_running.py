
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Parameters for the point lights representing the happy woman
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions of the point lights (they will form a stick figure)
initial_positions = np.array([
    [0, 1],   # Head
    [0, 0.5],  # Neck
    [-0.25, 0], # Left shoulder
    [0, 0],   # Center torso
    [0.25, 0], # Right shoulder
    [-0.25, -0.5], # Left elbow
    [0, -0.5], # Left hand
    [0.25, -0.5], # Right elbow
    [0, -0.5], # Right hand
    [-0.25, -1], # Left hip
    [0, -1],   # Center hip
    [0.25, -1], # Right hip
    [-0.25, -1.5], # Left knee
    [0, -1.5], # Left foot
    [0.25, -1.5], # Right knee
    [0, -1.5]  # Right foot
])

# Set the initial positions for the animation
points[:] = initial_positions

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Decide the running motion - this will be a simple side-to-side motion for demonstration
    global points
    # Running motion assuming a simple cyclic movement
    amplitude = 0.1
    phase_shift = frame * np.pi / 20  # Control speed
    
    # Update positions to simulate running
    points[:, 0] = initial_positions[:, 0] + amplitude * np.sin(phase_shift + np.linspace(0, np.pi, num_points))
    points[:, 1] = initial_positions[:, 1] - frame * 0.05  # Slight downward movement with time

    # Update scatter plot
    scat.set_offsets(points)
    
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.axis('off')  # Turn off the axis
plt.show()
