
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 points for the walking man with a heavy weight
# These positions are simplified and should be adjusted for more realistic motion
points = [
    [0, 1], [0, 2], [0, 3],  # Head
    [-1, 0], [1, 0],         # Shoulders
    [-2, -1], [2, -1],       # Hips
    [-3, -2], [3, -2],       # Knees
    [-4, -3], [4, -3],       # Ankles
    [-1, -1], [1, -1],       # Elbows
    [-2, -2], [2, -2]        # Hands
]

# Convert to numpy array for easier manipulation
points = np.array(points)

# Function to update the position of the points for each frame
def update(frame):
    global points
    # Simulate walking by shifting the points horizontally
    shift = np.sin(frame / 10) * 0.5  # Sinusoidal motion for natural walking
    points[:, 0] += shift
    scatter.set_offsets(points)
    return scatter,

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
