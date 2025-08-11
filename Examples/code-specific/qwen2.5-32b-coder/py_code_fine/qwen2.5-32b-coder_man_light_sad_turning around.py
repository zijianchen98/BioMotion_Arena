
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 10  # seconds
FRAME_COUNT = FPS * DURATION

# Initial positions for the sadman's joints (simplified)
initial_positions = np.array([
    [0, 0],  # Head
    [-0.1, -0.3],  # Left Shoulder
    [-0.2, -0.6],  # Left Elbow
    [-0.1, -0.9],  # Left Hand
    [0.1, -0.3],  # Right Shoulder
    [0.2, -0.6],  # Right Elbow
    [0.1, -0.9],  # Right Hand
    [0, -1.2],  # Torso
    [-0.1, -1.5],  # Left Hip
    [-0.2, -1.8],  # Left Knee
    [-0.1, -2.1],  # Left Foot
    [0.1, -1.5],  # Right Hip
    [0.2, -1.8],  # Right Knee
    [0.1, -2.1],  # Right Foot
])

# Function to generate a turning motion
def generate_turning_motion(t):
    # Simple circular motion for the torso
    angle = 2 * np.pi * t / FRAME_COUNT
    x_offset = 0.5 * np.sin(angle)
    y_offset = 0.5 * np.cos(angle)
    
    # Update positions based on the torso's motion
    positions = initial_positions.copy()
    positions[:, 0] += x_offset
    positions[:, 1] += y_offset
    
    # Rotate the limbs around the torso
    torso_pos = positions[7]
    for i in range(1, 7):  # Limbs
        relative_pos = positions[i] - torso_pos
        rotation_angle = 0.1 * np.sin(4 * np.pi * t / FRAME_COUNT) if i < 4 else -0.1 * np.sin(4 * np.pi * t / FRAME_COUNT)
        cos_theta, sin_theta = np.cos(rotation_angle), np.sin(rotation_angle)
        rotated_pos = np.dot(np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]]), relative_pos)
        positions[i] = torso_pos + rotated_pos
    
    return positions

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    positions = generate_turning_motion(i)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = FuncAnimation(fig, animate, frames=FRAME_COUNT, init_func=init, blit=True, interval=1000/FPS)
plt.show()
