
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.axis('off')

# Initial positions of the point-lights (white dots)
points = np.array([
    (5, 9),  # Head
    (5, 8),  # Neck
    (5, 7),  # Chest
    (4, 6),  # Left Shoulder
    (6, 6),  # Right Shoulder
    (3, 5),  # Left Elbow
    (7, 5),  # Right Elbow
    (2, 4),  # Left Hand
    (8, 4),  # Right Hand
    (5, 6),  # Hips
    (4, 5),  # Left Hip
    (6, 5),  # Right Hip
    (3, 3),  # Left Knee
    (7, 3),  # Right Knee
    (2, 2),  # Left Foot
    (8, 2)   # Right Foot
])

# Create scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], c='white', s=100)

def update(frame):
    t = 2 * np.pi * frame / 50
    amplitude = 0.5
    jump_amp = 0.8
    
    points[:, 1] = points[:, 1] + amplitude * np.sin(t)
    points[0, 1] += jump_amp * np.sin(2 * t)
    points[1, 1] += jump_amp * np.sin(2 * t)
    points[2:6, 1] += jump_amp * np.sin(t)
    points[6:10, 1] += jump_amp * np.sin(t)
    points[10:14, 1] += jump_amp * np.sin(t)
    points[14:, 1] += jump_amp * np.sin(t)
    
    sc.set_offsets(points)

ani = animation.FuncAnimation(fig, update, frames=50, interval=50)

plt.show()
