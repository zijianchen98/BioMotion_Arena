
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
dt = 1 / fps

# Initial positions and velocities
np.random.seed(0)
positions = np.zeros((frames, num_lights, 2))
velocities = np.zeros_like(positions)

# Define the initial positions of the lights in a lying down position
initial_positions = np.array([
    [0.5, 0.7],  # Head
    [0.4, 0.6],  # Left Shoulder
    [0.6, 0.6],  # Right Shoulder
    [0.3, 0.5],  # Left Elbow
    [0.7, 0.5],  # Right Elbow
    [0.2, 0.4],  # Left Hand
    [0.8, 0.4],  # Right Hand
    [0.5, 0.4],  # Chest
    [0.4, 0.3],  # Left Hip
    [0.6, 0.3],  # Right Hip
    [0.3, 0.2],  # Left Knee
    [0.7, 0.2],  # Right Knee
    [0.2, 0.1],  # Left Foot
    [0.8, 0.1],  # Right Foot
    [0.5, 0.5]   # Belly
])

positions[0] = initial_positions

# Define a simple biomechanical model for lying down motion
def update_positions(frame):
    if frame < frames // 2:
        # Curling up
        positions[frame, 1:7] += np.array([0, -0.005 * np.sin(frame * dt * 10)])
        positions[frame, 9:13] += np.array([0, -0.005 * np.sin(frame * dt * 10)])
    else:
        # Lying still
        positions[frame] = positions[frames // 2]

# Update positions for each frame
for frame in range(1, frames):
    update_positions(frame)

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, c='white')

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    scat.set_offsets(positions[i])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
