
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of 15 point-lights for a running sadman
# These coordinates are approximate and based on a simplified biomechanical model
initial_positions = np.array([
    [0, 10],  # Head
    [0, 8],   # Neck
    [0, 6],   # Chest
    [-1, 4],  # Left shoulder
    [1, 4],   # Right shoulder
    [-2, 2],  # Left elbow
    [2, 2],   # Right elbow
    [-3, 0],  # Left wrist
    [3, 0],   # Right wrist
    [0, 4],   # Hip
    [-1, 2],  # Left hip
    [1, 2],   # Right hip
    [-2, 0],  # Left knee
    [2, 0],   # Right knee
    [-3, -2], # Left ankle
    [3, -2]   # Right ankle
]) * 10  # Scale up for visibility

# Number of frames for the animation
n_frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Function to update the positions for each frame
def update(frame):
    # Simple sinusoidal motion to simulate running
    t = frame / n_frames * 2 * np.pi
    # Base movement (forward motion)
    base_x = frame * 0.5  # Slow forward movement
    # Leg and arm swinging
    leg_phase = np.sin(t)
    arm_phase = np.cos(t)
    
    positions = initial_positions.copy()
    # Hip movement
    positions[10, 1] += leg_phase * 10  # Left hip
    positions[11, 1] += -leg_phase * 10  # Right hip
    # Knee movement
    positions[12, 1] += leg_phase * 15  # Left knee
    positions[13, 1] += -leg_phase * 15  # Right knee
    # Ankle movement
    positions[14, 1] += leg_phase * 20  # Left ankle
    positions[15, 1] += -leg_phase * 20  # Right ankle
    # Arm movement
    positions[5, 1] += arm_phase * 10  # Left elbow
    positions[6, 1] += -arm_phase * 10  # Right elbow
    # Wrist movement
    positions[7, 1] += arm_phase * 15  # Left wrist
    positions[8, 1] += -arm_phase * 15  # Right wrist
    
    # Apply base movement
    positions[:, 0] += base_x
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
