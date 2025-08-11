
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions for 15 point-lights (simplified human figure)
def initial_positions():
    # Approximate joint positions for a human figure (head, shoulders, elbows, wrists, hips, knees, ankles)
    positions = np.array([
        [0, 10],  # Head
        [-2, 8],  # Left shoulder
        [-4, 6],  # Left elbow
        [-5, 4],  # Left wrist
        [2, 8],   # Right shoulder
        [4, 6],   # Right elbow
        [5, 4],   # Right wrist
        [-1, 5],  # Left hip
        [-2, 2],  # Left knee
        [-2, 0],  # Left ankle
        [1, 5],   # Right hip
        [2, 2],   # Right knee
        [2, 0],   # Right ankle
        [0, 7],   # Chest
        [0, 5]    # Pelvis
    ])
    return positions

# Update function for animation
def update(frame, points, scat):
    # Simulate jumping motion with a sinusoidal pattern for vertical movement
    t = frame * 0.1
    amplitude = 2.0  # Jump height
    offset = amplitude * np.sin(t)  # Vertical displacement
    
    # Biomechanically plausible movement: limbs follow body
    new_positions = initial_positions().copy()
    new_positions[:, 1] += offset  # Move all points vertically
    
    # Add slight limb movement for realism
    if offset > 0:  # Upward motion
        new_positions[2:4, 1] -= 0.5 * offset  # Arms swing down
        new_positions[6:8, 1] -= 0.5 * offset  # Legs swing down
    else:  # Downward motion
        new_positions[2:4, 1] += 0.5 * abs(offset)  # Arms swing up
        new_positions[6:8, 1] += 0.5 * abs(offset)  # Legs swing up
    
    scat.set_offsets(new_positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_facecolor('black')
ax.set_xlim(-6, 6)
ax.set_ylim(-2, 12)
ax.axis('off')

# Initialize scatter plot
points = initial_positions()
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), fargs=(points, scat),
                             interval=50, blit=True)

plt.show()
