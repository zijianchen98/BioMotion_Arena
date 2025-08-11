
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100
duration = 8  # in seconds

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize point lights' positions
points = np.zeros((num_points, 2))

# Define initial positions of point-lights to represent a happy man
# A simplistic configuration
initial_positions = np.array([
    [0, 8],  # Head
    [-1.5, 5], [1.5, 5],  # Shoulders
    [-3, 3], [0, 3], [3, 3],  # Arms
    [-2, 1], [2, 1],  # Hands
    [-1, -2], [0, -2], [1, -2],  # Waist
    [-3, -5], [0, -5], [3, -5],  # Legs
    [-1, -7], [1, -7]  # Feet
])

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=100)

# Calculate motion trajectory for forward rolling
def update(frame):
    # Update points positions based on rolling motion
    roll_angle = np.pi * frame / frames  # 1 full roll in 100 frames
    for i in range(num_points):
        if i == 0:  # Head stays more stable
            points[i, 0] = initial_positions[i, 0]
            points[i, 1] = initial_positions[i, 1] - (0.2 * frame)  # Slight downward motion
        else:
            # Rolling effect on body positions
            points[i, 0] = initial_positions[i, 0] * np.cos(roll_angle) + initial_positions[i, 1] * np.sin(roll_angle)
            points[i, 1] = -initial_positions[i, 0] * np.sin(roll_angle) + initial_positions[i, 1] * np.cos(roll_angle) - (0.2 * frame)

    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000*duration/frames, blit=True)

# Show the animation
plt.show()
