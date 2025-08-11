
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = int(fps * duration)

# Initialize positions and velocities
np.random.seed(42)
positions = np.zeros((frames, num_lights, 2))
velocities = np.zeros_like(positions)

# Define the trajectory for bowing
def bowing_trajectory(t):
    # t ranges from 0 to 1
    # Bowing motion: start upright, bend forward, then return to upright
    x = np.linspace(-0.2, 0.2, frames)  # Horizontal sway
    y = 0.5 - 0.3 * np.sin(2 * np.pi * t)  # Vertical bowing
    return x, y

# Initial positions of the point lights
initial_positions = np.array([
    [-0.1, 0.9], [-0.05, 0.8], [0, 0.7], [0.05, 0.8], [0.1, 0.9],  # Head and shoulders
    [-0.1, 0.6], [-0.05, 0.5], [0, 0.4], [0.05, 0.5], [0.1, 0.6],  # Upper arms
    [-0.1, 0.3], [-0.05, 0.2], [0, 0.1], [0.05, 0.2], [0.1, 0.3]   # Lower arms and hands
])

# Generate the trajectory for each light
for i in range(num_lights):
    x_bow, y_bow = bowing_trajectory(np.linspace(0, 1, frames))
    positions[:, i, 0] = initial_positions[i, 0] + x_bow
    positions[:, i, 1] = initial_positions[i, 1] + y_bow

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, c='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
