
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# Points: Head, Shoulders, Elbows, Wrists, Hips, Knees, Ankles
initial_positions = np.array([
    [0, 1],   # Head
    [-1, 0],  # Left Shoulder
    [1, 0],   # Right Shoulder
    [-2, -1], # Left Elbow
    [2, -1],  # Right Elbow
    [-1, -2], # Left Wrist
    [1, -2],  # Right Wrist
    [0, -3],  # Hips
    [-1, -4], # Left Knee
    [1, -4],  # Right Knee
    [-1, -5], # Left Ankle
    [1, -5],  # Right Ankle
    [-2, -6], # Left Foot
    [2, -6],  # Right Foot
    [0, -7]   # Center of Mass (for visualization)
])

# Define the sequence of keyframes for the forward roll
# Each keyframe is a 2D array representing the positions of the 15 points
keyframes = [
    initial_positions,  # Initial position
    np.array([
        [0, 0.5],  # Head
        [-1, -0.5],  # Left Shoulder
        [1, -0.5],  # Right Shoulder
        [-2, -1.5],  # Left Elbow
        [2, -1.5],  # Right Elbow
        [-1, -2.5],  # Left Wrist
        [1, -2.5],  # Right Wrist
        [0, -3.5],  # Hips
        [-1, -4.5],  # Left Knee
        [1, -4.5],  # Right Knee
        [-1, -5.5],  # Left Ankle
        [1, -5.5],  # Right Ankle
        [-2, -6.5],  # Left Foot
        [2, -6.5],  # Right Foot
        [0, -7.5]   # Center of Mass
    ]),
    np.array([
        [0, 0],  # Head
        [-1, -1],  # Left Shoulder
        [1, -1],  # Right Shoulder
        [-2, -2],  # Left Elbow
        [2, -2],  # Right Elbow
        [-1, -3],  # Left Wrist
        [1, -3],  # Right Wrist
        [0, -4],  # Hips
        [-1, -5],  # Left Knee
        [1, -5],  # Right Knee
        [-1, -6],  # Left Ankle
        [1, -6],  # Right Ankle
        [-2, -7],  # Left Foot
        [2, -7],  # Right Foot
        [0, -8]   # Center of Mass
    ]),
    np.array([
        [0, -0.5],  # Head
        [-1, -1.5],  # Left Shoulder
        [1, -1.5],  # Right Shoulder
        [-2, -2.5],  # Left Elbow
        [2, -2.5],  # Right Elbow
        [-1, -3.5],  # Left Wrist
        [1, -3.5],  # Right Wrist
        [0, -4.5],  # Hips
        [-1, -5.5],  # Left Knee
        [1, -5.5],  # Right Knee
        [-1, -6.5],  # Left Ankle
        [1, -6.5],  # Right Ankle
        [-2, -7.5],  # Left Foot
        [2, -7.5],  # Right Foot
        [0, -9]   # Center of Mass
    ]),
    np.array([
        [0, -1],  # Head
        [-1, -2],  # Left Shoulder
        [1, -2],  # Right Shoulder
        [-2, -3],  # Left Elbow
        [2, -3],  # Right Elbow
        [-1, -4],  # Left Wrist
        [1, -4],  # Right Wrist
        [0, -5],  # Hips
        [-1, -6],  # Left Knee
        [1, -6],  # Right Knee
        [-1, -7],  # Left Ankle
        [1, -7],  # Right Ankle
        [-2, -8],  # Left Foot
        [2, -8],  # Right Foot
        [0, -10]   # Center of Mass
    ])
]

# Interpolate between keyframes to create smooth motion
num_frames = 50
interpolated_positions = []
for i in range(len(keyframes) - 1):
    start = keyframes[i]
    end = keyframes[i + 1]
    for t in np.linspace(0, 1, num_frames // len(keyframes)):
        interpolated = (1 - t) * start + t * end
        interpolated_positions.append(interpolated)

# Create the animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-10, 2)
ax.axis('off')  # Hide axes for cleaner visualization

scatter = ax.scatter([], [], s=50, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    positions = interpolated_positions[frame]
    scatter.set_offsets(positions)
    return scatter,

ani = FuncAnimation(
    fig, update, frames=len(interpolated_positions), init_func=init,
    blit=True, interval=50, repeat=True
)

plt.show()
