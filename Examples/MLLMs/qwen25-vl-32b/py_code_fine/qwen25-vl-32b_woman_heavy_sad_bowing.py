
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions of the 15 points (x, y coordinates)
initial_positions = {
    'head': [0, 1.0],
    'left_shoulder': [-0.3, 0.8],
    'right_shoulder': [0.3, 0.8],
    'left_elbow': [-0.6, 0.5],
    'right_elbow': [0.6, 0.5],
    'left_wrist': [-0.9, 0.2],
    'right_wrist': [0.9, 0.2],
    'left_hip': [-0.3, 0.0],
    'right_hip': [0.3, 0.0],
    'left_knee': [-0.6, -0.3],
    'right_knee': [0.6, -0.3],
    'left_ankle': [-0.6, -0.8],
    'right_ankle': [0.6, -0.8]
}

# Convert to a list of (x, y) tuples
initial_points = [
    initial_positions['head'],
    initial_positions['left_shoulder'], initial_positions['right_shoulder'],
    initial_positions['left_elbow'], initial_positions['right_elbow'],
    initial_positions['left_wrist'], initial_positions['right_wrist'],
    initial_positions['left_hip'], initial_positions['right_hip'],
    initial_positions['left_knee'], initial_positions['right_knee'],
    initial_positions['left_ankle'], initial_positions['right_ankle']
]

# Define the final positions after bowing
final_positions = {
    'head': [0, 0.5],  # Head lowered
    'left_shoulder': [-0.3, 0.3],
    'right_shoulder': [0.3, 0.3],
    'left_elbow': [-0.6, 0.0],
    'right_elbow': [0.6, 0.0],
    'left_wrist': [-0.9, -0.3],
    'right_wrist': [0.9, -0.3],
    'left_hip': [-0.3, 0.0],
    'right_hip': [0.3, 0.0],
    'left_knee': [-0.6, -0.3],
    'right_knee': [0.6, -0.3],
    'left_ankle': [-0.6, -0.8],
    'right_ankle': [0.6, -0.8]
}

# Convert to a list of (x, y) tuples
final_points = [
    final_positions['head'],
    final_positions['left_shoulder'], final_positions['right_shoulder'],
    final_positions['left_elbow'], final_positions['right_elbow'],
    final_positions['left_wrist'], final_positions['right_wrist'],
    final_positions['left_hip'], final_positions['right_hip'],
    final_positions['left_knee'], final_positions['right_knee'],
    final_positions['left_ankle'], final_positions['right_ankle']
]

# Interpolate between initial and final positions
num_frames = 50
interpolated_positions = []
for t in np.linspace(0, 1, num_frames):
    interpolated = [(1 - t) * ip + t * fp for ip, fp in zip(initial_points, final_points)]
    interpolated_positions.append(interpolated)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')  # Hide axes
scat = ax.scatter([], [], s=50, c='white')

def update(frame):
    scat.set_offsets(interpolated_positions[frame])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
