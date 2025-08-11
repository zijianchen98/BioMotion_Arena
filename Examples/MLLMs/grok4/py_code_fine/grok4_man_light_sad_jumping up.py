
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
FPS = 30         # Frames per second
NUM_POINTS = 15  # Number of point-lights
JUMP_HEIGHT = 2  # Max jump height
DURATION = 2     # Duration of animation in seconds

# Generate point-light positions
def get_positions(frame, jump_height):
    t = frame / (FPS * DURATION)  # Normalized time [0, 1]
    if t < 0.5:  # Going up
        height = jump_height * (1 - np.cos(np.pi * t * 2)) / 2
    else:  # Coming down
        height = jump_height * (1 + np.cos(np.pi * (t - 0.5) * 2)) / 2
    
    # Vertical spacing
    vertical_spacing = height / 3
    positions = np.array([(0, height - vertical_spacing * i) for i in range(NUM_POINTS)])
    return positions

# Initialization function
def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, JUMP_HEIGHT + 1)
    return scatter,

# Update function for animation
def update(frame):
    positions = get_positions(frame, JUMP_HEIGHT)
    scatter.set_offsets(positions)
    return scatter,

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
scatter = ax.scatter([], [], c='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=FPS * DURATION, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
