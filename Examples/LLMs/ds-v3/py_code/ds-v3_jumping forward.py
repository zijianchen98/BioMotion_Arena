
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of frames and point-lights
num_frames = 30
num_points = 15

# Define the initial positions of the point-lights (relative to the body)
# These are approximate positions for a standing person (x, y)
initial_positions = np.array([
    [0, 1.0],    # Head
    [0, 0.8],    # Neck
    [-0.2, 0.6], # Left shoulder
    [0.2, 0.6],  # Right shoulder
    [-0.2, 0.4], # Left elbow
    [0.2, 0.4],  # Right elbow
    [-0.2, 0.2], # Left hand
    [0.2, 0.2],  # Right hand
    [0, 0.5],    # Torso center
    [-0.1, 0.0], # Left hip
    [0.1, 0.0],  # Right hip
    [-0.1, -0.3],# Left knee
    [0.1, -0.3], # Right knee
    [-0.1, -0.6],# Left foot
    [0.1, -0.6]  # Right foot
])

# Function to generate positions for each frame
def generate_positions(t):
    positions = np.zeros_like(initial_positions)
    
    # Time-dependent parameters for jumping motion
    jump_height = 0.5 * np.sin(t * np.pi)  # Sinusoidal jump motion
    forward_motion = 0.1 * t  # Forward movement
    
    # Vertical movement (applied to all points)
    positions[:, 1] = initial_positions[:, 1] + jump_height
    
    # Forward movement (applied to all points)
    positions[:, 0] = initial_positions[:, 0] + forward_motion
    
    # Additional limb movements for realism
    # Arms swing during jump
    arm_swing = 0.3 * np.sin(t * 2 * np.pi)
    positions[2:8:2, 0] = initial_positions[2:8:2, 0] - 0.1 * arm_swing  # Left arm
    positions[3:8:2, 0] = initial_positions[3:8:2, 0] + 0.1 * arm_swing  # Right arm
    
    # Leg bending during jump
    leg_bend = 0.2 * np.sin(t * np.pi)
    positions[10:, 1] = initial_positions[10:, 1] - leg_bend  # Legs bend during jump
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Create point-lights
points = [Circle((0, 0), 0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Animation update function
def update(frame):
    t = frame / num_frames
    positions = generate_positions(t)
    for i, point in enumerate(points):
        point.center = (positions[i, 0], positions[i, 1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.tight_layout()
plt.show()
