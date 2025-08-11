
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
DURATION = 60  # Duration of the animation in seconds
FPS = 30  # Frames per second

# Generate random initial positions for the points
positions = np.random.uniform(-5/2, width/2, size=(NUM_POINTS, 2))

def update(frame):
    global positions
    
    # Calculate new positions based on forward rolling motion
    for i in range(NUM_POINTS):
        # Update position based on speed and time step
        speed = 0.1 + 0.5 * np.sin(frame / FPS
        positions[i] += speed * np.sin(frame / FPS) * np.array([-np.sin(np.pi / 4), np.cos(np.pi / 4)])
        
        # Wrap around the screen if the point goes off the edge
        positions[i] %= width
        
        # Limit the position to the screen boundaries
        positions[i] = np.clip(positions[i], 0, width)
    
    ax.clear()
    ax.set_facecolor('k')
    ax.scatter(*positions.T, color='w', s=100)
    ax.axis('off')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
width = 8
ax.set_xlim(0, width
ax.set_ylim(0, width

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, DURATION * FPS, interval=1000 / FPS)

plt.show()

