
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 5)
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Define 15 point-light positions for a jumping human (simplified biomechanical model)
# Initial positions (head, shoulders, elbows, wrists, hips, knees, ankles)
initial_positions = np.array([
    [0, 4],    # Head
    [-0.3, 3.5], [0.3, 3.5],  # Shoulders
    [-0.5, 3], [-0.1, 3],     # Elbows
    [-0.6, 2.5], [0, 2.5],    # Wrists
    [0, 2],    # Hip
    [-0.2, 1.5], [0.2, 1.5],  # Knees
    [-0.3, 0.5], [0.3, 0.5]   # Ankles
])

# Number of frames for the animation
n_frames = 60

# Create scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def update(frame):
    t = frame / n_frames
    # Parametric motion for jumping forward (simplified)
    # Vertical motion (parabolic jump)
    y_offset = -4 * (t - 0.5) ** 2 + 1 if t <= 0.5 else -4 * (t - 1.5) ** 2 + 1
    # Forward motion
    x_offset = 2 * t
    
    # Apply biomechanical constraints
    positions = initial_positions.copy()
    positions[:, 0] += x_offset  # Move all points forward
    positions[:, 1] += y_offset  # Apply jump height
    
    # Add slight arm and leg swing
    if t < 0.5:
        positions[4, 1] += 0.2 * np.sin(4 * np.pi * t)  # Wrist swing
        positions[6, 1] += 0.2 * np.sin(4 * np.pi * t)  # Ankle swing
    else:
        positions[4, 1] -= 0.2 * np.sin(4 * np.pi * t)  # Reverse swing
        positions[6, 1] -= 0.2 * np.sin(4 * np.pi * t)
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
