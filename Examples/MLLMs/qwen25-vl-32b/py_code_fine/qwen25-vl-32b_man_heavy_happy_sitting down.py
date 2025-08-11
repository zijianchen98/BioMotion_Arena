
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial and final positions for the sitting-down motion
# Each row represents a joint's (x, y) position
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
    [0.0, -0.4],  # Head
    [-0.1, -0.6], # Left shoulder
    [0.1, -0.6],  # Right shoulder
    [-0.2, -0.8], # Left elbow
    [0.2, -0.8],  # Right elbow
    [-0.3, -1.0], # Left wrist
    [0.3, -1.0],  # Right wrist
    [0.0, -1.2],  # Hip
    [-0.1, -1.4], # Left knee
    [0.1, -1.4],  # Right knee
    [-0.2, -1.6], # Left ankle
    [0.2, -1.6],  # Right ankle
    [-0.3, -1.8], # Left foot
    [0.3, -1.8],  # Right foot
])

# Number of frames for the animation
num_frames = 50

# Interpolate between initial and final positions
interpolated_positions = []
for t in np.linspace(0, 1, num_frames):
    interpolated_positions.append((1 - t) * initial_positions + t * final_positions)

# Create the animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-2.0, 0.5)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    positions = interpolated_positions[frame]
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50
)

# Display the animation
plt.show()
