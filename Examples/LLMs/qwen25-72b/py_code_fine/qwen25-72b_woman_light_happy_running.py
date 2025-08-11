
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a running woman
key_points = [
    'head', 'neck', 'shoulder_left', 'elbow_left', 'wrist_left',
    'shoulder_right', 'elbow_right', 'wrist_right', 'hip_left', 'knee_left',
    'ankle_left', 'hip_right', 'knee_right', 'ankle_right', 'pelvis'
]

# Define the initial positions of the key points
initial_positions = {
    'head': [0, 1.5],
    'neck': [0, 1.0],
    'shoulder_left': [-0.5, 0.8],
    'elbow_left': [-0.7, 0.5],
    'wrist_left': [-0.6, 0.2],
    'shoulder_right': [0.5, 0.8],
    'elbow_right': [0.7, 0.5],
    'wrist_right': [0.6, 0.2],
    'hip_left': [-0.3, 0.0],
    'knee_left': [-0.4, -0.3],
    'ankle_left': [-0.3, -0.6],
    'hip_right': [0.3, 0.0],
    'knee_right': [0.4, -0.3],
    'ankle_right': [0.3, -0.6],
    'pelvis': [0, 0.0]
}

# Convert the initial positions to a list of coordinates
points = [initial_positions[key] for key in key_points]

# Function to update the positions of the points for each frame
def update(frame):
    # Update the positions based on the running motion
    for i, key in enumerate(key_points):
        if key == 'head':
            points[i][0] += 0.05 * np.sin(frame * 0.1)
            points[i][1] = 1.5 + 0.1 * np.sin(frame * 0.1)
        elif key == 'neck':
            points[i][0] += 0.05 * np.sin(frame * 0.1)
            points[i][1] = 1.0 + 0.1 * np.sin(frame * 0.1)
        elif key in ['shoulder_left', 'elbow_left', 'wrist_left']:
            points[i][0] += 0.05 * np.sin(frame * 0.1)
            points[i][1] += 0.1 * np.sin(frame * 0.1)
        elif key in ['shoulder_right', 'elbow_right', 'wrist_right']:
            points[i][0] += 0.05 * np.sin(frame * 0.1)
            points[i][1] -= 0.1 * np.sin(frame * 0.1)
        elif key in ['hip_left', 'knee_left', 'ankle_left']:
            points[i][0] += 0.05 * np.sin(frame * 0.1)
            points[i][1] += 0.2 * np.sin(frame * 0.1)
        elif key in ['hip_right', 'knee_right', 'ankle_right']:
            points[i][0] += 0.05 * np.sin(frame * 0.1)
            points[i][1] -= 0.2 * np.sin(frame * 0.1)
        elif key == 'pelvis':
            points[i][0] += 0.05 * np.sin(frame * 0.1)
    
    # Update the scatter plot data
    scat.set_offsets(points)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(*zip(*points), color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), interval=50)

# Display the animation
plt.show()
