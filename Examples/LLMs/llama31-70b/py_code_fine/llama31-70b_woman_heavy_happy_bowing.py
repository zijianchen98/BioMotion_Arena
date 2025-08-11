
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the happy woman
point_lights = np.array([
    [0, -0.5],  # Head
    [-0.2, -0.3],  # Left shoulder
    [0.2, -0.3],  # Right shoulder
    [-0.3, -0.2],  # Left elbow
    [0.3, -0.2],  # Right elbow
    [-0.4, 0],  # Left hand
    [0.4, 0],  # Right hand
    [0, -0.6],  # Hip
    [-0.2, -0.8],  # Left knee
    [0.2, -0.8],  # Right knee
    [-0.3, -1],  # Left foot
    [0.3, -1],  # Right foot
    [-0.1, -0.4],  # Left breast
    [0.1, -0.4],  # Right breast
    [0, -0.7],  # Weight
])

# Define the animation frames
frames = 30
animation_data = np.zeros((frames, 15, 2))

# Simulate the bowing motion
for i in range(frames):
    angle = np.pi / 2 * (1 - i / frames)
    animation_data[i, :, :] = point_lights.copy()
    animation_data[i, 0, :] = [0, -0.5 + 0.1 * np.sin(angle)]  # Head
    animation_data[i, 1, :] = [-0.2, -0.3 + 0.1 * np.sin(angle)]  # Left shoulder
    animation_data[i, 2, :] = [0.2, -0.3 + 0.1 * np.sin(angle)]  # Right shoulder
    animation_data[i, 3, :] = [-0.3, -0.2 + 0.1 * np.sin(angle)]  # Left elbow
    animation_data[i, 4, :] = [0.3, -0.2 + 0.1 * np.sin(angle)]  # Right elbow
    animation_data[i, 5, :] = [-0.4, 0 + 0.1 * np.sin(angle)]  # Left hand
    animation_data[i, 6, :] = [0.4, 0 + 0.1 * np.sin(angle)]  # Right hand
    animation_data[i, 7, :] = [0, -0.6 + 0.1 * np.sin(angle)]  # Hip
    animation_data[i, 8, :] = [-0.2, -0.8 + 0.1 * np.sin(angle)]  # Left knee
    animation_data[i, 9, :] = [0.2, -0.8 + 0.1 * np.sin(angle)]  # Right knee
    animation_data[i, 10, :] = [-0.3, -1 + 0.1 * np.sin(angle)]  # Left foot
    animation_data[i, 11, :] = [0.3, -1 + 0.1 * np.sin(angle)]  # Right foot
    animation_data[i, 12, :] = [-0.1, -0.4 + 0.1 * np.sin(angle)]  # Left breast
    animation_data[i, 13, :] = [0.1, -0.4 + 0.1 * np.sin(angle)]  # Right breast
    animation_data[i, 14, :] = [0, -0.7 + 0.1 * np.sin(angle)]  # Weight

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 0.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the first frame
scatter = ax.scatter(animation_data[0, :, 0], animation_data[0, :, 1], c='white', s=10)

# Define the animation function
def animate(i):
    scatter.set_offsets(animation_data[i, :, :])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50)

plt.show()
