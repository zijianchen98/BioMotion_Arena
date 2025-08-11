
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of the point-lights
n_points = 15
initial_positions = np.array([
    [0, 1],  # Head
    [-0.2, 0.5],  # Shoulder 1
    [0.2, 0.5],  # Shoulder 2
    [-0.4, 0.2],  # Elbow 1
    [0.4, 0.2],  # Elbow 2
    [-0.6, 0],  # Hand 1
    [0.6, 0],  # Hand 2
    [0, -0.3],  # Torso
    [-0.2, -1],  # Hip 1
    [0.2, -1],  # Hip 2
    [-0.4, -1.5],  # Knee 1
    [0.4, -1.5],  # Knee 2
    [-0.6, -2],  # Foot 1
    [0.6, -2],  # Foot 2
    [0, 0]  # Center of mass
])

# Function to create jumping motion
def jump_motion(t, amplitude=0.5, frequency=1):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2.5, 1.5)
ax.axis('off')

# Create scatter plot for point-lights
scat = ax.scatter([], [], c='white', s=100)

# Update function for animation
def update(frame):
    positions = initial_positions.copy()
    t = frame / 60  # Assuming 60 frames per second
    
    # Head and center of mass motion
    positions[0, 1] = jump_motion(t, amplitude=0.3, frequency=1) + 1
    positions[-1, 1] = jump_motion(t, amplitude=0.3, frequency=1)
    
    # Torso motion
    positions[7, 1] = jump_motion(t, amplitude=0.3, frequency=1) - 0.3
    
    # Arm and shoulder motion
    positions[1:5, 1] = positions[1:5, 1] + jump_motion(t, amplitude=0.2, frequency=1)
    
    # Hip and leg motion
    positions[8:13, 1] = positions[8:13, 1] + jump_motion(t, amplitude=0.4, frequency=1)
    
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=range(60), interval=16, blit=True)

# Show animation
plt.show()
