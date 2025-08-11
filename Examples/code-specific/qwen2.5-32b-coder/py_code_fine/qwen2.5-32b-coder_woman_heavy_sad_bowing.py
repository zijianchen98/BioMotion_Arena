
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the lights
positions = np.array([
    [-0.05, 0.7],  # Head
    [-0.05, 0.6],  # Neck
    [-0.05, 0.5],  # Upper Spine
    [-0.05, 0.4],  # Lower Spine
    [-0.05, 0.3],  # Hips
    [-0.1, 0.2],   # Left Hip Joint
    [-0.2, 0.1],   # Left Knee
    [-0.15, 0.0],  # Left Ankle
    [-0.05, 0.2],  # Right Hip Joint
    [-0.0, 0.1],   # Right Knee
    [0.05, 0.0],   # Right Ankle
    [-0.05, 0.5],  # Left Shoulder
    [-0.1, 0.4],   # Left Elbow
    [-0.1, 0.3],   # Left Wrist
    [0.05, 0.5],   # Right Shoulder
    [0.1, 0.4],    # Right Elbow
    [0.1, 0.3]     # Right Wrist
])

# Create scatter plot for the lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

def update(frame):
    t = frame / frames * 2 * np.pi
    
    # Bowing motion
    new_positions = positions.copy()
    new_positions[:, 1] -= 0.1 * np.sin(t)  # Vertical bobbing
    new_positions[3:, 1] -= 0.1 * np.sin(t + np.pi/2)  # Legs bending
    new_positions[11:, 1] += 0.05 * np.sin(t)  # Arms swinging
    
    scatter.set_offsets(new_positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
