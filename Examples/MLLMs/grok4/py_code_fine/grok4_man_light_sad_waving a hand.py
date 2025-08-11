
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide the axes

# Define the initial positions of the 15 point-lights
# Positioning in a rough form of a sad man's body waving hand
points = np.array([
    [0, 0.8],   # Head
    [-0.15, 0.6], # Left shoulder
    [0.15, 0.6],  # Right shoulder
    [-0.35, 0.4], # Left elbow
    [0.35, 0.4],  # Right elbow
    [-0.15, 0.2], # Left wrist
    [0.15, 0.2],  # Right wrist
    [-0.5, 0],    # Left hand
    [0.5, 0],     # Right hand
    [0, 0.4],     # Body center
    [0, 0.1],     # Belt line
    [-0.1, -0.3], # Left leg
    [0.1, -0.3],  # Right leg
    [-0.15, -0.5],# Left foot
    [0.15, -0.5], # Right foot
    [0, 0.5]      # Hand waving up
])

# Initialize the points in the plot
scat = ax.scatter(points[:,0], points[:,1], color='white')

# Function to update the positions for animation
def update(frame):
    # Update the y-position of the right wrist to simulate waving
    new_points = points.copy()
    waving_amplitude = 0.15 * np.sin(frame / 10.0)  # Adjust this value for bigger/smaller wave
    new_points[5, 1] += waving_amplitude   # Update right wrist position
    new_points[6, 1] += waving_amplitude   # Update right hand position
    scat.set_offsets(new_points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
