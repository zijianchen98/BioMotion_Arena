
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')

# Define the initial positions of the point lights (15 points)
# Positions correspond to a jumping human figure
points = np.array([[0, 0], [0.5, 1.5], [-0.5, 1.5], [0.5, 2], [-0.5, 2], 
                   [0, 2.5], [0.2, 1], [-0.2, 1], [0.75, 1.5], [-0.75, 1.5],
                   [1, 0], [-1, 0], [0.75, 0.5], [-0.75, 0.5], [0, 0.5], [0, 0]])

# Create a scatter plot for the points
sc = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Update the positions of the point-lights to simulate jumping action
    # The y position oscillates to simulate a jump
    jump_height = 1.5 * np.sin(frame * 0.1)  # Oscillation for jumping effect
    new_points = points.copy()
    new_points[:, 1] += jump_height  # Apply jump height to each point's y-coordinate
    # Keep the lights within bounds
    new_points[:, 1] = np.clip(new_points[:, 1], 0, 2.5)
    sc.set_offsets(new_points)
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
