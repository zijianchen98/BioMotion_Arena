
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights and frames
num_lights = 15
frames = 100

# Create figure and axis objects
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the lights
positions = np.zeros((num_lights, 2))

# Scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=10)

def init():
    scat.set_offsets(positions)
    return scat,

def update(frame):
    global positions
    
    # Jumping motion simulation
    t = frame / frames * 2 * np.pi
    amplitude = 0.4
    frequency = 1.0
    
    # Simplified jumping motion for the point-lights
    positions[:, 1] = amplitude * np.sin(frequency * t) - 0.5
    positions[:, 0] += (np.random.rand(num_lights) - 0.5) * 0.01
    
    # Update scatter plot with new positions
    scat.set_offsets(positions)
    
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

plt.show()
