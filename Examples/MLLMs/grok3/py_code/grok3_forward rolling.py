
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define joint positions for a forward roll (simplified 2D representation)
# 15 point-lights: head, shoulders, elbows, wrists, hips, knees, ankles
def get_frame(t, duration=2.0, fps=30):
    t = t % duration
    phase = 2 * np.pi * (t / duration)
    
    # Base positions and movements (approximated for forward roll)
    if t < duration / 2:
        # First half: rolling forward
        head = [np.sin(phase) * 2, np.cos(phase) * 2]
        shoulders = [0, 1 + np.sin(phase) * 0.5]
        elbows = [-0.5 + np.sin(phase) * 0.3, 0.5 + np.cos(phase) * 0.3]
        wrists = [-1 + np.sin(phase) * 0.4, 0 + np.cos(phase) * 0.2]
        hips = [0.5 + np.sin(phase) * 0.2, -0.5 + np.cos(phase) * 0.3]
        knees = [0.7 + np.sin(phase) * 0.2, -1 + np.cos(phase) * 0.3]
        ankles = [0.9 + np.sin(phase) * 0.2, -1.5 + np.cos(phase) * 0.3]
    else:
        # Second half: returning to upright
        head = [np.sin(phase) * 1.5, np.cos(phase) * 1.5 + 2]
        shoulders = [0, 2 + np.sin(phase) * 0.3]
        elbows = [-0.5 + np.sin(phase) * 0.2, 1.5 + np.cos(phase) * 0.2]
        wrists = [-1 + np.sin(phase) * 0.3, 1 + np.cos(phase) * 0.1]
        hips = [0.5 + np.sin(phase) * 0.1, 0.5 + np.cos(phase) * 0.2]
        knees = [0.7 + np.sin(phase) * 0.1, 0 + np.cos(phase) * 0.2]
        ankles = [0.9 + np.sin(phase) * 0.1, -0.5 + np.cos(phase) * 0.2]

    return np.array([head, shoulders[0], shoulders[1], elbows[0], elbows[1], 
                     wrists[0], wrists[1], hips[0], hips[1], knees[0], knees[1], 
                     ankles[0], ankles[1], [0, 0], [0, 0]])  # Extra points for symmetry

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    positions = get_frame(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2.0, 60), interval=1000/30, blit=True)

plt.show()
