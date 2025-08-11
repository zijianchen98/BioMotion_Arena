
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 120
fps = 24
background_color = 'black'
light_color = 'white'
figsize = (8, 4)

# Initial positions of the lights (approximate, refined for lying down)
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.7],  # Left Shoulder
    [0.6, 0.7],  # Right Shoulder
    [0.3, 0.6],  # Left Elbow
    [0.7, 0.6],  # Right Elbow
    [0.2, 0.5],  # Left Wrist
    [0.8, 0.5],  # Right Wrist
    [0.5, 0.5],  # Torso
    [0.4, 0.4],  # Left Hip
    [0.6, 0.4],  # Right Hip
    [0.3, 0.3],  # Left Knee
    [0.7, 0.3],  # Right Knee
    [0.2, 0.2],  # Left Ankle
    [0.8, 0.2],  # Right Ankle
    [0.5, 0.9]   # Neck
])

# Generate smooth motion for each light
def generate_motion(path, frames):
    t = np.linspace(0, 1, frames)
    x = np.interp(t, [0, 0.25, 0.5, 0.75, 1], path[:, 0])
    y = np.interp(t, [0, 0.25, 0.5, 0.75, 1], path[:, 1])
    return np.column_stack((x, y))

# Define paths for each light to create a lying down motion
paths = [
    [(0.5, 0.8), (0.5, 0.6), (0.5, 0.6), (0.5, 0.6), (0.5, 0.8)],  # Head
    [(0.4, 0.7), (0.4, 0.6), (0.4, 0.6), (0.4, 0.6), (0.4, 0.7)],  # Left Shoulder
    [(0.6, 0.7), (0.6, 0.6), (0.6, 0.6), (0.6, 0.6), (0.6, 0.7)],  # Right Shoulder
    [(0.3, 0.6), (0.3, 0.5), (0.3, 0.5), (0.3, 0.5), (0.3, 0.6)],  # Left Elbow
    [(0.7, 0.6), (0.7, 0.5), (0.7, 0.5), (0.7, 0.5), (0.7, 0.6)],  # Right Elbow
    [(0.2, 0.5), (0.2, 0.4), (0.2, 0.4), (0.2, 0.4), (0.2, 0.5)],  # Left Wrist
    [(0.8, 0.5), (0.8, 0.4), (0.8, 0.4), (0.8, 0.4), (0.8, 0.5)],  # Right Wrist
    [(0.5, 0.5), (0.5, 0.4), (0.5, 0.4), (0.5, 0.4), (0.5, 0.5)],  # Torso
    [(0.4, 0.4), (0.4, 0.3), (0.4, 0.3), (0.4, 0.3), (0.4, 0.4)],  # Left Hip
    [(0.6, 0.4), (0.6, 0.3), (0.6, 0.3), (0.6, 0.3), (0.6, 0.4)],  # Right Hip
    [(0.3, 0.3), (0.3, 0.2), (0.3, 0.2), (0.3, 0.2), (0.3, 0.3)],  # Left Knee
    [(0.7, 0.3), (0.7, 0.2), (0.7, 0.2), (0.7, 0.2), (0.7, 0.3)],  # Right Knee
    [(0.2, 0.2), (0.2, 0.1), (0.2, 0.1), (0.2, 0.1), (0.2, 0.2)],  # Left Ankle
    [(0.8, 0.2), (0.8, 0.1), (0.8, 0.1), (0.8, 0.1), (0.8, 0.2)],  # Right Ankle
    [(0.5, 0.9), (0.5, 0.8), (0.5, 0.8), (0.5, 0.8), (0.5, 0.9)]   # Neck
]

# Generate motions
motions = [generate_motion(path, frames) for path in paths]

# Create plot
fig, ax = plt.subplots(figsize=figsize, facecolor=background_color)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, c=light_color)

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    positions = np.array([motion[i % frames] for motion in motions])
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, repeat=True, interval=1000/fps)
plt.show()
