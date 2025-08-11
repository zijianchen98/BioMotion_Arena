
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a sitting sadman
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [0, -1], [1, -1],  # Shoulders
    [-2, -2], [0, -2], [2, -2],  # Elbows
    [-3, -3], [0, -3], [3, -3],  # Hands
    [0, -4],  # Waist
    [-1, -5], [0, -5], [1, -5],  # Knees
    [-2, -6], [0, -6], [2, -6]   # Feet
])

# Function to update the positions of the points for each frame
def update(frame):
    global initial_positions
    positions = initial_positions.copy()
    
    # Apply a simple harmonic motion to simulate sitting down
    amplitude = 0.5
    frequency = 0.1
    time = frame / 10.0
    
    # Update y-coordinates based on the harmonic motion
    positions[:, 1] += amplitude * np.sin(frequency * time)
    
    # Clear the previous frame and plot the new positions
    ax.clear()
    ax.scatter(positions[:, 0], positions[:, 1], color='white')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-10, 1)
    ax.set_facecolor('black')

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
