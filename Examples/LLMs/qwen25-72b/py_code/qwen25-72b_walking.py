
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a walking human figure
key_points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_hand',
    'left_shoulder', 'left_elbow', 'left_hand', 'right_hip', 'right_knee',
    'right_foot', 'left_hip', 'left_knee', 'left_foot', 'pelvis'
]

# Define the initial positions of the key points
initial_positions = {
    'head': [0, 1.8],
    'neck': [0, 1.6],
    'right_shoulder': [-0.2, 1.4],
    'right_elbow': [-0.4, 1.2],
    'right_hand': [-0.6, 1.0],
    'left_shoulder': [0.2, 1.4],
    'left_elbow': [0.4, 1.2],
    'left_hand': [0.6, 1.0],
    'right_hip': [-0.2, 1.0],
    'right_knee': [-0.4, 0.6],
    'right_foot': [-0.6, 0.2],
    'left_hip': [0.2, 1.0],
    'left_knee': [0.4, 0.6],
    'left_foot': [0.6, 0.2],
    'pelvis': [0, 0.8]
}

# Define the walking cycle
def walk_cycle(t):
    # t is the time in seconds
    amplitude = 0.1
    frequency = 1.0  # cycles per second
    phase_shift = 0.0  # phase shift in radians
    
    # Calculate the position of each key point at time t
    positions = {}
    for key, (x, y) in initial_positions.items():
        if 'foot' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif 'knee' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift + np.pi)
        elif 'hip' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift + np.pi / 2)
        elif 'hand' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift + np.pi)
        elif 'elbow' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift + np.pi / 2)
        elif 'shoulder' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif 'neck' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        elif 'head' in key:
            y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
        
        positions[key] = [x, y]
    
    return positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter([], [], c='white', s=50)

# Update function for the animation
def update(frame):
    positions = walk_cycle(frame / 10)  # frame / 10 to slow down the animation
    x = [positions[key][0] for key in key_points]
    y = [positions[key][1] for key in key_points]
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
