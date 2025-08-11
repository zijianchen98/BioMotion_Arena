
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15  # Number of point-lights
frames = 100     # Number of frames in the animation
weight_position = np.array([1.0, -0.5])  # Position of the weight relative to the center
background_color = 'black'
point_color = 'white'

# Initialize point positions (15 points)
# Here we define a simple skeleton structure for the points
# Y coordinates will simulate a happy running motion
point_positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Elbows
    [-0.5, -0.5], [0.5, -0.5],  # Hips
    [-0.75, -1], [0.75, -1],  # Knees
    [-0.5, -1.5], [0.5, -1.5],  # Feet
    [0, -2],  # Weight position (heavy)
    [1.0, -2]  # Opposite side for balance
]).T  # Transpose to get shape (2, num_points)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.set_facecolor(background_color)

# Create scatter plot for initial points
points = ax.scatter(point_positions[0, :], point_positions[1, :], color=point_color)

# Animation function
def animate(i):
    # Running motion (simple sinusoidal for vertical movement)
    angle = np.pi * i / frames
    vertical_offset = 0.5 * np.sin(3 * angle)

    # Update points' positions
    # Apply running motion to "head", "torso", "hips", and add weight offset
    point_positions[1, 0] = 1 + vertical_offset  # Head
    point_positions[1, 1:3] = 0.5 + vertical_offset  # Shoulders
    point_positions[1, 3:5] = vertical_offset  # Elbows
    point_positions[1, 5:7] = -0.5 + vertical_offset  # Hips
    point_positions[1, 7:9] = -1 + vertical_offset  # Knees
    point_positions[1, 9:11] = -1.5 + vertical_offset  # Feet
    point_positions[1, 10] = -2 + vertical_offset  # Weight position
    point_positions[1, 11] = -2 + vertical_offset  # Opposite side for balance

    points.set_offsets(point_positions.T)

    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
