
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
FPS = 30  # Frames per second
DURATION = 5  # Duration in seconds
TOTAL_FRAMES = FPS * DURATION
JUMP_HEIGHT = 0  # Adjust this value for the jump height
JUMP_DURATION = 1  # Duration of the jump in seconds

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [1, 1], [1, 2), (1, 3), (1, 4), (1, 5),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)
])

def update_light_positions(frame):
    global current_jump_time
    
    if frame < JUMP_DURATION * FPS:
        # Initial jumping phase
        t = frame / FPS
        y_offset = JUMP_HEIGHT * (1 - np.cos(t * np.pi / JUMP_DURATION))
        x_offset = 0  # Adjust horizontal offset for more natural motion
        
        new_positions = initial_positions + np.array([[x_offset, y_offset] for x, y in initial_positions])
    else:
        # Falling back down phase
        t = (frame - JUMP_DURATION * FPS) / FPS
        y_offset = JUMP_HEIGHT * (np.cos((t - 1) * np.pi / JUMP_DURATION) - 1)
        x_offset =  0  # Adjust horizontal offset for more natural motion
        
        new_positions = initial_positions + np.array([[x_offset, y_offset] for x, y in initial_positions])
    
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax ax.set_xlim(0, 6)
ax ax.set_ylim(1, 6)
ax ax.set_aspect('equal'
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot for the point-lights
scatter = ax.scatter(*initial_positions.T, color='white')

# Animate the point-lights
ani = FuncAnimation(fig, update_light_positions, frames=TOTAL_FRAMES, blit=True)

plt.show()
