
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the lights representing the body parts of a running person
body_parts = ['head', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
              'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee',
              'right_knee', 'left_ankle', 'right_ankle', 'left_toe', 'right_toe']

# Initial positions of the points (x, y)
initial_positions = {
    'head': (0, 2),
    'left_shoulder': (-0.5, 1.5),
    'right_shoulder': (0.5, 1.5),
    'left_elbow': (-1, 1),
    'right_elbow': (1, 1),
    'left_wrist': (-1.5, 0.5),
    'right_wrist': (1.5, 0.5),
    'left_hip': (-0.5, -0.5),
    'right_hip': (0.5, -0.5),
    'left_knee': (-0.5, -1.5),
    'right_knee': (0.5, -1.5),
    'left_ankle': (-0.5, -2.5),
    'right_ankle': (0.5, -2.5),
    'left_toe': (-0.5, -3),
    'right_toe': (0.5, -3)
}

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 3)
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter(*zip(*initial_positions.values()), color='white', s=50)

# Function to update the frame
def update(frame):
    positions = initial_positions.copy()
    
    # Simulate running motion
    if frame % 2 == 0:
        positions['left_ankle'] = (-0.5, -2.5 + np.sin(frame / 10))
        positions['right_ankle'] = (0.5, -2.5 + np.cos(frame / 10))
        positions['left_toe'] = (-0.5, -3 + np.sin(frame / 10))
        positions['right_toe'] = (0.5, -3 + np.cos(frame / 10))
        
        positions['left_elbow'] = (-1 + 0.1 * np.sin(frame / 5), 1)
        positions['right_elbow'] = (1 - 0.1 * np.sin(frame / 5), 1)
        positions['left_wrist'] = (-1.5 + 0.1 * np.sin(frame / 5), 0.5)
        positions['right_wrist'] = (1.5 - 0.1 * np.sin(frame / 5), 0.5)
    else:
        positions['left_ankle'] = (-0.5, -2.5 + np.cos(frame / 10))
        positions['right_ankle'] = (0.5, -2.5 + np.sin(frame / 10))
        positions['left_toe'] = (-0.5, -3 + np.cos(frame / 10))
        positions['right_toe'] = (0.5, -3 + np.sin(frame / 10))
        
        positions['left_elbow'] = (-1 - 0.1 * np.cos(frame / 5), 1)
        positions['right_elbow'] = (1 + 0.1 * np.cos(frame / 5), 1)
        positions['left_wrist'] = (-1.5 - 0.1 * np.cos(frame / 5), 0.5)
        positions['right_wrist'] = (1.5 + 0.1 * np.cos(frame / 5), 0.5)
    
    scat.set_offsets(list(positions.values()))

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
