
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for the sadman's body
key_points = {
    'head': [0, 1],
    'neck': [0, 0.8],
    'shoulder_left': [-0.3, 0.6],
    'shoulder_right': [0.3, 0.6],
    'elbow_left': [-0.4, 0.4],
    'elbow_right': [0.4, 0.4],
    'wrist_left': [-0.5, 0.2],
    'wrist_right': [0.5, 0.2],
    'hip_left': [-0.2, 0.2],
    'hip_right': [0.2, 0.2],
    'knee_left': [-0.2, -0.2],
    'knee_right': [0.2, -0.2],
    'ankle_left': [-0.2, -0.6],
    'ankle_right': [0.2, -0.6],
    'center_of_mass': [0, 0]
}

# Define the initial positions of the points
points = np.array([key_points[key] for key in key_points])

# Define the animation parameters
frames = 100
fps = 30

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

def update(frame):
    # Update the positions of the points to simulate the bowing motion
    angle = np.sin(2 * np.pi * frame / frames) * 0.2
    for i, key in enumerate(key_points):
        if key != 'center_of_mass':
            points[i, 1] += angle * (1 - points[i, 1])
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
