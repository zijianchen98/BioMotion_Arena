
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 120
fps = 30

# Initialize positions
positions = np.zeros((num_lights, frames, 2))

# Define key points for a jumping forward motion
# These coordinates are simplified and may need refinement for realism
# Head, shoulders, elbows, hands, hips, knees, feet
key_points = [
    [0.5, 0.8],  # Head
    [0.4, 0.7],  # Left shoulder
    [0.6, 0.7],  # Right shoulder
    [0.3, 0.6],  # Left elbow
    [0.7, 0.6],  # Right elbow
    [0.2, 0.5],  # Left hand
    [0.8, 0.5],  # Right hand
    [0.5, 0.4],  # Hips
    [0.4, 0.3],  # Left knee
    [0.6, 0.3],  # Right knee
    [0.3, 0.2],  # Left foot
    [0.7, 0.2],  # Right foot
    [0.5, 0.9],  # Additional point for balance
    [0.4, 0.8],  # Additional point for balance
    [0.6, 0.8]   # Additional point for balance
]

# Create a smooth trajectory for each point
for i in range(num_lights):
    x = np.linspace(key_points[i][0], key_points[i][0], frames)
    y = np.linspace(key_points[i][1], key_points[i][1], frames)
    
    # Simulate jumping forward
    if i in [0, 1, 2, 8, 9]:  # Head, shoulders, knees
        y += 0.1 * np.sin(np.linspace(0, 2 * np.pi, frames))
        x += 0.05 * np.cos(np.linspace(0, 2 * np.pi, frames))
    elif i in [3, 4, 10, 11]:  # Elbows, hands, feet
        y += 0.05 * np.sin(np.linspace(0, 2 * np.pi, frames))
        x += 0.025 * np.cos(np.linspace(0, 2 * np.pi, frames))
    else:  # Hips, additional points
        y += 0.15 * np.sin(np.linspace(0, 2 * np.pi, frames))
        x += 0.1 * np.cos(np.linspace(0, 2 * np.pi, frames))
    
    positions[i, :, 0] = x
    positions[i, :, 1] = y

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, c='white')

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    offsets = positions[:, i]
    scat.set_offsets(offsets)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, repeat=True, interval=1000/fps)

plt.show()
