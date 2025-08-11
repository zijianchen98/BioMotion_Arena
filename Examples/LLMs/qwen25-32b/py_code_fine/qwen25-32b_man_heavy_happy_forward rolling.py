
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
positions = np.array([
    [0.5, 0.4], [0.6, 0.4], [0.7, 0.4],  # Head
    [0.4, 0.5], [0.5, 0.5], [0.6, 0.5], [0.7, 0.5], [0.8, 0.5],  # Torso
    [0.3, 0.6], [0.9, 0.6],  # Arms
    [0.4, 0.7], [0.8, 0.7],  # Legs
])

# Define the trajectory function for forward rolling
def forward_roll(t):
    angle = t * np.pi / 180
    roll = np.sin(angle)
    return roll

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Update function for the animation
def update(frame):
    global positions
    roll_value = forward_roll(frame)
    
    # Update positions based on the forward roll motion
    for i in range(len(positions)):
        x, y = positions[i]
        if i < 3:  # Head
            positions[i] = [x + roll_value * 0.05, y - roll_value * 0.05]
        elif i < 8:  # Torso
            positions[i] = [x + roll_value * 0.05, y - roll_value * 0.05]
        elif i < 10:  # Arms
            positions[i] = [x + roll_value * 0.05, y - roll_value * 0.05]
        else:  # Legs
            positions[i] = [x + roll_value * 0.05, y - roll_value * 0.05]

    scat.set_offsets(positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 100), interval=50, repeat=True)

plt.show()
