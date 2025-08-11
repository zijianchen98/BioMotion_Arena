
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of points
points = np.array([
    [0.0, 0.8],  # Head
    [-0.1, 0.7], [-0.1, 0.6], [-0.1, 0.5],  # Left arm
    [0.1, 0.7], [0.1, 0.6], [0.1, 0.5],  # Right arm
    [0.0, 0.4],  # Body
    [-0.1, 0.3], [-0.1, 0.2], [-0.1, 0.1],  # Left leg
    [0.1, 0.3], [0.1, 0.2], [0.1, 0.1]   # Right leg
])

# Scatter plot for points
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

def bowing_motion(t):
    """Function to define the bowing motion."""
    phase = t / TOTAL_FRAMES * 2 * np.pi
    amplitude = 0.1
    
    # Head and body tilt forward
    points[0, 1] = 0.8 - 0.1 * np.sin(phase)  # Head
    points[4, 1] = 0.4 - 0.1 * np.sin(phase)  # Left shoulder
    points[7, 1] = 0.4 - 0.1 * np.sin(phase)  # Body center
    points[10, 1] = 0.3 - 0.1 * np.sin(phase)  # Left hip
    points[13, 1] = 0.3 - 0.1 * np.sin(phase)  # Right hip
    
    # Arms move slightly
    points[1, 1] = 0.7 - 0.05 * np.cos(phase)  # Left upper arm
    points[4, 0] = -0.1 - 0.05 * np.sin(phase)  # Left shoulder
    points[7, 0] = -0.05 * np.sin(phase)  # Body center
    points[10, 0] = -0.1 - 0.05 * np.sin(phase)  # Left hip
    points[13, 0] = 0.1 + 0.05 * np.sin(phase)  # Right hip
    
    points[5, 1] = 0.7 - 0.05 * np.cos(phase)  # Right upper arm
    points[1, 0] = 0.1 + 0.05 * np.sin(phase)  # Right shoulder
    points[13, 0] = 0.1 + 0.05 * np.sin(phase)  # Right hip
    points[10, 0] = -0.1 - 0.05 * np.sin(phase)  # Left hip
    
    # Legs bend at knees
    points[10, 1] -= amplitude * np.sin(phase)  # Left knee
    points[13, 1] -= amplitude * np.sin(phase)  # Right knee
    points[11, 1] -= amplitude * np.sin(phase)  # Left lower leg
    points[14, 1] -= amplitude * np.sin(phase)  # Right lower leg

def update(frame):
    """Update function for animation."""
    bowing_motion(frame)
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

plt.show()
