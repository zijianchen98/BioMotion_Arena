
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 4  # seconds
TIME = np.linspace(0, DURATION, int(FPS * DURATION))

# Initial positions of lights
initial_positions = np.random.rand(NUM_LIGHTS, 2) * 8 - 4  # Range from -4 to 4 on both axes

# Animation function
def update(frame):
    ax.clear()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_facecolor('black')
    
    # Update positions based on time
    x = initial_positions[:, 0] + np.sin(TIME[frame]) * 0.5
    y = initial_positions[:, 1] + np.cos(TIME[frame]) * 0.5
    
    # Plot lights
    ax.scatter(x, y, color='white', s=50)

# Create figure and axis
fig, ax = plt.subplots()

# Create animation
ani = FuncAnimation(fig, update, frames=len(TIME), interval=1000 / FPS)

# Show animation
plt.show()
