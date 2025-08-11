
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis.
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.axis('off')  # Hide the axes for cleaner visualization.

# Number of points representing the point-light display.
num_points = 15

# Initial positions for the points. These positions are arbitrary and can be adjusted for better representation.
positions = np.random.rand(num_points, 2)

# Scatter plot for the point-lights.
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Function to update the positions of the points in each frame.
def update(frame):
    global positions
    
    # Define the motion pattern for the waving hand.
    # This is a simplified example and may need adjustments for realism.
    if frame < 100:
        positions[0] += np.array([np.sin(frame / 10.) * 0.01, np.cos(frame / 10.) * 0.01])  # Waving hand motion.
        positions[1:] += np.random.normal(scale=0.005, size=(num_points-1, 2))  # Slight jitter for other body parts.
    
    # Update the scatter plot data.
    scat.set_offsets(positions)
    return scat,

# Create the animation.
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=40, blit=True)

plt.show()
