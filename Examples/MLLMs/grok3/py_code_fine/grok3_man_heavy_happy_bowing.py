
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights (simplified human figure bowing)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
t = np.linspace(0, 2*np.pi, 100)  # Time steps for smooth motion
initial_positions = np.array([
    [0, 1.5],  # head
    [-0.5, 1.2], [0.5, 1.2],  # shoulders
    [-0.7, 0.8], [0.7, 0.8],  # elbows
    [-0.9, 0.4], [0.9, 0.4],  # wrists
    [0, 0.8],  # torso
    [-0.2, 0.4], [0.2, 0.4],  # hips
    [-0.3, 0], [0.3, 0],  # knees
    [-0.4, -0.4], [0.4, -0.4]  # ankles
])

# Parameters for bowing motion
amplitude = 0.5  # Bowing depth
frequency = 0.5  # Bowing speed

# Function to update positions for each frame
def update(frame):
    angle = amplitude * np.sin(frequency * t[frame])  # Bowing motion
    positions = initial_positions.copy()
    
    # Apply bowing motion: lower torso and limbs
    positions[0, 1] -= angle  # head
    positions[1:3, 1] -= angle * 0.8  # shoulders
    positions[3:5, 1] -= angle * 0.6  # elbows
    positions[5:7, 1] -= angle * 0.4  # wrists
    positions[7, 1] -= angle * 0.9  # torso
    positions[8:10, 1] -= angle * 0.7  # hips
    positions[10:12, 1] -= angle * 0.5  # knees
    positions[12:, 1] -= angle * 0.3  # ankles
    
    # Update scatter points
    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2)
ax.axis('off')

# Create scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

# Display animation
plt.show()
