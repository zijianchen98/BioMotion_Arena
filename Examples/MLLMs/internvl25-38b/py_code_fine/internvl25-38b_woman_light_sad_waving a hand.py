
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Initial positions (y-axis represents height, x-axis represents horizontal position)
# Positions are arranged as follows: head, torso, arms, legs
points = np.array([
    [0, 0],  # head
    [0, -1],  # torso
    [-1, -2], [-1.5, -3], [-2, -4],  # left arm
    [1, -2], [1.5, -3], [2, -4],  # right arm
    [-1, -5], [-1, -6],  # left leg
    [1, -5], [1, -6],  # right leg
])

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-8, 2)
ax.axis('off')
ax.set_facecolor('black')

# For point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, c='white', animated=True)

# Frame update function
def update(frame):
    global points
    t = 2 * np.pi * frame / 20.0

    # Waving motion for the right arm
    right_arm = points[6:9]
    right_arm[:, 0] = points[5][0] + 1 * np.sin(t)
    right_arm[:, 1] = points[5][1] + 0.5 * np.sin(t)

    # Update the scatter plot with new positions
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 20), interval=50, blit=True)

# Show plot
plt.show()
