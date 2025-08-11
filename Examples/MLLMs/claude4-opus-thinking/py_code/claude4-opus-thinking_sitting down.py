
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points and frames
num_points = 15
num_frames = 60

# Initial configuration of point-lights (2D coordinates)
initial_positions = np.array([
    [0, 1],           # Head
    [-0.5, 0.8],     # Left shoulder
    [0.5, 0.8],      # Right shoulder
    [-0.6, 0.6],     # Left elbow
    [0.6, 0.6],      # Right elbow
    [-0.7, 0.3],     # Left wrist
    [0.7, 0.3],      # Right wrist
    [-0.5, 0.0],     # Left hip
    [0.5, 0.0],      # Right hip
    [-0.5, -0.3],    # Left knee
    [0.5, -0.3],     # Right knee
    [-0.5, -0.6],    # Left ankle
    [0.5, -0.6],     # Right ankle
    [0, 0],          # Center of mass (hip)
    [-0.2, -0.6],    # Lower body
    [0.2, -0.6]      # Lower body
])

# Function to update the position of point-lights for each frame
def animate(frame):
    # Clear previous points
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')

    # Calculate new positions mimicking sitting down motion
    y_shift = frame / num_frames * 0.5
    new_positions = initial_positions.copy()
    
    # Apply transformation to simulate the sitting motion
    new_positions[:, 1] -= y_shift  # Move down

    # Draw point-lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Create figure and axes for animation
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Create an animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/30, repeat=True)

# Show the animation
plt.show()
