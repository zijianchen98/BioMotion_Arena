
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 100
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
plt.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=6)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation for each frame
def animate(i):
    # Define the coordinates of the points for a walking sadman carrying heavy weight
    x = np.array([
        0.0 + 0.1 * np.sin(i * 0.1),  # Head
        -0.3 + 0.1 * np.sin(i * 0.1),  # Left shoulder
        0.3 + 0.1 * np.sin(i * 0.1),  # Right shoulder
        -0.6 + 0.1 * np.sin(i * 0.1),  # Left elbow
        0.6 + 0.1 * np.sin(i * 0.1),  # Right elbow
        -0.9 + 0.2 * np.sin(i * 0.15),  # Left wrist
        0.9 + 0.2 * np.sin(i * 0.15),  # Right wrist
        0.0 + 0.1 * np.sin(i * 0.1),  # Torso
        -0.3 + 0.1 * np.sin(i * 0.1 + np.pi),  # Left hip
        0.3 + 0.1 * np.sin(i * 0.1 + np.pi),  # Right hip
        -0.6 + 0.3 * np.sin(i * 0.15),  # Left knee
        0.6 + 0.3 * np.sin(i * 0.15),  # Right knee
        -0.9 + 0.4 * np.sin(i * 0.2),  # Left ankle
        0.9 + 0.4 * np.sin(i * 0.2),  # Right ankle
        0.0 + 0.05 * np.cos(i * 0.1)   # Middle
    ])
    y = np.array([
        1.0,  # Head
        0.7,  # Left shoulder
        0.7,  # Right shoulder
        0.4,  # Left elbow
        0.4,  # Right elbow
        0.1,  # Left wrist
        0.1,  # Right wrist
        0.5,  # Torso
        -0.1, # Left hip
        -0.1, # Right hip
        -0.4, # Left knee
        -0.4, # Right knee
        -0.7, # Left ankle
        -0.7, # Right ankle
        0.6 # Middle
    ])

    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True)

# Show the animation
plt.show()
