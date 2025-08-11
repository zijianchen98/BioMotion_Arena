
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 0],
    [0.5, 1],
    [1, 1],
    [1.5, 1],
    [0.25, 2],
    [0.75, 2],
    [1.25, 2],
    [1.75, 2],
    [0.5, 3],
    [1.5, 3],
    [0.75, 4],
    [1.25, 4],
    [1, 5],
    [1, 6],
    [1, 7]
])


# Define a function to update the positions of the point lights
def update_positions(frame, positions):
    """Updates the positions of the point lights for each frame of the animation."""

    # Define the motion parameters. Adjust these to change the animation.
    rotation_speed = 0.05  # radians per frame
    radius = 2.0

    # Rotate each point around the center
    center_x = np.mean(positions[:, 0])
    center_y = np.mean(positions[:, 1])

    rotated_positions = np.zeros_like(positions)
    for i, (x, y) in enumerate(positions):
      dx = x - center_x
      dy = y - center_y
      rotated_x = center_x + dx * np.cos(frame * rotation_speed) - dy * np.sin(frame * rotation_speed)
      rotated_y = center_y + dx * np.sin(frame * rotation_speed) + dy * np.cos(frame * rotation_speed)
      rotated_positions[i] = [rotated_x, rotated_y]
            
    return rotated_positions



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-2, 4])
ax.set_ylim([-1, 8])
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create the point lights
scat = ax.scatter([], [], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(
    fig, update_positions, frames=range(100), fargs=(initial_positions,), blit=False, interval=20, repeat=False
)

# Show the animation
plt.show()

