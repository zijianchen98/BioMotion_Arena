
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 120
dt = 0.1
g = 9.81

# Initial positions and velocities
positions = np.zeros((num_lights, 2))
velocities = np.zeros((num_lights, 2))

# Define initial positions of the lights
def initialize_positions():
    # Head, torso, hips
    positions[0] = [0, 1.8]  # Head
    positions[1] = [0, 1.6]  # Upper torso
    positions[2] = [0, 1.4]  # Lower torso
    positions[3] = [0, 1.2]  # Hips
    
    # Right arm
    positions[4] = [-0.2, 1.6]  # Shoulder
    positions[5] = [-0.4, 1.4]  # Elbow
    positions[6] = [-0.6, 1.2]  # Hand
    
    # Left arm
    positions[7] = [0.2, 1.6]   # Shoulder
    positions[8] = [0.4, 1.4]   # Elbow
    positions[9] = [0.6, 1.2]   # Hand
    
    # Right leg
    positions[10] = [-0.1, 1.0]  # Hip joint
    positions[11] = [-0.1, 0.8]  # Knee
    positions[12] = [-0.1, 0.6]  # Foot
    
    # Left leg
    positions[13] = [0.1, 1.0]   # Hip joint
    positions[14] = [0.1, 0.8]   # Knee
    positions[15] = [0.1, 0.6]   # Foot

# Update function for the animation
def update(frame):
    global positions, velocities
    
    # Simple physics for jumping
    if frame < 30:
        velocities[3:, 1] -= g * dt  # Gravity affects only the lower body
    else:
        velocities[3:, 1] += g * dt  # Gravity affects only the lower body
    
    # Jumping motion
    if frame == 0:
        velocities[3:, 1] = 4.0  # Initial upward velocity for the lower body
    
    # Update positions
    positions += velocities * dt
    
    # Simple constraints to mimic jumping forward
    if frame < 30:
        positions[:, 0] += 0.02 * dt  # Move forward
    else:
        positions[:, 0] += 0.01 * dt  # Move forward slower after reaching peak
    
    # Reset after landing
    if positions[12, 1] <= 0.0 or positions[15, 1] <= 0.0:
        initialize_positions()
        velocities = np.zeros((num_lights, 2))
    
    scatter.set_offsets(positions)
    return scatter,

# Initialize positions
initialize_positions()

# Create plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.axis('off')
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

# Create animation
ani = FuncAnimation(fig, update, frames=frames, blit=True, repeat=True)

plt.show()
