
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the number of frames in the animation
n_frames = 100

# Define the position of the point-lights at each frame
positions = np.zeros((n_frames, n_points, 2))

# Define the initial positions of the point-lights
# Head, shoulders, elbows, hands, hips, knees, ankles
initial_positions = np.array([
    [0.0, 0.5],  # Head
    [-0.2, 0.4], [-0.1, 0.4],  # Shoulders
    [-0.3, 0.2], [-0.1, 0.2],  # Elbows
    [-0.4, 0.0], [-0.2, 0.0],  # Hands
    [0.0, 0.0],  # Hips
    [0.1, -0.2], [0.2, -0.2],  # Knees
    [0.1, -0.4], [0.2, -0.4],  # Ankles
    [0.0, -0.1], [0.1, -0.1], [-0.1, -0.1]  # Additional points for the body
])

# Define the movement of the point-lights
for i in range(n_frames):
    angle = i / n_frames * np.pi * 2
    positions[i] = initial_positions.copy()

    # Move the arms and legs
    positions[i, 3] = [-0.4 + 0.1 * np.sin(angle), 0.0]  # Left hand
    positions[i, 4] = [-0.2 + 0.1 * np.sin(angle), 0.0]  # Right hand
    positions[i, 9] = [0.1 + 0.1 * np.sin(angle), -0.2]  # Left knee
    positions[i, 10] = [0.2 + 0.1 * np.sin(angle), -0.2]  # Right knee
    positions[i, 11] = [0.1 + 0.1 * np.sin(angle), -0.4]  # Left ankle
    positions[i, 12] = [0.2 + 0.1 * np.sin(angle), -0.4]  # Right ankle

    # Move the hips and shoulders
    positions[i, 5] = [0.0 + 0.05 * np.sin(angle), 0.0]  # Hips
    positions[i, 1] = [-0.2 + 0.05 * np.sin(angle), 0.4]  # Left shoulder
    positions[i, 2] = [-0.1 + 0.05 * np.sin(angle), 0.4]  # Right shoulder

    # Move the head
    positions[i, 0] = [0.0 + 0.01 * np.sin(angle), 0.5]  # Head

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.6, 0.6)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot
scatter = ax.scatter(positions[0, :, 0], positions[0, :, 1], s=10, color='white')

# Animation function
def animate(i):
    scatter.set_offsets(positions[i])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

plt.show()
