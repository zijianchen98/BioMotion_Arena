
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frame_rate = 30
total_frames = 360  # 12 seconds of animation at 30 FPS
background_color = 'black'
light_color = 'white'
fig_size = (8, 8)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=fig_size, facecolor=background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions for the lights (approximate)
initial_positions = np.array([
    [0.0, 0.7],  # Head
    [-0.1, 0.6], # Left eye
    [0.1, 0.6],  # Right eye
    [0.0, 0.4],  # Nose
    [0.0, 0.3],  # Chin
    [-0.3, 0.3], # Left shoulder
    [-0.5, 0.1], # Left elbow
    [-0.6, -0.1],# Left wrist
    [-0.5, -0.4],# Left hand
    [0.3, 0.3],  # Right shoulder
    [0.5, 0.1],  # Right elbow
    [0.6, -0.1], # Right wrist
    [0.5, -0.4], # Right hand
    [0.0, -0.5], # Hip
    [0.0, -0.8]  # Foot
])

# Scatter plot for the lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=light_color)

def update(frame):
    # Calculate new positions based on frame number
    positions = initial_positions.copy()
    
    # Waving hand motion
    t = frame / frame_rate
    wave_amplitude = 0.2
    wave_frequency = 1.0
    
    # Left hand waving
    positions[12, 1] = initial_positions[12, 1] + wave_amplitude * np.sin(2 * np.pi * wave_frequency * t)
    
    # Right hand waving
    positions[14, 1] = initial_positions[14, 1] + wave_amplitude * np.sin(2 * np.pi * wave_frequency * (t + 0.5))
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=total_frames, blit=True, interval=1000/frame_rate)
plt.show()
