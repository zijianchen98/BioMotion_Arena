
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 100
fps = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points (simplified for demonstration)
initial_positions = np.array([
    [-0.2, 0.8], [-0.1, 0.8], [0, 0.9], [0.1, 0.8], [0.2, 0.8],  # Head and neck
    [-0.2, 0.6], [-0.1, 0.6], [0, 0.7], [0.1, 0.6], [0.2, 0.6],  # Shoulders
    [-0.1, 0.4], [0.1, 0.4],                                    # Elbows
    [-0.1, 0.2], [0.1, 0.2],                                    # Hands
    [0, -0.1]                                                  # Center of gravity
])

# Scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='white')

def update(frame):
    t = frame / frames * 2 * np.pi  # Time variable for sinusoidal motion
    positions = initial_positions.copy()
    
    # Update positions for jumping motion
    # Vertical jump
    positions[:, 1] += 0.1 * np.sin(t)
    # Swing arms and legs
    swing_angle = 0.2 * np.sin(t + np.pi / 2)
    positions[[3, 7, 10, 12]] += np.array([swing_angle, 0])
    positions[[1, 5, 11, 13]] += np.array([-swing_angle, 0])
    # Move center of gravity vertically
    positions[14, 1] += 0.1 * np.sin(t)
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
