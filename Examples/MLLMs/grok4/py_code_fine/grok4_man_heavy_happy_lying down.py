
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up parameters for the animation
num_points = 15  # Total number of point-lights
duration = 2000  # Duration of the animation in milliseconds
fps = 30  # Frames per second
frames = int(duration / 1000 * fps)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Create points for the "happy man lying down"
# Coordinates for 15 points (simplified body position)
init_positions = np.array([
    [0, 0.5],   # Head
    [-0.2, 0.4],  # Left shoulder
    [0.2, 0.4],   # Right shoulder
    [-0.2, 0],    # Left elbow
    [0.2, 0],     # Right elbow
    [-0.5, -0.6], # Left hand
    [0.5, -0.6],  # Right hand
    [-0.4, -0.8], # Left hip
    [0.4, -0.8],  # Right hip
    [-0.4, -1.2], # Left knee
    [0.4, -1.2],  # Right knee
    [-0.5, -1.4], # Left foot
    [0.5, -1.4],  # Right foot
    [0.0, -0.5],  # Center of body 
    [0.0, -0.2],  # Mid-center (optional)
    [0.05, 0]     # Extra point for motion
])

# Initialize plot with points
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    t = frame / frames * np.pi * 4  # Normalize frame to a range for smooth oscillation
    # Example transformation to create motion: vertical oscillation
    new_positions = init_positions.copy()
    new_positions[:, 1] += 0.1 * np.sin(t + np.linspace(0, 2 * np.pi, num_points))
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
