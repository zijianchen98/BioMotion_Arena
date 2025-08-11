
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the points representing the happy man
points = [
    [5, 2],  # Head
    [4, 3],  [6, 3],  # Shoulders
    [3.5, 4], [6.5, 4],  # Elbows
    [3, 5], [7, 5],  # Hands
    [4.5, 3], [5.5, 3],  # Waist
    [4, 4], [6, 4],  # Hips
    [3.5, 5], [6.5, 5],  # Knees
    [3, 6], [7, 6]  # Feet
]

# Convert points to a numpy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the position of the points
def update(frame):
    global points
    t = frame / 100.0  # Time parameter for the jump
    amplitude = 1.0  # Jump height
    frequency = 1.0  # Frequency of the jump
    
    # Update the y-coordinates to simulate jumping
    points[:, 1] += amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the x-coordinates to simulate forward movement
    points[:, 0] += 0.01 * t
    
    # Reset positions if the man has moved too far to the right
    if points[0, 0] > 10:
        points[:, 0] -= 10
        points[:, 1] -= amplitude * np.sin(2 * np.pi * frequency * t)
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(300), interval=20, blit=True)

# Show the animation
plt.show()
