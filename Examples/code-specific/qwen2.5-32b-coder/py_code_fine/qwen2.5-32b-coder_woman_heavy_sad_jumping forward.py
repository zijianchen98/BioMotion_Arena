
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 200
fps = 24

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions of the lights (simplified model of a person)
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [-0.1, 0.6], # Left shoulder
    [0.1, 0.6],  # Right shoulder
    [-0.2, 0.4], # Left elbow
    [0.2, 0.4],  # Right elbow
    [-0.3, 0.2], # Left wrist
    [0.3, 0.2],  # Right wrist
    [0.0, 0.4],  # Spine
    [0.0, 0.2],  # Hip
    [-0.1, 0.0], # Left knee
    [0.1, 0.0],  # Right knee
    [-0.15, -0.2], # Left ankle
    [0.15, -0.2], # Right ankle
    [0.0, -0.4], # Waist
    [0.0, -0.6]  # Feet
])

# Create scatter plot for the lights
lights, = ax.plot([], [], 'o', markersize=10, color='white')

def init():
    lights.set_data([], [])
    return lights,

def animate(i):
    t = i / frames * 2 * np.pi
    
    # Jumping motion parameters
    jump_height = 0.1
    jump_width = 0.05
    phase_shift = np.pi / 2
    
    # Update positions based on jumping motion
    positions = initial_positions.copy()
    
    # Legs motion
    positions[9:, 1] += jump_height * np.sin(t + phase_shift)
    positions[9:, 0] += jump_width * np.sin(2 * t)
    
    # Arms motion
    positions[2:5, 1] -= 0.05 * np.sin(t)
    positions[5:, 1] -= 0.1 * np.sin(t + phase_shift)
    
    # Body motion
    positions[:, 1] += 0.05 * np.sin(t)
    
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)
plt.show()
