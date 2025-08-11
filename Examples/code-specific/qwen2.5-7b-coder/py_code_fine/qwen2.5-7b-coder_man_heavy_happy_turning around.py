
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 5  # seconds

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize light positions
light_positions = np.random.rand(NUM_LIGHTS, 2) * 2 - 1

# Function to update the animation
def update(frame):
    # Clear the current frame
    ax.clear()
    
    # Update light positions based on happyman turning around
    angle = frame / FPS * 2 * np.pi
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    light_positions = np.dot(light_positions, rotation_matrix.T)
    
    # Plot the lights
    ax.scatter(light_positions[:, 0], light_positions[:, 1], color='white', s=50)
    
    # Set the background to black
    ax.set_facecolor('black')

# Create the animation
ani = FuncAnimation(fig, update, frames=int(FPS * DURATION), interval=1000/FPS)

# Show the animation
plt.show()
