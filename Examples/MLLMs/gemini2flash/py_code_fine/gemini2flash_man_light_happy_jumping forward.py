
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of frames in the animation
num_frames = 50

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 4],  # head
    [-0.5, 3], [0.5, 3],  # shoulders
    [-0.75, 2], [0.75, 2],  # elbows
    [-1, 1], [1, 1],  # wrists
    [-0.25, 2], [0.25, 2],  # torso
    [-0.5, 0], [0.5, 0],  # hips
    [-0.75, -1], [0.75, -1],  # knees
    [-1, -2], [1, -2]  # ankles
])

# Define the movement of the point-lights to simulate jumping forward
def update_points(frame_num):
    x = initial_positions[:, 0].copy()
    y = initial_positions[:, 1].copy()

    # Adjust positions to simulate jumping and forward movement
    y += np.sin(frame_num / 10) * 0.5  # Vertical jumping motion
    x += frame_num / 100  # Horizontal forward movement

    # Leg movements
    x[12] += np.sin(frame_num / 5) * 0.2  # Right knee
    y[12] += np.cos(frame_num / 5) * 0.1
    x[14] -= np.sin(frame_num / 5) * 0.2  # Left knee
    y[14] -= np.cos(frame_num / 5) * 0.1

    # Arm movements
    x[4] -= np.sin(frame_num / 5) * 0.1  # Right elbow
    y[4] -= np.cos(frame_num / 5) * 0.05
    x[6] += np.sin(frame_num / 5) * 0.1  # Left elbow
    y[6] += np.cos(frame_num / 5) * 0.05
    
    # Update the point positions
    points.set_data(x, y)
    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-2, 3)
ax.set_ylim(-3, 5)
ax.axis('off')  # Turn off the axes

# Create the scatter plot for the point-lights
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'wo', markersize=8)  # 'wo' for white circles

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, blit=True, repeat=True)

plt.show()
