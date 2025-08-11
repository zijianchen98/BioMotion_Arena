
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a sitting down action
key_points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_hand',
    'left_shoulder', 'left_elbow', 'left_hand', 'right_hip', 'right_knee',
    'right_foot', 'left_hip', 'left_knee', 'left_foot', 'center_of_mass'
]

# Define initial positions for the key points
initial_positions = {
    'head': [0.0, 1.8],
    'neck': [0.0, 1.6],
    'right_shoulder': [-0.2, 1.5],
    'right_elbow': [-0.4, 1.3],
    'right_hand': [-0.6, 1.1],
    'left_shoulder': [0.2, 1.5],
    'left_elbow': [0.4, 1.3],
    'left_hand': [0.6, 1.1],
    'right_hip': [-0.2, 1.0],
    'right_knee': [-0.2, 0.5],
    'right_foot': [-0.2, 0.0],
    'left_hip': [0.2, 1.0],
    'left_knee': [0.2, 0.5],
    'left_foot': [0.2, 0.0],
    'center_of_mass': [0.0, 0.8]
}

# Define the animation frames
frames = 60
fps = 30

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 2.0)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter([], [], s=50, color='white')

# Function to update the scatter plot
def update(frame):
    # Update the positions of the key points for the current frame
    positions = {key: list(initial_positions[key]) for key in key_points}
    
    # Animate the sitting down action
    t = frame / frames
    for key in key_points:
        if key in ['right_knee', 'right_foot', 'left_knee', 'left_foot']:
            positions[key][1] *= (1 - t)  # Lower the legs
        elif key in ['right_hip', 'left_hip']:
            positions[key][1] *= (1 - t * 0.5)  # Lower the hips slightly
        elif key in ['right_elbow', 'right_hand', 'left_elbow', 'left_hand']:
            positions[key][1] *= (1 - t * 0.3)  # Lower the arms slightly
        elif key == 'center_of_mass':
            positions[key][1] *= (1 - t * 0.7)  # Lower the center of mass
    
    # Update the scatter plot data
    x = [positions[key][0] for key in key_points]
    y = [positions[key][1] for key in key_points]
    scat.set_offsets(np.c_[x, y])
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
