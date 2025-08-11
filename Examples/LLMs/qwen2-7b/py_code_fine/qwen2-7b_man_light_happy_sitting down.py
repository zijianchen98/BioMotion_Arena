
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
NUM_LIGHTS = 15
DURATION = 10  # Duration in seconds
FPS = 30  # Frames per second

# Calculate frame duration
frame_duration = Duration / FPS

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim((-1, 1)
ax.set_ylim((-1, 1))
ax.set_aspect('equal')
ax.axis('off')

# Initialize positions of the lights
light_positions = np.random.uniform(-0.5, 0.8, size=(NUM_LIGHTS, 2))

def update(frame):
    global light_positions
    
    # Update each light's position based on the action
    for i, pos in enumerate(light_positions):
        if frame % 2 == 0:
            # Moving left to right
            light_positions[i] += 0.05 * (np.sign(pos[0])
        else:
            # Moving right to left
            light_positions[i] -= 0.01 * np.sign(pos[0])

    # Ensure the lights stay within the plot boundaries
    light_positions = np.clip(light_positions, -1, 1)

    # Clear the previous frame and draw the updated positions
    ax.clear()
    ax.scatter(*zip(*light_positions), color='white', s=50)
    ax.set_title('Happy Man Sitting Animation', fontsize=16)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange((0, DURATION * FPS), interval=1000/FPS, repeat=True)

# Display the animation
plt.show()
