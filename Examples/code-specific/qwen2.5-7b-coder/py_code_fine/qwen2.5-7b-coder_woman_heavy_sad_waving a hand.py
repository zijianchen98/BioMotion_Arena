
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 5  # seconds
TIME_STEP = 1 / FPS
TOTAL_FRAMES = int(DURATION * FPS)

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions and velocities of lights
positions = np.random.rand(NUM_LIGHTS, 2) * 2 - 1
velocities = np.random.randn(NUM_LIGHTS, 2) * 0.1

# Create scatter plot for light points
lights = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

def update(frame):
    global positions, velocities
    
    # Update positions based on velocities
    positions += velocities * TIME_STEP
    
    # Apply boundary conditions (wrap around)
    positions %= 2 - 1e-6
    
    # Update scatter plot data
    lights.set_offsets(positions)
    
    return lights,

# Create animation
animation = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

plt.show()
