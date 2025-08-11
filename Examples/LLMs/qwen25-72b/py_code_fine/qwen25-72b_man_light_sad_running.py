
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the sadman's joints
points = {
    'head': [0, 1.5],
    'neck': [0, 1.0],
    'shoulder_l': [-0.5, 0.8],
    'shoulder_r': [0.5, 0.8],
    'elbow_l': [-1.0, 0.5],
    'elbow_r': [1.0, 0.5],
    'wrist_l': [-1.2, 0.0],
    'wrist_r': [1.2, 0.0],
    'hip_l': [-0.4, -0.2],
    'hip_r': [0.4, -0.2],
    'knee_l': [-0.6, -0.8],
    'knee_r': [0.6, -0.8],
    'ankle_l': [-0.7, -1.2],
    'ankle_r': [0.7, -1.2],
    'center': [0, 0]
}

# Convert the points to a list of coordinates
coordinates = np.array([points[key] for key in points])

# Define the running motion parameters
def running_motion(t):
    # Head
    coordinates[0] = [0, 1.5 + 0.1 * np.sin(t)]
    
    # Neck
    coordinates[1] = [0, 1.0 + 0.1 * np.sin(t)]
    
    # Shoulders
    coordinates[2] = [-0.5 + 0.1 * np.sin(t), 0.8 + 0.1 * np.sin(t)]
    coordinates[3] = [0.5 - 0.1 * np.sin(t), 0.8 + 0.1 * np.sin(t)]
    
    # Elbows
    coordinates[4] = [-1.0 + 0.2 * np.sin(t), 0.5 + 0.2 * np.cos(t)]
    coordinates[5] = [1.0 - 0.2 * np.sin(t), 0.5 - 0.2 * np.cos(t)]
    
    # Wrists
    coordinates[6] = [-1.2 + 0.3 * np.sin(t), 0.0 + 0.3 * np.cos(t)]
    coordinates[7] = [1.2 - 0.3 * np.sin(t), 0.0 - 0.3 * np.cos(t)]
    
    # Hips
    coordinates[8] = [-0.4 + 0.1 * np.sin(t), -0.2 + 0.1 * np.cos(t)]
    coordinates[9] = [0.4 - 0.1 * np.sin(t), -0.2 - 0.1 * np.cos(t)]
    
    # Knees
    coordinates[10] = [-0.6 + 0.2 * np.sin(t), -0.8 + 0.2 * np.cos(t)]
    coordinates[11] = [0.6 - 0.2 * np.sin(t), -0.8 - 0.2 * np.cos(t)]
    
    # Ankles
    coordinates[12] = [-0.7 + 0.3 * np.sin(t), -1.2 + 0.3 * np.cos(t)]
    coordinates[13] = [0.7 - 0.3 * np.sin(t), -1.2 - 0.3 * np.cos(t)]
    
    # Center
    coordinates[14] = [0.1 * np.sin(t), 0.1 * np.cos(t)]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the point-lights
scat = ax.scatter(coordinates[:, 0], coordinates[:, 1], s=50, c='white')

# Animation update function
def update(frame):
    running_motion(frame)
    scat.set_offsets(coordinates)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 200), interval=50, blit=True)

# Show the animation
plt.show()
