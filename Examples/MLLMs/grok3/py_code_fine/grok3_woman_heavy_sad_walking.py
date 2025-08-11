
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the initial positions and structure of the 15 point-lights (simplified human figure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [-2, 8],  # left shoulder, right shoulder
    [-4, 6], [-4, 6],  # left elbow, right elbow
    [-6, 4], [-6, 4],  # left wrist, right wrist
    [0, 0], [0, 0],  # left hip, right hip
    [-2, -2], [-2, -2],  # left knee, right knee
    [-4, -4], [-4, -4]   # left ankle, right ankle
]) * 10  # Scale for visibility

# Parameters for walking motion
frames = 100
gait_cycle = 2 * np.pi  # One complete gait cycle
speed = 0.1  # Walking speed
amplitude = 2  # Amplitude of leg and arm swing

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('black')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.axis('off')

# Create scatter points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / frames * gait_cycle
    positions = initial_positions.copy()

    # Simulate walking motion (simplified biomechanical motion)
    # Horizontal movement
    positions[:, 0] += speed * frame * 10
    
    # Leg and arm swing (sinusoidal motion for natural gait)
    positions[6:8, 1] += amplitude * np.sin(t)  # Hips
    positions[8:10, 1] += amplitude * np.sin(t + np.pi/2)  # Knees
    positions[10:12, 1] += amplitude * np.sin(t + np.pi)  # Ankles
    positions[2:4, 1] += amplitude * np.sin(t + np.pi/2) * 0.5  # Shoulders
    positions[4:6, 1] += amplitude * np.sin(t + np.pi) * 0.5  # Elbows
    positions[6:8, 1] -= 0.5  # Slight downward shift to suggest heavy weight

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50, repeat=True)

plt.show()
