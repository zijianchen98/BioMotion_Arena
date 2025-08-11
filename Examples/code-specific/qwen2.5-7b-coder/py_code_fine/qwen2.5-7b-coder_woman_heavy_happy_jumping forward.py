
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAMES = 60
FPS = 30
BACKGROUND_COLOR = 'black'
LIGHT_COLOR = 'white'

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor(BACKGROUND_COLOR)
ax.axis('off')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Initialize light positions
light_positions = np.random.rand(NUM_LIGHTS, 2) * 10 - 5

# Define the jumping motion
def jump_motion(t):
    amplitude = 1
    frequency = 2 * np.pi / FRAMES
    phase = t % FRAMES
    y_offset = amplitude * np.sin(frequency * phase)
    return y_offset

# Update function for animation
def update(frame):
    y_offsets = [jump_motion(frame + i) for i in range(NUM_LIGHTS)]
    light_positions[:, 1] += y_offsets
    
    # Wrap around if out of bounds
    light_positions[light_positions[:, 1] > 5, 1] -= 10
    light_positions[light_positions[:, 1] < -5, 1] += 10
    
    # Clear previous plot
    ax.clear()
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.axis('off')
    
    # Plot updated light positions
    ax.scatter(light_positions[:, 0], light_positions[:, 1], color=LIGHT_COLOR, s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(FRAMES), interval=1000/FPS, repeat=True)

plt.show()
