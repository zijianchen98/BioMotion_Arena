
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15   # Number of point-lights
duration = 10     # Duration of the animation in seconds
fps = 30          # Frames per second
total_frames = duration * fps

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initial positions of point-lights (15 points)
# Assuming a basic structure for a human body in 2D space
# Adjust positions according to desired joint locations
initial_positions = np.array([
    [0, 8],  # Head
    [-1, 6], [1, 6],  # Shoulders
    [-1, 4], [1, 4],  # Elbows
    [-2, 2], [2, 2],  # Hands
    [0, 2],  # Torso
    [0, 0],  # Hips
    [-1, -2], [1, -2],  # Knees
    [-1, -4], [1, -4],  # Feet
    [-0.5, -3], [0.5, -3],  # Weight position
])

# Create a scatter plot for the point-lights
points, = ax.plot([], [], 'o', color='white')

# Update function for animation
def update(frame):
    angle = frame * (2 * np.pi / total_frames)  # Simulate a rolling effect
    rolling_positions = initial_positions.copy()
    
    # Simple forward rolling motion transformation
    for i in range(rolling_positions.shape[0]):
        x_offset = 0.5 * np.sin(angle + np.pi * (i % 3) / 3)
        y_offset = -0.1 * frame / fps  # Move downwards as if rolling
        rolling_positions[i] += [x_offset, y_offset]
    
    points.set_data(rolling_positions[:, 0], rolling_positions[:, 1])
    return points,

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, blit=True, interval=1000 / fps)

# Show the animation
plt.show()
