
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # number of points
duration = 1000  # duration of the animation frame in milliseconds
frames = 60  # number of frames in the animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.axis('off')  # turn off axis

# Initialize points' positions
points = np.zeros((num_points, 2))

# Define the initial positions of the points making an abstract representation of a jumping body
initial_positions = np.array([
    [0, 0],   # center point (torso)
    [-0.5, 1.5], [0.5, 1.5],   # shoulder points
    [-0.75, 3], [0.75, 3],  # hand points (arms up)
    [-0.25, 2], [0.25, 2],  # hip points
    [-0.5, 0], [0.5, 0],   # knee points
    [-0.5, -1], [0.5, -1],  # ankle points
])

points[:initial_positions.shape[0]] = initial_positions

# Function to update the points' positions
def update(frame):
    # Clear previous points
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 5)
    ax.axis('off')

    # Update positions to create a jumping effect
    vertical_jump = 3 * np.sin(frame / 10.0)  # simulate upward and downward motion
    points[:, 1] = initial_positions[:, 1] + vertical_jump  # modify vertical position
    points[:, 0] += 0.1  # move to the right for forward jumping effect
    
    # Draw points
    ax.plot(points[:, 0], points[:, 1], 'o', color='white')

# Create Animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=duration / frames)

# Display the animation
plt.show()
