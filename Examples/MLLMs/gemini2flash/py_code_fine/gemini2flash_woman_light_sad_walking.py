
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (adjust these to represent a standing figure)
initial_positions = np.array([
    [0, 2],  # Head
    [-0.3, 1.6],  # Left Shoulder
    [0.3, 1.6],  # Right Shoulder
    [-0.6, 1.2],  # Left Elbow
    [0.6, 1.2],  # Right Elbow
    [-0.9, 0.8],  # Left Hand
    [0.9, 0.8],  # Right Hand
    [0, 1.2],  # Spine Top
    [0, 0.5],  # Spine Bottom
    [-0.3, 0.4],  # Left Hip
    [0.3, 0.4],  # Right Hip
    [-0.5, -0.2],  # Left Knee
    [0.5, -0.2],  # Right Knee
    [-0.7, -0.8],  # Left Foot
    [0.7, -0.8]   # Right Foot
])

# Define the walking motion (adjust these to create a realistic walking animation)
def walking_motion(frame_num):
    # Normalize frame number to be between 0 and 1 for a smoother loop
    t = (frame_num % 100) / 100.0

    # Example motion: sinusoidal movement of arms and legs
    positions = initial_positions.copy()

    # Arm motion
    positions[3, 0] += 0.2 * np.sin(2 * np.pi * t)  # Left Elbow
    positions[5, 0] += 0.3 * np.sin(2 * np.pi * t)  # Left Hand
    positions[4, 0] -= 0.2 * np.sin(2 * np.pi * t)  # Right Elbow
    positions[6, 0] -= 0.3 * np.sin(2 * np.pi * t)  # Right Hand

    # Leg motion
    positions[11, 0] += 0.15 * np.sin(2 * np.pi * t + np.pi)  # Left Knee
    positions[13, 0] += 0.2 * np.sin(2 * np.pi * t + np.pi)  # Left Foot
    positions[12, 0] -= 0.15 * np.sin(2 * np.pi * t + np.pi)  # Right Knee
    positions[14, 0] -= 0.2 * np.sin(2 * np.pi * t + np.pi)  # Right Foot

    # Slight vertical bobbing
    positions[:, 1] += 0.05 * np.sin(4 * np.pi * t)

    return positions


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=8)

# Animation function
def animate(frame_num):
    positions = walking_motion(frame_num)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

plt.show()
