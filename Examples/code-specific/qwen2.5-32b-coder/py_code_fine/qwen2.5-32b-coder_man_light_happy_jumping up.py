
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 3  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initial positions of the points (simplified happyman)
initial_positions = np.array([
    [0, 1],   # head
    [-0.5, 0.7], [-0.5, 0.5], [-0.5, 0.3],  # left arm
    [0.5, 0.7], [0.5, 0.5], [0.5, 0.3],     # right arm
    [-0.3, -0.1], [-0.3, -0.3],             # left leg
    [0.3, -0.1], [0.3, -0.3],               # right leg
    [-0.1, 0.1], [0.1, 0.1],                # shoulders
    [0, 0]                                 # torso
])

def jump_motion(t):
    """Define the jumping motion."""
    amplitude = 0.5
    frequency = 1 / DURATION
    phase_shift = np.pi / 2
    vertical = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    
    # Adjustments for limbs and torso
    positions = initial_positions.copy()
    positions[:, 1] += vertical
    
    # Simplistic limb adjustments for more natural motion
    if t < DURATION / 2:
        # Left leg goes down, right leg goes up
        positions[8, 1] -= 0.1 * np.sin(4 * np.pi * frequency * t)
        positions[9, 1] += 0.1 * np.sin(4 * np.pi * frequency * t)
        positions[10, 1] -= 0.1 * np.sin(4 * np.pi * frequency * t)
        positions[11, 1] += 0.1 * np.sin(4 * np.pi * frequency * t)
    else:
        # Right leg goes down, left leg goes up
        positions[8, 1] += 0.1 * np.sin(4 * np.pi * frequency * t)
        positions[9, 1] -= 0.1 * np.sin(4 * np.pi * frequency * t)
        positions[10, 1] += 0.1 * np.sin(4 * np.pi * frequency * t)
        positions[11, 1] -= 0.1 * np.sin(4 * np.pi * frequency * t)
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2)
ax.axis('off')
ax.set_aspect('equal')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, color='white')

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    t = i / FPS
    positions = jump_motion(t)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = FuncAnimation(fig, animate, frames=TOTAL_FRAMES, init_func=init, blit=True, interval=1000/FPS)

plt.show()
