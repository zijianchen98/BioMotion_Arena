
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],  # Right Elbow
    [-1.5, 0.5], # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.2, 1.0], # Mid-Torso
    [-0.5, 0.0], # Left Hip
    [0.5, 0.0],  # Right Hip
    [-0.8, -1.0],# Left Knee
    [0.8, -1.0], # Right Knee
    [-0.8, -2.0],# Left Ankle
    [0.8, -2.0], # Right Ankle
    [0.0, 0.5]   # Center Torso
])

# Define the movement of the point-lights for the "sitting down" action
def update_points(frame_num, points):
    x = initial_positions[:, 0].copy()
    y = initial_positions[:, 1].copy()

    # Simulate sitting down movement
    y[[8, 9]] += 0.2 * np.sin(frame_num * 0.1) # Hips move down
    y[[10, 11]] += 0.4 * np.sin(frame_num * 0.1) # Knees move down
    y[[12, 13]] += 0.6 * np.sin(frame_num * 0.1) # Ankles move down
    y[1] += 0.1 * np.sin(frame_num * 0.1) # Move left shoulder
    y[2] += 0.1 * np.sin(frame_num * 0.1) # Move right shoulder

    points.set_data(x, y)
    return points,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.axis('off')

# Create the initial scatter plot
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,), frames=num_frames, interval=50, blit=True, repeat=True)

# Show the animation
plt.show()
