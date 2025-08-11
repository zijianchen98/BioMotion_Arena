
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the initial positions of 15 point-lights for a lying down sad woman
# These positions are approximate and based on a simplified human figure
initial_positions = np.array([
    [0, 0],    # Head
    [0.5, 0.5], # Right shoulder
    [-0.5, 0.5], # Left shoulder
    [0.7, 1.0], # Right elbow
    [-0.7, 1.0], # Left elbow
    [0.9, 1.5], # Right wrist
    [-0.9, 1.5], # Left wrist
    [0, 1.8],  # Hip
    [0.5, 2.3], # Right knee
    [-0.5, 2.3], # Left knee
    [0.7, 3.0], # Right ankle
    [-0.7, 3.0], # Left ankle
    [0.2, 0.2], # Right chest
    [-0.2, 0.2], # Left chest
    [0, 0.8]   # Neck
]) * 10  # Scale up for visibility

# Define motion parameters for a lying down motion (subtle breathing and slight arm movement)
frames = 100
time = np.linspace(0, 2 * np.pi, frames)
amplitude = 0.5  # Subtle movement amplitude
freq = 0.5       # Breathing frequency

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-15, 15)
ax.set_ylim(-5, 35)
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation update function
def update(frame):
    # Breathing motion (vertical movement for torso and limbs)
    breath = amplitude * np.sin(freq * time[frame])
    # Slight arm movement (natural sway while lying)
    arm_sway = 0.2 * np.sin(2 * freq * time[frame])
    
    # Update positions
    new_positions = initial_positions.copy()
    # Apply breathing to torso and limbs
    new_positions[0:5, 1] += breath  # Head, shoulders, elbows
    new_positions[5:7, 1] += breath  # Wrists
    new_positions[7:11, 1] += breath  # Hip, knees, ankles
    new_positions[12:15, 1] += breath  # Chest, neck
    # Apply slight arm sway
    new_positions[5, 0] += arm_sway  # Right wrist
    new_positions[6, 0] -= arm_sway  # Left wrist
    
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
