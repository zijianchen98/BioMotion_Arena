
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 200
fps = 24

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of lights for a standing person
initial_positions = np.array([
    [0, 0.8],  # Head
    [-0.1, 0.7], [0.1, 0.7],  # Eyes
    [0, 0.6],  # Nose
    [0, 0.5],  # Mouth
    [0, 0.4],  # Neck
    [0, 0.3],  # Shoulder
    [-0.2, 0.2], [0.2, 0.2],  # Elbows
    [-0.3, 0.1], [0.3, 0.1],  # Wrists
    [0, 0.2],  # Chest
    [0, 0.1],  # Waist
    [-0.1, 0], [0.1, 0],  # Hips
    [-0.2, -0.1], [0.2, -0.1]  # Knees
])

# Create scatter plot for lights
lights = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='white')

def update(frame):
    t = frame / frames * 2 * np.pi
    positions = initial_positions.copy()
    
    # Head bobbing slightly
    positions[0, 1] += 0.01 * np.sin(t)
    
    # Shoulders moving slightly
    positions[5, 0] += 0.02 * np.cos(t)
    
    # Arms swinging naturally
    positions[6:8, 0] += 0.05 * np.sin(t + np.pi / 2)
    positions[9:11, 0] += 0.05 * np.sin(t)
    
    # Chest moving up and down
    positions[11, 1] += 0.02 * np.sin(t)
    
    # Waist tilting slightly
    positions[12, 1] += 0.01 * np.sin(t + np.pi / 4)
    
    # Hips moving slightly
    positions[13, 0] += 0.02 * np.cos(t)
    positions[14, 0] -= 0.02 * np.cos(t)
    
    # Knees bending naturally
    positions[13, 1] -= 0.05 * np.sin(t)
    positions[14, 1] -= 0.05 * np.sin(t)
    
    # Transition to sitting position
    if frame > frames // 2:
        sit_factor = (frame - frames // 2) / (frames // 2)
        positions[5:, 1] -= 0.3 * sit_factor
        positions[13:, 0] *= 0.5 * (1 - sit_factor) + 0.5
        positions[13:, 1] += 0.3 * sit_factor
    
    lights.set_offsets(positions)
    return lights,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
