
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 200
fps = 24

# Initial positions of the lights (simplified model)
initial_positions = np.array([
    [0.5, 1.5],  # Head
    [0.3, 1.2],  # Left Shoulder
    [0.7, 1.2],  # Right Shoulder
    [0.2, 0.9],  # Left Elbow
    [0.8, 0.9],  # Right Elbow
    [0.1, 0.6],  # Left Hand
    [0.9, 0.6],  # Right Hand
    [0.5, 1.0],  # Spine
    [0.5, 0.7],  # Hip
    [0.4, 0.4],  # Left Knee
    [0.6, 0.4],  # Right Knee
    [0.3, 0.1],  # Left Ankle
    [0.7, 0.1],  # Right Ankle
    [0.2, -0.2], # Left Foot
    [0.8, -0.2]  # Right Foot
])

# Walking motion parameters
def walking_motion(t):
    phase = t * 0.1
    x_offset = 0.3 * np.sin(phase)
    y_offset = 0.1 * np.cos(phase)
    
    # Adjustments for walking motion
    offsets = np.zeros_like(initial_positions)
    offsets[1:4, 0] += x_offset  # Shoulders move side to side
    offsets[1:4, 1] += y_offset  # Shoulders bob up and down slightly
    
    offsets[4:7, 0] += -x_offset  # Arms move opposite to shoulders
    offsets[4:7, 1] += -y_offset
    
    offsets[7:, 0] += 0.2 * np.sin(phase + np.pi/2)  # Legs move forward and back
    offsets[9:, 1] += 0.1 * np.cos(phase * 2)       # Knees and feet bob
    
    return offsets

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize points
points, = ax.plot([], [], 'o', markersize=10, color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    offsets = walking_motion(i)
    positions = initial_positions + offsets
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
