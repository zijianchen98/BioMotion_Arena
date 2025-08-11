
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial and final positions for the sitting-down motion
# Each row represents a joint position (x, y)
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.2], # Left shoulder
    [0.1, -0.2],  # Right shoulder
    [-0.2, -0.4], # Left elbow
    [0.2, -0.4],  # Right elbow
    [-0.3, -0.6], # Left wrist
    [0.3, -0.6],  # Right wrist
    [0.0, -0.8],  # Hip
    [-0.1, -1.0], # Left knee
    [0.1, -1.0],  # Right knee
    [-0.2, -1.2], # Left ankle
    [0.2, -1.2],  # Right ankle
    [-0.3, -1.4], # Left foot
    [0.3, -1.4],  # Right foot
])

final_positions = np.array([
    [0.0, -0.5],  # Head
    [-0.1, -0.7], # Left shoulder
    [0.1, -0.7],  # Right shoulder
    [-0.2, -0.9], # Left elbow
    [0.2, -0.9],  # Right elbow
    [-0.3, -1.1], # Left wrist
    [0.3, -1.1],  # Right wrist
    [0.0, -1.3],  # Hip
    [-0.1, -1.5], # Left knee
    [0.1, -1.5],  # Right knee
    [-0.2, -1.7], # Left ankle
    [0.2, -1.7],  # Right ankle
    [-0.3, -1.9], # Left foot
    [0.3, -1.9],  # Right foot
])

# Number of frames for the animation
num_frames = 100

# Interpolate between initial and final positions
positions = np.linspace(initial_positions, final_positions, num_frames)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-2.0, 0.5)
ax.axis('off')  # Hide axes
ax.set_aspect('equal')

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white', edgecolors='none')

def init():
    """Initialize the animation."""
    scatter.set_offsets([])
    return scatter,

def update(frame):
    """Update the animation for each frame."""
    current_positions = positions[frame]
    scatter.set_offsets(current_positions)
    return scatter,

# Create the animation
ani = FuncAnimation(
    fig,
    update,
    frames=num_frames,
    init_func=init,
    blit=True,
    interval=50,  # 50 ms per frame
    repeat=False  # Play once
)

# Display the animation
plt.show()
