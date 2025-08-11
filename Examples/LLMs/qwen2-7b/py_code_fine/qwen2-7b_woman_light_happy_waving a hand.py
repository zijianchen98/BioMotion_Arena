
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FRAME_RATE = 30
ACTION_DURATION = 5 # seconds
WAVE_AMPLITUDE = 0.2
WAVE_FREQUENCY = 1.5
WAVE_OFFSET = 0.5
BACKGROUND_COLOR = 'black'
LIGHT_COLOR = 'white'

# Define the wave function for hand waving
def wave_function(t):
    t = 2 * np.pi * WAVE_FREQUENCY * (t + WAVE_OFFSET
    return np.sin(np.abs(np.sin((t))) * WAVE_AMPLITUDE

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim((-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Generate initial positions for the lights
light_positions = np.random.uniform(-0.5, 0.5, size=(NUM_LIGHTS, 2))

# Function to update the position of each light during animation
def update_light_positions(i):
    global light_positions
    
    t = i / FRAME_RATE * ACTION_DURATION
    light_positions = np.roll(light_positions, 1, axis= 0)
    light_positions[0] = [wave_function(t), 0]
    
    return light_positions

# Create the animation
ani = animation.FuncAnimation(fig, update_light_positions, frames=np.arange((0, int(FRAME_RATE * ACTION_DURATION)), blit=True, interval=1000 / FRAME_RATE)

# Display the animation
plt.show()

