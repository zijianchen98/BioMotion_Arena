
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Initial positions of the lights (simplified model)
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left Shoulder
    [-2, -2], # Left Elbow
    [-3, -2], # Left Hand
    [1, -1],  # Right Shoulder
    [2, -2],  # Right Elbow
    [3, -2],  # Right Hand
    [0, -2],  # Spine
    [-1, -3], # Left Hip
    [-2, -4], # Left Knee
    [-3, -5], # Left Foot
    [1, -3],  # Right Hip
    [2, -4],  # Right Knee
    [3, -5],  # Right Foot
    [0, -6]   # Tailbone
])

# Function to create a waving motion
def waving_motion(t):
    phase = 2 * np.pi * t / frames
    waving_positions = initial_positions.copy()
    waving_positions[2, 1] -= 0.5 * np.sin(phase)  # Left Elbow
    waving_positions[3, 1] -= 0.5 * np.sin(phase)  # Left Hand
    waving_positions[5, 1] += 0.5 * np.sin(phase)  # Right Elbow
    waving_positions[6, 1] += 0.5 * np.sin(phase)  # Right Hand
    return waving_positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], s=100, color='white')

# Update function for animation
def update(frame):
    positions = waving_motion(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
