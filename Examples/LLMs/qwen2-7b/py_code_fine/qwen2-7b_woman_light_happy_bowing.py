
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 60
DURATION = 5 # in seconds
POINT_SIZE = 5

# Define the subject and action
ACTION = "bowing"
SUBJECT = "happy woman with light weight"

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim((-8, 8))
ax.set_ylim((-8, 8))
ax.set_aspect('equal')
ax.axis('off')

# Generate random initial positions for the points
points = np.random.uniform(low=-4, high=4, size=(NUM_POINTS, 2))

# Create the animation function
def animate(i):
    global points
    
    # Update each point's position based on the action (bowing
    for j in range(NUM_POINTS):
        x, y = points[j]
        if ACTION == "bowing":
            # Simple bowing motion example
            angle = i * 2 * np.pi / FPS
            points[j] = (x + 4 * np.cos(angle), y + 4 * np.sin(angle)
    
    # Clear previous points
    ax.clear()
    # Plot the updated points
    ax.scatter(*zip(*points), c='white', s=POINT_SIZE)
    # Set background color to black
    ax.set_facecolor('black')

# Create the animation
ani = FuncAnimation(fig, animate, frames=DURATION * FPS, interval=1000/FPS)

# Show the animation
plt.show()

print("Animation completed successfully.")
