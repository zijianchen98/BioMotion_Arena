
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Set parameters for the animation**
num_points = 15
frames = 60
time_steps = np.linspace(0, 2 * np.pi, frames)

# **Define the starting positions of the point-lights**
# Define positions for 'lying down' action
body_positions = np.array([
    [0, 1],   # Head
    [-0.3, 0.5],  # Left shoulder
    [0.3, 0.5],   # Right shoulder
    [-0.5, 0],    # Left elbow
    [0.5, 0],     # Right elbow
    [-0.7, -0.5], # Left hip
    [0.7, -0.5],  # Right hip
    [-0.3, -0.5], # Left knee
    [0.3, -0.5],  # Right knee
    [-0.5, -1],   # Left foot
    [0.5, -1],    # Right foot
    [0, 0],       # Center point
    [0, 0.3],     # Center body
    [0, -0.7],    # Center belly
    [0.4, -0.7],  # Offset for weight
    [-0.4, -0.7]   # Offset for weight
])

# **Initialize the figure**
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.axis('off')  # Turn off the axis

# **Create a scatter plot for point-lights**
points, = ax.plot([], [], 'o', color='white', markersize=10)

# **Update function for the animation**
def update(frame):
    # **Compute new positions based on a simple sine wave for demonstration**
    # Simulate smooth motion for the point-lights
    y_offset = 0.1 * np.sin(2 * np.pi * (time_steps[frame] + 0.5))  # for natural motion

    # Adjust positions to show motion
    new_positions = body_positions + np.array([0, y_offset])
    
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# **Create animation**
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True)

# **Display the animation**
plt.show()
