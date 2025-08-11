
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 60
fps = 30
background_color = 'black'
point_color = 'white'

# Initial positions and parameters for a 'sad woman with heavy weight jumping up'
# These are simplified and may not fully capture the complexity of real biomechanics
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.2, -0.4], # Left Shoulder
    [0.2, -0.4],  # Right Shoulder
    [-0.3, -0.8], # Left Elbow
    [0.3, -0.8],  # Right Elbow
    [-0.3, -1.2], # Left Hand
    [0.3, -1.2],  # Right Hand
    [0.0, -1.0],  # Spine
    [0.0, -1.4],  # Hip
    [-0.2, -1.8], # Left Knee
    [0.2, -1.8],  # Right Knee
    [-0.2, -2.2], # Left Foot
    [0.2, -2.2],  # Right Foot
    [0.0, -0.6],  # Chest
    [0.0, -0.2]   # Neck
])

# Function to calculate the position of each point at a given frame
def calculate_positions(frame):
    t = frame / frames * 2 * np.pi  # Time parameter
    positions = initial_positions.copy()
    
    # Jumping motion with a sine wave to simulate the up and down movement
    amplitude = 0.5
    frequency = 1.0
    phase = 0.0
    positions[:, 1] += amplitude * np.sin(frequency * t + phase)
    
    # Additional adjustments to simulate weight and sadness
    # Slight forward lean and asymmetry in movement
    positions[:, 0] += 0.1 * np.sin(0.5 * t)  # Lean forward with a smaller sine wave
    positions[2:, 1] -= 0.1 * np.cos(t)       # Asymmetry in lower body movement
    
    return positions

# Setup figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor(background_color)

# Create scatter plot for points
scat = ax.scatter([], [], s=100, c=point_color)

# Update function for animation
def update(frame):
    positions = calculate_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
