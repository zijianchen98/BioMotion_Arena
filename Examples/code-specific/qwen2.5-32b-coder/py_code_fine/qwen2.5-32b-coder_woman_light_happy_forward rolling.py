
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
fps = 24
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the lights (simplified model of a person)
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [-0.1, 0.7], # Left eye
    [0.1, 0.7],  # Right eye
    [0.0, 0.6],  # Nose
    [0.0, 0.5],  # Neck
    [-0.1, 0.4], # Left shoulder
    [-0.2, 0.3], # Left elbow
    [-0.2, 0.2], # Left wrist
    [0.1, 0.4],  # Right shoulder
    [0.2, 0.3],  # Right elbow
    [0.2, 0.2],  # Right wrist
    [0.0, 0.3],  # Hip
    [-0.1, 0.2], # Left hip
    [-0.1, 0.1], # Left knee
    [-0.1, 0.0]  # Left foot
])

# Create scatter plot for the lights
lights = ax.scatter([], [], s=100, color='white')

def init():
    lights.set_offsets(initial_positions)
    return lights,

def animate(i):
    t = i / frames * 2 * np.pi
    positions = initial_positions.copy()
    
    # Simple forward rolling motion
    # Head and neck rotation
    head_neck_rotation = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t), np.cos(t)]
    ])
    positions[:5] = np.dot(positions[:5] - initial_positions[0], head_neck_rotation) + initial_positions[0]
    
    # Shoulder and arm swing
    arm_swing = np.array([
        [np.cos(t + np.pi/2), -np.sin(t + np.pi/2)],
        [np.sin(t + np.pi/2), np.cos(t + np.pi/2)]
    ])
    positions[5:9] = np.dot(positions[5:9] - initial_positions[5], arm_swing) + initial_positions[5]
    positions[9:13] = np.dot(positions[9:13] - initial_positions[9], arm_swing) + initial_positions[9]
    
    # Hip and leg swing
    leg_swing = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t), np.cos(t)]
    ])
    positions[12:] = np.dot(positions[12:] - initial_positions[12], leg_swing) + initial_positions[12]
    
    lights.set_offsets(positions)
    return lights,

ani = FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, repeat=True, interval=1000/fps)
plt.show()
