
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a heavy man running
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [1, -1],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -3], [3, -3],  # Hands
    [0, -2],  # Waist
    [-1, -3], [1, -3],  # Knees
    [-2, -4], [2, -4],  # Ankles
    [-3, -5], [3, -5]   # Feet
])

# Function to update the positions of the points for each frame
def update(frame):
    global initial_positions
    positions = initial_positions.copy()
    
    # Apply a sinusoidal motion to simulate running
    phase = frame / 10.0
    amplitude = 0.5
    
    # Update head position
    positions[0, 0] += amplitude * np.sin(phase)
    
    # Update shoulders position
    positions[1:3, 0] += amplitude * np.sin(phase + np.pi/2)
    
    # Update elbows position
    positions[3:5, 0] += amplitude * np.sin(phase + np.pi)
    
    # Update hands position
    positions[5:7, 0] += amplitude * np.sin(phase + 3*np.pi/2)
    
    # Update waist position
    positions[7, 0] += amplitude * np.sin(phase)
    
    # Update knees position
    positions[8:10, 0] += amplitude * np.sin(phase + np.pi/2)
    
    # Update ankles position
    positions[10:12, 0] += amplitude * np.sin(phase + np.pi)
    
    # Update feet position
    positions[12:14, 0] += amplitude * np.sin(phase + 3*np.pi/2)
    
    # Clear the previous frame
    ax.cla()
    
    # Plot the updated positions
    ax.scatter(positions[:, 0], positions[:, 1], color='white')
    
    # Set the plot limits and background color
    ax.set_xlim(-5, 5)
    ax.set_ylim(-6, 1)
    ax.set_facecolor('black')
    ax.axis('off')

# Create a figure and axis with a black background
fig, ax = plt.subplots(facecolor='black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Display the animation
plt.show()
