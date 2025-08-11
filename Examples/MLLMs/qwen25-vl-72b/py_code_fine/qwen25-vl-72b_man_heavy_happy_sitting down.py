
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a heavy man sitting down
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [1, -1],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -3], [3, -3],  # Hands
    [0, -2],  # Torso
    [-1, -4], [1, -4],  # Hips
    [-2, -6], [2, -6],  # Knees
    [-3, -8], [3, -8]   # Feet
])

# Function to update the positions of the points for each frame
def update(frame):
    global initial_positions
    # Apply a simple harmonic motion to simulate sitting down
    amplitude = 0.5
    frequency = 0.1
    phase_shift = np.pi / 2
    
    new_positions = initial_positions.copy()
    new_positions[:, 1] += amplitude * np.sin(frequency * frame + phase_shift)
    
    # Update the scatter plot data
    scat.set_offsets(new_positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 1)
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
