
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Initial positions of the point-lights
positions = np.array([
    [4.5, 5], [5.5, 5],  # Shoulders
    [4, 6], [6, 6],      # Hips
    [3, 7], [7, 7],      # Hands
    [3.5, 8], [6.5, 8],  # Elbows
    [4, 9], [6, 9],      # Head
    [3, 4], [7, 4],      # Knees
    [3.5, 3], [6.5, 3],  # Ankles
    [3, 2], [7, 2]       # Feet
])

# Create scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

def update(frame):
    global positions
    
    # Adjust positions based on frame for jumping motion
    t = frame / 50.0  # Normalize frame number to time in seconds
    amplitude = 0.5 * np.sin(t * 2 * np.pi)  # Vertical displacement
    
    # Apply amplitude to certain body parts to simulate jumping
    positions[0:2, 1] += amplitude  # Shoulders
    positions[2:4, 1] += amplitude  # Hips
    positions[4:6, 1] += amplitude  # Hands
    positions[6:8, 1] += amplitude  # Elbows
    positions[8:10, 1] += amplitude  # Head
    positions[10:12, 1] += amplitude  # Knees
    positions[12:14, 1] += amplitude  # Ankles
    positions[14:16, 1] += amplitude  # Feet
    
    # Update scatter plot data
    scat.set_offsets(positions)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, repeat=True)

plt.show()
