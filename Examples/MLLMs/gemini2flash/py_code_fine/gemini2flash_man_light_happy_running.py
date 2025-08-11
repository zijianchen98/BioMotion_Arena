
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 50
num_points = 15

# Define the initial positions of the points (x, y)
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left Shoulder
    [0.6, 0.8],  # Right Shoulder
    [0.3, 0.7],  # Left Elbow
    [0.7, 0.7],  # Right Elbow
    [0.2, 0.6],  # Left Hand
    [0.8, 0.6],  # Right Hand
    [0.45, 0.65], # Spine Upper
    [0.55, 0.65], # Spine Upper
    [0.5, 0.55], # Spine Mid
    [0.5, 0.45],  # Hip
    [0.4, 0.35],  # Left Knee
    [0.6, 0.35],  # Right Knee
    [0.3, 0.25],  # Left Foot
    [0.7, 0.25]   # Right Foot
])

# Define the motion of the points for each frame (example: running motion)
def update_points(frame_num):
    x = initial_positions[:, 0].copy()
    y = initial_positions[:, 1].copy()
    
    # Example motion (running) - adjust these values for a more realistic motion
    y[1] += 0.01 * np.sin(frame_num * 0.2)  # Left shoulder
    y[2] -= 0.01 * np.sin(frame_num * 0.2)  # Right shoulder
    y[3] += 0.02 * np.sin(frame_num * 0.2)  # Left elbow
    y[4] -= 0.02 * np.sin(frame_num * 0.2)  # Right elbow
    y[5] += 0.03 * np.sin(frame_num * 0.2)  # Left hand
    y[6] -= 0.03 * np.sin(frame_num * 0.2)  # Right hand
    y[11] += 0.04 * np.sin(frame_num * 0.2)  # Left knee
    y[12] -= 0.04 * np.sin(frame_num * 0.2)  # Right knee
    y[13] += 0.05 * np.sin(frame_num * 0.2)  # Left foot
    y[14] -= 0.05 * np.sin(frame_num * 0.2)  # Right foot

    # Adjust the up-down movement of the hip with running 
    y[10] += 0.005 * np.sin(frame_num * 0.2)

    # Cyclic switching left-right motion to mimic running
    x[11] += 0.01 * np.sin(frame_num * 0.4) #left knee
    x[12] -= 0.01 * np.sin(frame_num * 0.4) #right knee
    x[13] += 0.02 * np.sin(frame_num * 0.4) #left foot
    x[14] -= 0.02 * np.sin(frame_num * 0.4) #right foot
    
    points.set_data(x, y)
    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.axis('off')

# Create the points
points, = ax.plot([], [], 'wo', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, blit=True, interval=20, repeat=True, frames=num_frames)

# Show the animation
plt.show()
