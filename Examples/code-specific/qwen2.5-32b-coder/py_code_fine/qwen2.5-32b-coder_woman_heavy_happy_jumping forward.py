
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 100
fps = 24
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points (simplified model)
initial_positions = np.array([
    [0.0, 0.6],  # Head
    [-0.1, 0.5], [-0.1, 0.4], [-0.1, 0.3],  # Left arm
    [0.1, 0.5], [0.1, 0.4], [0.1, 0.3],  # Right arm
    [0.0, 0.4],  # Torso top
    [0.0, 0.3],  # Torso middle
    [0.0, 0.2],  # Torso bottom
    [-0.1, 0.1], [0.1, 0.1],  # Legs top
    [-0.1, 0.0], [0.1, 0.0]   # Legs bottom
])

# Create scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, color='white')

def update(frame):
    t = frame / frames * 2 * np.pi
    # Define the jumping motion with a sine wave for vertical movement and a simple harmonic for horizontal sway
    positions = initial_positions.copy()
    
    # Vertical jump
    positions[:, 1] += 0.1 * np.sin(t)
    
    # Horizontal sway
    positions[:, 0] += 0.05 * np.sin(2 * t)
    
    # Adjustments for more realistic motion
    # Arms swing forward and backward
    arm_swing = 0.05 * np.sin(3 * t)
    positions[1:4, 0] -= arm_swing
    positions[5:8, 0] += arm_swing
    
    # Legs move in opposite directions
    leg_swing = 0.05 * np.sin(3 * t + np.pi)
    positions[11:13, 0] -= leg_swing
    positions[13:15, 0] += leg_swing
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
