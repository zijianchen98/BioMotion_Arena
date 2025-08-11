
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Define the initial positions of the point-lights representing a happy man waving
# The points based on a simple stick figure formation
points = np.array([
    [0, 0.6],   # Head
    [-0.2, 0.4],  # Left shoulder
    [0.2, 0.4],   # Right shoulder
    [-0.2, 0.2],  # Left elbow
    [0.2, 0.2],   # Right elbow
    [-0.2, 0],    # Left hand
    [0.2, 0],     # Right hand
    [0, -0.5],    # Body
    [-0.1, -1],   # Left leg
    [0.1, -1],    # Right leg
])

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

# Function to update positions for animation
def update(frame):
    global points
    # Waving motion parameters
    wave_amplitude = 0.1
    wave_frequency = 0.1

    # Update the position of the hands in a waving motion
    points[5, 1] = np.sin(frame * wave_frequency) * wave_amplitude - 0.2  # Left hand
    points[6, 1] = np.sin(frame * wave_frequency) * wave_amplitude + 0.2  # Right hand

    # Update scatter
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

plt.axis('off')  # Hide the axis
plt.show()
