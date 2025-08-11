
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FRAME_RATE = 30
DURATION = 10  # seconds
TOTAL_FRAMES = FRAME_RATE * DURATION

# Define the initial positions of the points (simplified)
initial_positions = np.array([
    [0.0, 0.5],  # Head
    [-0.1, 0.4], [0.1, 0.4],  # Shoulders
    [-0.2, 0.3], [0.2, 0.3],  # Elbows
    [-0.2, 0.2], [0.2, 0.2],  # Wrists
    [0.0, 0.1],  # Hip
    [-0.1, 0.0], [0.1, 0.0],  # Knees
    [-0.1, -0.1], [0.1, -0.1],  # Ankles
    [-0.15, -0.2], [0.15, -0.2],  # Toes
    [0.0, 0.3],  # Neck
    [0.0, 0.4],  # Top of head
])

# Function to update the positions based on frame number
def update(frame):
    t = frame / TOTAL_FRAMES * 2 * np.pi  # Normalize frame to time in radians
    positions = initial_positions.copy()

    # Simple walking motion model
    positions[0] += np.array([0.05 * np.sin(t), 0.0])
    positions[1:3] += np.array([[-0.1 * np.cos(t), 0.0], [0.1 * np.cos(t), 0.0]])
    positions[3:5] += np.array([[-0.2 * np.sin(t), 0.0], [0.2 * np.sin(t), 0.0]])
    positions[6:8] += np.array([[-0.2 * np.cos(t), 0.0], [0.2 * np.cos(t), 0.0]])
    positions[9:11] += np.array([[-0.1 * np.sin(2*t), 0.0], [0.1 * np.sin(2*t), 0.0]])
    positions[11:13] += np.array([[-0.15 * np.cos(2*t), 0.0], [0.15 * np.cos(2*t), 0.0]])

    scatter.set_offsets(positions)
    return scatter,

# Setup the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.7)
ax.axis('off')
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FRAME_RATE, blit=True)

plt.show()
