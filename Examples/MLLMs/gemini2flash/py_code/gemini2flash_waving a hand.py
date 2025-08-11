
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],   # Right Elbow
    [-1.5, 0.5], # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.2, 1.0], # Left Hip
    [0.2, 1.0],  # Right Hip
    [-0.2, 0.0], # Left Knee
    [0.2, 0.0],  # Right Knee
    [-0.2, -1.0],# Left Ankle
    [0.2, -1.0], # Right Ankle
    [0.0, 0.5],  # Torso
    [0.0, -1.5], # Feet
])

# Define the motion of the point-lights over time
def update_points(num):
    x = positions[:, 0] + np.sin(2 * np.pi * (num / num_frames)) * 0.2
    y = positions[:, 1] 
    
    # Simulate waving motion with the right hand
    positions[5, 0] = initial_positions[5, 0] + np.sin(2 * np.pi * (num / num_frames)) * 0.5
    positions[5, 1] = initial_positions[5, 1] + np.cos(2 * np.pi * (num / num_frames)) * 0.2
    
    # Simulate waving motion with the left hand
    positions[4, 0] = initial_positions[4, 0] + np.sin(2 * np.pi * (num / num_frames)) * 0.5
    positions[4, 1] = initial_positions[4, 1] - np.cos(2 * np.pi * (num / num_frames)) * 0.2

    point.set_data(positions[:, 0], positions[:, 1])
    return point,

# Create the figure and axes
fig = plt.figure(figsize=(6, 8))
ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
plt.axis('off')

# Create the point-light stimulus
positions = initial_positions.copy()
point, = ax.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, interval=50, blit=True)

plt.show()
