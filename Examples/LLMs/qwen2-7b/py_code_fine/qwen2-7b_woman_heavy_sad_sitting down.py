
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
LIGHT_SIZE = 10
FRAME_RATE = 60
DURATION_SECS = 5
ACTION_TIME = DURATION_SECS / FRAME_RATE

# Initial position of the points
initial_positions = np.random.uniform(-100, 100, (NUM_LIGHTS, 2)

# Function to update the positions of the lights
def update(frame):
    global initial_positions
    
    # Simulate motion by updating positions
    for i in range(NUM_LIGHTS):
        x, y = initial_positions[i]
        dx = np.sin(np.pi * frame / ACTION_TIME)
        dy = np.cos(np.pi * frame / ACTION_TIME)
        initial_positions[i] = (x + dx, y + dy
        
    # Update the scatter plot
    scatter.set_offsets(initial_positions)
    return scatter,

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for the lights
scatter = ax.scatter([], [], s=LIGHT_SIZE, c='white')

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(DURATION_SECS*FRAME_RATE),
         blit=True, interval=1000/FRAME_RATE)

# Show the animation
plt.show()
