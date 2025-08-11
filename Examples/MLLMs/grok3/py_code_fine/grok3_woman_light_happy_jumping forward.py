
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human stick figure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-4, 6], [4, 6],  # elbows
    [-6, 4], [6, 4],  # wrists
    [-1, 5], [1, 5],  # hips
    [-2, 2], [2, 2],  # knees
    [-3, 0], [3, 0],  # ankles
    [0, 7], [0, 6], [0, 5]  # torso (3 points for stability)
])

# Number of frames for one jump cycle
frames = 60
positions = np.zeros((frames, 15, 2))

# Simulate a jumping forward motion (simplified biomechanics)
for i in range(frames):
    t = i / frames * 2 * np.pi  # One complete cycle
    # Vertical motion (jump)
    height = 2 * np.sin(t) + 5  # Jump height
    # Forward motion
    forward = 5 * t / (2 * np.pi)  # Linear forward movement
    # Update positions with natural joint movement
    positions[i] = initial_positions + [forward, height]
    # Add slight joint articulation (e.g., bending knees and elbows during jump)
    if 0 <= t <= np.pi:  # Ascent phase
        positions[i, [6, 7], 1] -= 1 * np.sin(t)  # Knees bend
        positions[i, [4, 5], 1] -= 0.5 * np.sin(t)  # Elbows bend
    else:  # Descent phase
        positions[i, [6, 7], 1] += 1 * np.sin(t - np.pi)
        positions[i, [4, 5], 1] += 0.5 * np.sin(t - np.pi)

# Set up the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-2, 12)
ax.axis('off')
scat = ax.scatter([], [], c='white', s=50)

# Animation update function
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
