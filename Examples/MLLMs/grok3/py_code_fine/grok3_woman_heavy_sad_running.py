
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates and motion for 15 point-lights representing a sad woman running
# These are approximate positions based on a human figure with biomechanical plausibility
initial_positions = np.array([
    [0, 10],  # Head
    [0, 8],   # Chest
    [0, 6],   # Pelvis
    [-1, 5],  # Left shoulder
    [1, 5],   # Right shoulder
    [-1.5, 3], # Left elbow
    [1.5, 3],  # Right elbow
    [-2, 1],   # Left wrist
    [2, 1],    # Right wrist
    [-0.5, 4], # Left hip
    [0.5, 4],  # Right hip
    [-1, 2],   # Left knee
    [1, 2],    # Right knee
    [-1.5, 0], # Left ankle
    [1.5, 0]   # Right ankle
])

# Motion parameters for running (sinusoidal motion for limbs, forward progression)
def update_points(frame):
    t = frame * 0.1  # Time parameter for smooth motion
    positions = initial_positions.copy()
    
    # Forward progression
    positions[:, 0] += t * 2  # Move rightward
    
    # Arm and leg swinging (simplified sinusoidal motion)
    positions[6, 1] = initial_positions[6, 1] + np.sin(t) * 2  # Right elbow
    positions[7, 1] = initial_positions[7, 1] + np.sin(t + np.pi/2) * 2  # Right wrist
    positions[5, 1] = initial_positions[5, 1] + np.sin(t + np.pi) * 2  # Left elbow
    positions[4, 1] = initial_positions[4, 1] + np.sin(t + 3*np.pi/2) * 2  # Left wrist
    
    positions[11, 1] = initial_positions[11, 1] + np.sin(t) * 2  # Left knee
    positions[12, 1] = initial_positions[12, 1] + np.sin(t + np.pi/2) * 2  # Right knee
    positions[13, 1] = initial_positions[13, 1] + np.sin(t + np.pi) * 2  # Left ankle
    positions[14, 1] = initial_positions[14, 1] + np.sin(t + 3*np.pi/2) * 2  # Right ankle
    
    # Slight slumping for sad posture
    positions[0:3, 1] -= 0.5  # Head, chest, pelvis slightly lower
    
    scatter.set_offsets(positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 15)  # Adjusted for movement
ax.set_ylim(-2, 12)
ax.axis('off')

# Plot the initial points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update_points, frames=100, interval=50, blit=True)

plt.show()
