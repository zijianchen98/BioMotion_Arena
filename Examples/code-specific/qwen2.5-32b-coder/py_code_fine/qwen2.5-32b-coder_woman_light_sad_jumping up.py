
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
bg_color = 'black'
point_color = 'white'

# Initial positions and velocities
positions = np.zeros((num_lights, 2))
velocities = np.zeros((num_lights, 2))

# Define joint indices for connections
connections = [
    (0, 1), (1, 2), (2, 3),  # Head and neck
    (0, 4), (4, 5), (5, 6), (6, 7),  # Right arm
    (0, 8), (8, 9), (9, 10), (10, 11),  # Left arm
    (0, 12), (12, 13), (13, 14), (14, 15),  # Spine and legs
]

# Create scatter plot for points
points, = ax.plot([], [], 'o', color=point_color, markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    global positions, velocities
    
    # Simple harmonic motion for jumping effect
    t = frame / fps
    jump_height = 0.2 * np.sin(2 * np.pi * 0.5 * t)  # Jump every second
    
    # Update positions
    positions[0] = [0, 0.2 + jump_height]  # Head position with jump
    positions[1] = [0, 0.1 + jump_height]  # Neck
    positions[2] = [0, 0 + jump_height]    # Shoulders
    positions[3] = [0, -0.1 + jump_height]   # Hips
    
    # Arms swinging
    arm_angle = 0.5 * np.sin(2 * np.pi * t)
    positions[4] = [-0.1, 0.1 + jump_height]  # Right shoulder
    positions[5] = [-0.2, 0.2 + 0.2 * arm_angle + jump_height]  # Right elbow
    positions[6] = [-0.3, 0.1 + 0.2 * arm_angle + jump_height]  # Right wrist
    positions[7] = [-0.4, 0.0 + 0.2 * arm_angle + jump_height]  # Right hand
    
    positions[8] = [0.1, 0.1 + jump_height]  # Left shoulder
    positions[9] = [0.2, 0.2 - 0.2 * arm_angle + jump_height]  # Left elbow
    positions[10] = [0.3, 0.1 - 0.2 * arm_angle + jump_height]  # Left wrist
    positions[11] = [0.4, 0.0 - 0.2 * arm_angle + jump_height]  # Left hand
    
    # Legs moving
    leg_angle = 0.5 * np.sin(2 * np.pi * (t + 0.25))
    positions[12] = [-0.1, -0.1 + jump_height]  # Right hip
    positions[13] = [-0.2, -0.3 + 0.2 * leg_angle + jump_height]  # Right knee
    positions[14] = [-0.3, -0.5 + 0.2 * leg_angle + jump_height]  # Right foot
    
    positions[12] = [0.1, -0.1 + jump_height]  # Left hip
    positions[13] = [0.2, -0.3 - 0.2 * leg_angle + jump_height]  # Left knee
    positions[14] = [0.3, -0.5 - 0.2 * leg_angle + jump_height]  # Left foot
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)
plt.show()
