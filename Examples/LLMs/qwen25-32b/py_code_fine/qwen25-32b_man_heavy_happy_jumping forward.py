
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')  # Hide the axis

# Initial positions of the 15 points representing the jumping person
positions = np.array([
    [0, -8],   # Feet
    [-1, -6],  # Left leg
    [1, -6],   # Right leg
    [0, -4],   # Hips
    [-1, -2],  # Left hip
    [1, -2],   # Right hip
    [0, -1],   # Torso
    [-1, 0],   # Left arm
    [1, 0],    # Right arm
    [0, 2],    # Neck
    [0, 4],    # Head
    [-1, 6],   # Left hand
    [1, 6],    # Right hand
    [-1, 3],   # Left shoulder
    [1, 3]     # Right shoulder
])

# Create scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Function to update the frame
def update(num):
    global positions
    
    # Define the amplitude and frequency of the jump
    amp = 1.5
    freq = 0.05
    
    # Update the y-position of each point according to a sine wave
    for i in range(len(positions)):
        if i <= 5:  # Legs and hips
            positions[i, 1] = positions[i, 1] + amp * np.sin(freq * num)
        else:  # Upper body
            positions[i, 1] = positions[i, 1] + 2 * amp * np.sin(freq * num)
    
    # Update the x-position for forward movement
    positions[:, 0] += 0.05 * np.cos(freq * num)
    
    # Update the scatter plot
    scat.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

plt.show()
