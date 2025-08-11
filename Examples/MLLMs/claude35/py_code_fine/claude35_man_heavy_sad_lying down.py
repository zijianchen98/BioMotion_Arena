
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Number of point lights
num_points = 15

# Generate initial positions for point lights (keypoints of a lying down figure)
# Approximate positions for a sad man lying down
initial_positions = np.array([
    [0, 4],   # head
    [-1, 3],  # left shoulder
    [1, 3],   # right shoulder
    [-1, 2],  # left elbow
    [1, 2],   # right elbow
    [-1, 1],  # left hand
    [1, 1],   # right hand
    [0, 0],   # torso
    [-1, -2], # left hip
    [1, -2],  # right hip
    [-1, -4], # left knee
    [1, -4],  # right knee
    [-1, -5], # left foot
    [1, -5],  # right foot
    [0, -3],  # belly (weighted)
])

# Update function for animation
def update(frame):
    # Simulate the motion of the points (smooth and biomechanically plausible)
    # Adding simple downward motion to depict heaviness
    new_positions = initial_positions.copy()
    
    # Here we simulate the movement by updating positions
    new_positions[:, 1] -= 0.1 * (frame % 50) / 50  # make it slightly heavier overall gradually

    # Update the data for points
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
