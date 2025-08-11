
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axes

# Number of point-lights
num_lights = 15

# Initial positions of the point-lights
positions = np.random.rand(num_lights, 2) * 10

# Function to update the positions of the lights in each frame
def update(frame):
    global positions
    
    # Forward rolling motion can be simulated by updating positions based on a sine wave for vertical motion and linear motion for horizontal motion.
    t = frame / 40.0  # Time variable
    positions[:, 0] += 0.05  # Linear horizontal motion
    
    # Vertical motion using sine wave to simulate forward rolling
    positions[:, 1] = 5 + 1.5 * np.sin(t + positions[:, 0])
    
    # Reset the position if it goes off-screen
    off_screen = positions[:, 0] > 10
    positions[off_screen] = [np.random.rand() * 2, 5]
    
    # Update the scatter plot data
    scat.set_offsets(positions)

# Scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=20)

plt.show()
