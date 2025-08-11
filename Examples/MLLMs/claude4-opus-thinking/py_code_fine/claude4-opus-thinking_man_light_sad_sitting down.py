
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 1)
ax.axis('off')  # Turn off the axis

# Number of points (15 as per requirement)
num_points = 15

# Initial positions of points for the "sad man sitting down"
# (x, y) coordinates for the point lights
point_positions = np.array([
    (0, 0.8),  # Head
    (0.3, 0.5), (-0.3, 0.5),  # Shoulders
    (0.4, 0.3), (-0.4, 0.3),  # Upper body
    (0.2, 0.1), (-0.2, 0.1),  # Arms
    (0, -0.3),  # Waist
    (0.2, -0.6), (-0.2, -0.6),  # Upper legs
    (0.2, -1.0), (-0.2, -1.0),  # Lower legs
    (0, -1.2),  # Feet
])

# Number of frames in the animation
num_frames = 100

# Function to update the points
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1, 1)
    ax.axis('off')  # Turn off the axis
    
    # Slightly move points to create the effect of sitting
    # Simulating smooth sinking motion
    offset_y = (frame / num_frames) * 0.3  # Control the amount of motion here
    moved_positions = point_positions.copy()
    moved_positions[:, 1] -= offset_y  # Move down
    
    # Plot the points
    ax.scatter(moved_positions[:, 0], moved_positions[:, 1], color='white', s=100)

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, repeat=True)

# Show the animation
plt.show()
