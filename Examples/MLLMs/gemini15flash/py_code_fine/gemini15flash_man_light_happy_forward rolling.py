
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point-lights
positions = np.array([
    [0, 5],  # Head
    [-1, 4], [0, 4], [1, 4], # Shoulders
    [-1.5, 3], [-0.5, 3], [0.5, 3], [1.5, 3], # Upper arms
    [-1.5, 2], [-0.5, 2], [0.5, 2], [1.5, 2], # Lower arms
    [0, 1], [0.5, 0], [-0.5, 0] # Legs
])


# Function to update the positions of the point-lights for each frame
def update(frame):
    global positions

    # Simple rolling motion (replace with more sophisticated biomechanical model for better realism)

    # Head movement
    positions[0, 0] += 0.02 * np.sin(frame * 0.1)
    positions[0, 1] += 0.05

    # Shoulder movement
    positions[1:4, 0] += 0.05 * np.sin(frame * 0.1)
    positions[1:4, 1] += 0.05

    # Arm movement
    positions[4:8, 0] += 0.1 * np.sin(frame * 0.2)
    positions[4:8, 1] += 0.05

    # Leg movement
    positions[8:12, 0] += 0.08 * np.sin(frame * 0.15)
    positions[8:12, 1] += 0.05


    # Plot the point-lights
    ln.set_offsets(positions)
    return ln,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-3, 3])
ax.set_ylim([-1, 7])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light scatter plot
ln, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

