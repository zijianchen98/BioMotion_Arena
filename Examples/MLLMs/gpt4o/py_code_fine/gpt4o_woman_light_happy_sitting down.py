
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of 15 points representing joints
# These positions will represent the initial 'sitting down' posture 
# and will be animated to simulate biological motion.
def generate_biological_motion(frame):
    # Simplified model for "sitting down" animation
    points = np.array([
        [0, 8],  # Head
        [-1.5, 7], [1.5, 7],  # Shoulders
        [-2, 5.5], [2, 5.5],  # Elbows
        [-1.5, 4], [1.5, 4],  # Hands
        [-1, 6], [1, 6],  # Torso
        [-1, 2], [0, 2], [1, 2],  # Thighs
        [-1, 0], [0, 0], [1, 0],  # Feet
    ])

    # Add animation dynamics
    # Create a smooth "sitting down" movement by interpolating Y-axis values of legs
    vertical_shift = min(2 * frame / 100, 2)  # Smooth sitting-down motion
    points[9:12, 1] -= vertical_shift  # Adjust thigh positions
    points[12:15, 1] -= vertical_shift  # Adjust feet positions

    return points

# Create the point-light animation
def update(frame):
    points = generate_biological_motion(frame)
    scatter.set_offsets(points)
    return scatter,

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 9)
ax.set_facecolor('black')
ax.axis('off')

# Initialize scatter plot for points
points = generate_biological_motion(0)
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Create and display animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
