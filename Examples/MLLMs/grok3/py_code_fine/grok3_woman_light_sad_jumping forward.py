
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Define 15 point-light positions (simplified human figure with joints)
# Head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 1.5],  # Head
    [-0.3, 1.2], [0.3, 1.2],  # Shoulders
    [-0.6, 0.9], [0.6, 0.9],  # Elbows
    [-0.8, 0.6], [0.8, 0.6],  # Wrists
    [-0.2, 0.6], [0.2, 0.6],  # Hips
    [-0.3, 0.3], [0.3, 0.3],  # Knees
    [-0.4, 0], [0.4, 0],  # Ankles
    [0, 0.9],  # Chest (extra point)
    [0, 0.3]   # Pelvis (extra point)
])

# Initialize scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Jumping forward motion parameters
frames = 100
jump_height = 1.0
forward_step = 0.1
time = np.linspace(0, 2*np.pi, frames)

def update(frame):
    t = time[frame]
    # Vertical motion (parabolic jump)
    y_offset = jump_height * np.sin(t)
    # Forward motion
    x_offset = forward_step * t / (2*np.pi)
    # Apply slight biomechanical adjustments for realism
    positions = initial_positions.copy()
    positions[:, 0] += x_offset  # Forward movement
    positions[:, 1] += y_offset  # Jump height
    # Arm and leg swing (simplified sinusoidal motion)
    positions[3:5, 1] += 0.2 * np.sin(t + np.pi/2)  # Wrists
    positions[7:9, 1] += 0.2 * np.sin(t + np.pi/2)  # Ankles
    positions[2:4, 0] += 0.1 * np.sin(t)  # Elbows
    positions[6:8, 0] += 0.1 * np.sin(t)  # Knees
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
