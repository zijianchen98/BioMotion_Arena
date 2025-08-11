
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Animation duration in frames
num_frames = 100

# Define the initial positions of the point-lights
# These positions correspond to a person lying down
initial_positions = np.array([
    [0, 10],   # Head
    [-2, 9],  # Left shoulder
    [2, 9],   # Right shoulder
    [-4, 7],  # Left elbow
    [4, 7],   # Right elbow
    [-6, 5],  # Left wrist
    [6, 5],   # Right wrist
    [0, 7],   # Spine
    [-1, 4],  # Left hip
    [1, 4],   # Right hip
    [-2, 2],  # Left knee
    [2, 2],   # Right knee
    [-3, 0],  # Left ankle
    [3, 0],   # Right ankle
    [0, 2]    # Centre
])

# Define the motion of the point-lights over time
# These movements should be small and coherent to simulate lying down movements
motion = np.random.randn(num_frames, num_points, 2) * 0.1

# Scale the motion to make it more realistic
motion[:, 0, :] *= 0.05  # Head motion
motion[:, 1:3, :] *= 0.08  # Shoulder motion
motion[:, 3:5, :] *= 0.1  # Elbow motion
motion[:, 5:7, :] *= 0.12  # Wrist motion
motion[:, 7, :] *= 0.06  # Spine motion
motion[:, 8:10, :] *= 0.09 # Hip Motion
motion[:, 10:12, :] *= 0.11 # Knee Motion
motion[:, 12:14, :] *= 0.13 # Ankle Motion
motion[:, 14, :] *= 0.07 # Centre Motion


# Function to update the positions of the point-lights for each frame
def update(frame_num):
    positions = initial_positions + np.sum(motion[:frame_num], axis=0)
    scat.set_offsets(positions)
    return (scat,)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-8, 8)
ax.set_ylim(-2, 12)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=20)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Display the animation
plt.show()
