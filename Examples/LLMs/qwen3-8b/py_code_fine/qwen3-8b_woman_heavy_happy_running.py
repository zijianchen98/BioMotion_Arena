
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

# Define the number of point lights and the action
NUM_LIGHTS = 15
ACTION = 'running'
BACKGROUND_COLOR = 'black'
LIGHT_COLOR = 'white'

# Define a biomechanically plausible motion for a running woman with a heavy weight
# This is a simplified model of body parts and their motion
body_parts = {
    'hips': {'position': np.array([0, 0]), 'amplitude': 0.3, 'frequency': 0.5, 'phase': 0.0},
    'knees': {'position': np.array([0, 0.5]), 'amplitude': 0.2, 'frequency': 0.5, 'phase': 0.3},
    'ankles': {'position': np.array([0, 1.0]), 'amplitude': 0.15, 'frequency': 0.5, 'phase': 0.6},
    'shoulders': {'position': np.array([0, 0.5]), 'amplitude': 0.3, 'frequency': 0.5, 'phase': 0.0},
    'elbows': {'position': np.array([0, 1.0]), 'amplitude': 0.2, 'frequency': 0.5, 'phase': 0.3},
    'wrists': {'position': np.array([0, 1.5]), 'amplitude': 0.15, 'frequency': 0.5, 'phase': 0.6},
    'head': {'position': np.array([0, 1.5]), 'amplitude': 0.2, 'frequency': 0.5, 'phase': 0.0},
    'weight': {'position': np.array([0, 0.2]), 'amplitude': 0.1, 'frequency': 0.5, 'phase': 0.0}
}

# Define a function to generate the positions of the point lights based on body parts
def generate_positions(t):
    positions = []
    for part in body_parts.values():
        x = part['position'][0] + part['amplitude'] * np.sin(2 * np.pi * part['frequency'] * t + part['phase'])
        y = part['position'][1] + part['amplitude'] * np.sin(2 * np.pi * part['frequency'] * t + part['phase'])
        positions.append((x, y))
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
lights = [Circle((0, 0), 0.05, color=LIGHT_COLOR) for _ in range(NUM_LIGHTS)]
light_collection = PatchCollection(lights, match_original=True)
ax.add_collection(light_collection)

# Animation function
def animate(t):
    positions = generate_positions(t)
    light_collection.set_offsets(np.array(positions))
    return light_collection,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
