
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the points
points = [
    [0, -4],  # Torso
    [-1, -3], [1, -3],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -1], [3, -1],  # Hands
    [0, 0],  # Head
    [0, -6],  # Hip
    [-1, -7], [1, -7],  # Knees
    [-2, -8], [2, -8],  # Ankles
    [-3, -9], [3, -9]   # Feet
]

# Convert to numpy array for easier manipulation
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the positions of the points
def update(frame):
    global points
    t = frame / 100  # Time parameter for the jump
    amplitude = 3  # Jump height
    frequency = 1  # Frequency of the jump
    
    # Update the y-coordinates of the points
    points[:, 1] += amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the scatter plot
    scat.set_offsets(points)
    
    # Reset the points after one full cycle
    if frame % 100 == 0:
        points[:, 1] -= amplitude * np.sin(2 * np.pi * frequency * t)
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 1000, 1), interval=50, blit=True)

# Show the animation
plt.show()
