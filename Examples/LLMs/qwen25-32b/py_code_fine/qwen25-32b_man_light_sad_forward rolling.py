
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
FPS = 30
DURATION_SECONDS = 10
FRAMES = FPS * DURATION_SECONDS
POINT_LIGHTS = 15

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for better visualization

# Create scatter plot for point lights
scat = ax.scatter([], [], color='white', s=10)

# Generate initial positions
positions = np.random.rand(POINT_LIGHTS, 2)

# Define forward rolling motion
def update(frame):
    global positions
    time = frame / FPS
    for i in range(POINT_LIGHTS):
        # Simple sine wave motion for each point to simulate rolling
        positions[i, 0] = 0.5 + 0.4 * np.sin(time + i * 0.1)
        positions[i, 1] = 0.5 + 0.4 * np.cos(time + i * 0.2)
    
    # Update scatter plot data
    scat.set_offsets(positions)
    return scat,

# Animation function
ani = FuncAnimation(fig, update, frames=np.arange(FRAMES), interval=1000/FPS, blit=True)

plt.show()
