
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the number of points
num_frames = 100
num_points = 15

# Define the initial positions of the points (standing position)
initial_positions = np.array([
    [0, 3],  # Head
    [-0.5, 2.5],  # Left Shoulder
    [0.5, 2.5],  # Right Shoulder
    [-1, 2],  # Left Elbow
    [1, 2],  # Right Elbow
    [-1.5, 1.5],  # Left Wrist
    [1.5, 1.5],  # Right Wrist
    [-0.2, 2], # Neck
    [-0.2, 1.3],  # Hip center
    [-0.7, 0.7],  # Left Hip
    [0.3, 0.7],  # Right Hip
    [-0.8, 0],  # Left Knee
    [0.4, 0],  # Right Knee
    [-0.9, -0.7],  # Left Ankle
    [0.5, -0.7],  # Right Ankle
])

# Define the final positions of the points (sitting position)
final_positions = np.array([
    [0, 2.5],  # Head
    [-0.5, 2],  # Left Shoulder
    [0.5, 2],  # Right Shoulder
    [-1, 1.5],  # Left Elbow
    [1, 1.5],  # Right Elbow
    [-1.2, 1],  # Left Wrist
    [1.2, 1],  # Right Wrist
    [-0.2, 1.5], # Neck
    [-0.2, 0.8],  # Hip center
    [-0.7, 0.2],  # Left Hip
    [0.3, 0.2],  # Right Hip
    [-0.3, -0.2],  # Left Knee
    [0.1, -0.2],  # Right Knee
    [-0.3, -0.6],  # Left Ankle
    [0.2, -0.6],  # Right Ankle
])


# Create the animation data by interpolating between the initial and final positions
data = np.zeros((num_points, 2, num_frames))
for i in range(num_points):
    for j in range(2):
        data[i, j, :] = np.linspace(initial_positions[i, j], final_positions[i, j], num_frames)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3.5)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scat = ax.scatter(data[:, 0, 0], data[:, 1, 0], c='white', s=50)

# Define the animation function
def animate(i):
    scat.set_offsets(data[:, :, i].T)
    return (scat,)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
