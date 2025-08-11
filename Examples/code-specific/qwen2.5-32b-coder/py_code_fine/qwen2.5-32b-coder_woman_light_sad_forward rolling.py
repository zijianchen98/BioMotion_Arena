
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = int(fps * duration)

# Initial positions of the lights (simplified)
# These positions are placeholders and should be refined for realism
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.1], # Left Shoulder
    [0.1, -0.1],  # Right Shoulder
    [-0.2, -0.3], # Left Elbow
    [0.2, -0.3],  # Right Elbow
    [-0.3, -0.5], # Left Wrist
    [0.3, -0.5],  # Right Wrist
    [0.0, -0.6],  # Spine
    [-0.1, -0.8], # Left Hip
    [0.1, -0.8],  # Right Hip
    [-0.2, -1.0], # Left Knee
    [0.2, -1.0],  # Right Knee
    [-0.3, -1.2], # Left Ankle
    [0.3, -1.2],  # Right Ankle
    [0.0, -1.4]   # Toes
])

# Function to generate forward rolling motion
def forward_rolling(t):
    phase = t * 2 * np.pi / frames
    positions = initial_positions.copy()
    
    # Simple model for forward rolling motion
    # This is a placeholder and should be refined for realism
    positions[:, 1] += 0.1 * np.sin(phase + np.linspace(0, 2*np.pi, num_lights))
    positions[:, 0] += 0.1 * np.cos(phase + np.linspace(0, 2*np.pi, num_lights))
    
    return positions

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 0.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], s=100, c='white')

# Update function for animation
def update(frame):
    positions = forward_rolling(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show animation
plt.show()
