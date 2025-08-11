
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the coordinates of the lights representing the runner
def get_coordinates(t):
    # Simplified model of running motion
    x = [0, -1, 1, -1, 1, -1.5, 1.5, -1.5, 1.5, -1, 1, -1, 1, -2, 2]
    y = [0, 1, 1, 2, 2, 0, 0, -1, -1, -2, -2, -3, -3, -1.5, -1.5]
    
    # Apply periodic vertical movement to simulate running
    amplitude = 0.5
    frequency = 2
    phase_shift = np.pi / 2
    
    y = [yi + amplitude * np.sin(frequency * t + phase_shift) for yi in y]
    
    return list(zip(x, y))

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 3)
ax.axis('off')  # Hide the axes

# Create scatter plot for the lights
scatter = ax.scatter([], [], color='white')

# Update function for animation
def update(frame):
    coords = get_coordinates(frame)
    scatter.set_offsets(coords)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100), interval=50, blit=False)

plt.show()
