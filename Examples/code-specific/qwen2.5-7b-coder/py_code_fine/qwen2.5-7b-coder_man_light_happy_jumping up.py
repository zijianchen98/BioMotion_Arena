
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 4  # seconds
TIME_INTERVAL = 1 / FPS

# Initialize positions
positions = np.zeros((NUM_LIGHTS, 2))
velocities = np.random.randn(NUM_LIGHTS, 2)
accelerations = np.zeros((NUM_LIGHTS, 2))

# Define the acceleration function based on the jumping motion
def update_acceleration(positions):
    center_position = np.mean(positions, axis=0)
    distances = positions - center_position
    magnitudes = np.linalg.norm(distances, axis=1)
    accelerations = np.where(magnitudes > 0, -distances / magnitudes**3, 0)
    return accelerations

# Update function for the animation
def update(frame):
    global positions, velocities, accelerations
    
    accelerations = update_acceleration(positions)
    velocities += accelerations * TIME_INTERVAL
    positions += velocities * TIME_INTERVAL
    
    # Keep points within bounds
    positions[:, 0] = np.clip(positions[:, 0], 0, 8)
    positions[:, 1] = np.clip(positions[:, 1], 0, 6)
    
    scatter.set_offsets(positions)
    return scatter,

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize scatter plot
scatter = ax.scatter([], [], s=50, color='white')

# Create animation
ani = FuncAnimation(fig, update, frames=int(FPS * DURATION), interval=TIME_INTERVAL * 1000, blit=True)

plt.show()
