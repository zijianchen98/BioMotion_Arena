
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30

# Initial positions of the lights (simplified representation of a walking woman)
initial_positions = np.array([
    [0.0, 0.5],   # Head
    [-0.1, 0.4],  # Left eye
    [0.1, 0.4],   # Right eye
    [0.0, 0.3],   # Nose
    [0.0, 0.2],   # Neck
    [-0.1, 0.1],  # Left shoulder
    [0.1, 0.1],   # Right shoulder
    [-0.2, 0.0],  # Left elbow
    [0.2, 0.0],   # Right elbow
    [-0.3, -0.1], # Left hand
    [0.3, -0.1],  # Right hand
    [0.0, 0.0],   # Torso
    [-0.1, -0.2], # Left hip
    [0.1, -0.2],  # Right hip
    [0.0, -0.4]   # Pelvis
])

# Function to update positions based on walking cycle
def update_positions(t):
    positions = initial_positions.copy()
    
    # Walking motion parameters
    stride_length = 0.2
    arm_swing_amplitude = 0.1
    leg_lift_height = 0.1
    phase_shift = np.pi / 2
    
    # Update positions
    for i in range(num_lights):
        if i in [5, 7, 9]:  # Left arm, left elbow, left hand
            positions[i, 1] += arm_swing_amplitude * np.sin(2 * np.pi * t / frames + phase_shift)
        elif i in [6, 8, 10]:  # Right arm, right elbow, right hand
            positions[i, 1] += arm_swing_amplitude * np.sin(2 * np.pi * t / frames)
        elif i == 11:  # Torso
            positions[i, 0] += stride_length * np.sin(np.pi * t / frames) / 2
        elif i in [12, 14]:  # Left hip, pelvis
            positions[i, 1] += leg_lift_height * np.sin(2 * np.pi * t / frames + phase_shift)
        elif i == 13:  # Right hip
            positions[i, 1] += leg_lift_height * np.sin(2 * np.pi * t / frames)
    
    return positions

# Initialize plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.7)
ax.axis('off')
scat = ax.scatter([], [], s=100, c='white')

# Update function for animation
def update(frame):
    new_positions = update_positions(frame)
    scat.set_offsets(new_positions)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
