
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Define the positions of the lights for a running figure
def get_light_positions(t):
    positions = []
    
    # Torso and head
    positions.append((np.sin(t), 1.5))  # Head
    positions.append((np.sin(t), 1.0))  # Chest
    positions.append((np.sin(t), 0.5))  # Waist
    
    # Arms
    positions.append((np.sin(t) + 0.7 * np.cos(2 * t), 1.2))  # Right shoulder
    positions.append((np.sin(t) + 0.7 * np.cos(2 * t), 0.8))  # Right elbow
    positions.append((np.sin(t) + 0.7 * np.cos(2 * t), 0.4))  # Right hand
    positions.append((np.sin(t) - 0.7 * np.cos(2 * t), 1.2))  # Left shoulder
    positions.append((np.sin(t) - 0.7 * np.cos(2 * t), 0.8))  # Left elbow
    positions.append((np.sin(t) - 0.7 * np.cos(2 * t), 0.4))  # Left hand
    
    # Legs
    positions.append((np.sin(t) + 0.6 * np.cos(3 * t), 0.2))  # Right hip
    positions.append((np.sin(t) + 0.6 * np.cos(3 * t) - 0.4, -0.3))  # Right knee
    positions.append((np.sin(t) + 0.6 * np.cos(3 * t) - 0.8, -0.8))  # Right foot
    positions.append((np.sin(t) - 0.6 * np.cos(3 * t), 0.2))  # Left hip
    positions.append((np.sin(t) - 0.6 * np.cos(3 * t) + 0.4, -0.3))  # Left knee
    positions.append((np.sin(t) - 0.6 * np.cos(3 * t) + 0.8, -0.8))  # Left foot
    
    return np.array(positions)

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.axis('off')

points, = ax.plot([], [], 'wo', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    t = i / fps
    positions = get_light_positions(t)
    x, y = zip(*positions)
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
