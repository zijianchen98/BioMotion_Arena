
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
point_lights = np.array([
    [-0.2, 0.5],  # head
    [-0.1, 0.4],  # right shoulder
    [0.1, 0.4],   # left shoulder
    [-0.2, 0.2],  # right elbow
    [0.2, 0.2],   # left elbow
    [-0.3, 0.1],  # right wrist
    [0.3, 0.1],   # left wrist
    [-0.1, 0.0],  # right hip
    [0.1, 0.0],   # left hip
    [-0.2, -0.2], # right knee
    [0.2, -0.2],  # left knee
    [-0.3, -0.4], # right ankle
    [0.3, -0.4],  # left ankle
    [0.0, 0.6],   # torso top
    [0.0, -0.6]   # torso bottom
])

# Define the motion parameters
fps = 30
duration = 2  # seconds
frames = int(fps * duration)

# Define the motion trajectory
def forward_rolling(t):
    angle = np.pi * t
    x = np.cos(angle)
    y = -np.sin(angle)
    return x, y

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    t = i / fps
    x, y = forward_rolling(t)
    
    # Update point-lights positions
    updated_point_lights = point_lights.copy()
    updated_point_lights[:, 0] += x
    updated_point_lights[:, 1] += y
    
    # Apply rotation to point-lights
    rotation_matrix = np.array([
        [np.cos(np.pi * t), -np.sin(np.pi * t)],
        [np.sin(np.pi * t), np.cos(np.pi * t)]
    ])
    updated_point_lights = np.dot(updated_point_lights, rotation_matrix)
    
    # Plot point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], c='white', s=10)

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000//fps, repeat=False)

plt.show()
