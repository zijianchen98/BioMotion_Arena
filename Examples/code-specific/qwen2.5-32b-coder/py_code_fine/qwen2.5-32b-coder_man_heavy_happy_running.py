
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.5)
ax.axis('off')

# Initial positions for the point lights representing 'happyman running'
initial_positions = np.array([
    [-0.5, 0.9], [-0.4, 0.9], [-0.3, 0.9],  # Head and shoulders
    [-0.4, 0.7], [-0.3, 0.7],              # Upper arms
    [-0.4, 0.5], [-0.3, 0.5],              # Forearms
    [-0.45, 0.3], [-0.35, 0.3],            # Hands
    [-0.5, 0.1], [-0.3, 0.1],              # Hips
    [-0.5, -0.1], [-0.4, -0.3], [-0.3, -0.3] # Legs and feet
])

# Scatter plot for the point lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='white')

def update(frame):
    t = frame / frames  # Normalized time from 0 to 1
    
    # Define the movement functions for each body part
    def head_shoulder_x(t):
        return -0.5 + 0.1 * np.sin(2 * np.pi * t)
    
    def arm_upper_x(t):
        return -0.4 + 0.05 * np.sin(2 * np.pi * t + np.pi/2)
    
    def arm_forearm_x(t):
        return -0.4 + 0.05 * np.sin(2 * np.pi * t + np.pi)
    
    def hand_x(t):
        return -0.45 + 0.025 * np.sin(2 * np.pi * t + 3*np.pi/2)
    
    def hip_x(t):
        return -0.5 + 0.05 * np.sin(2 * np.pi * t)
    
    def leg_x(t):
        return -0.5 + 0.075 * np.sin(2 * np.pi * t + np.pi/4)
    
    # Update positions
    positions = np.array([
        [head_shoulder_x(t), 0.9], [head_shoulder_x(t) + 0.1, 0.9], [head_shoulder_x(t) + 0.2, 0.9],
        [arm_upper_x(t), 0.7], [arm_upper_x(t) + 0.1, 0.7],
        [arm_forearm_x(t), 0.5], [arm_forearm_x(t) + 0.1, 0.5],
        [hand_x(t), 0.3], [hand_x(t) + 0.1, 0.3],
        [hip_x(t), 0.1], [hip_x(t) + 0.2, 0.1],
        [leg_x(t), -0.1], [leg_x(t) + 0.1, -0.3], [leg_x(t) + 0.2, -0.3]
    ])
    
    scat.set_offsets(positions)

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=False)

plt.show()
