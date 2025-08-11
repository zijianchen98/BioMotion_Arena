
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize parameters
num_points = 15
fps = 30
duration = 3  # duration of the animation in seconds
frames = fps * duration

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Starting positions of the point lights for the bowing animation
def get_positions(frame):
    # Create a base position for the points to start from
    # These will represent the location of joints in a simplistic bowing figure
    base_positions = np.array([
        [0, 0],  # Head
        [0, -0.5],  # Middle body
        [0.5, -1],  # Right shoulder
        [-0.5, -1],  # Left shoulder
        [0.5, -1.5],  # Right elbow
        [-0.5, -1.5],  # Left elbow
        [1, -2],  # Right hand
        [-1, -2],  # Left hand
        [0, -2.5],  # Lower back
        [0.5, -1.5],  # Right leg
        [-0.5, -1.5],  # Left leg
        [0.3, -3],  # Right knee
        [-0.3, -3],  # Left knee
        [0, -3.5],  # Feet
        [0, -0.2]   # Weighted object air
    ])

    # Modify positions for bowing motion
    angle = np.pi / 4 * np.sin(frame / (frames / (2 * np.pi)))  # Oscillating angle for bowing
    bowing_positions = base_positions.copy()
    
    # Adjust y-coordinates for bowing
    bowing_positions[:, 1] -= 0.5 * (1 - np.cos(angle))

    return bowing_positions

# Initialize scatter plot
points, = ax.plot([], [], 'o', color='white')

# Animation update function
def update(frame):
    positions = get_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000 / fps, blit=True)

# Show the animation
plt.show()
