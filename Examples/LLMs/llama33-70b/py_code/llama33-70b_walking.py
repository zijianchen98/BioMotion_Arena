
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the walking man
points = {
    'head': [0, 1.5],
    'left_shoulder': [-0.5, 1.2],
    'right_shoulder': [0.5, 1.2],
    'left_elbow': [-0.5, 0.8],
    'right_elbow': [0.5, 0.8],
    'left_hand': [-0.5, 0.4],
    'right_hand': [0.5, 0.4],
    'left_hip': [-0.2, 0.2],
    'right_hip': [0.2, 0.2],
    'left_knee': [-0.2, -0.2],
    'right_knee': [0.2, -0.2],
    'left_ankle': [-0.2, -0.6],
    'right_ankle': [0.2, -0.6],
    'left_foot': [-0.2, -0.8],
    'right_foot': [0.2, -0.8]
}

# Define the connections between the points
connections = [
    ['head', 'left_shoulder'],
    ['head', 'right_shoulder'],
    ['left_shoulder', 'left_elbow'],
    ['right_shoulder', 'right_elbow'],
    ['left_elbow', 'left_hand'],
    ['right_elbow', 'right_hand'],
    ['left_shoulder', 'left_hip'],
    ['right_shoulder', 'right_hip'],
    ['left_hip', 'left_knee'],
    ['right_hip', 'right_knee'],
    ['left_knee', 'left_ankle'],
    ['right_knee', 'right_ankle'],
    ['left_ankle', 'left_foot'],
    ['right_ankle', 'right_foot']
]

# Define the movement of the points
def move_points(frame):
    moved_points = points.copy()
    
    # Move the legs
    moved_points['left_knee'][1] = -0.2 + np.sin(frame / 10.0) * 0.2
    moved_points['right_knee'][1] = -0.2 - np.sin(frame / 10.0) * 0.2
    moved_points['left_ankle'][1] = -0.6 + np.sin(frame / 10.0) * 0.2
    moved_points['right_ankle'][1] = -0.6 - np.sin(frame / 10.0) * 0.2
    moved_points['left_foot'][1] = -0.8 + np.sin(frame / 10.0) * 0.2
    moved_points['right_foot'][1] = -0.8 - np.sin(frame / 10.0) * 0.2
    
    # Move the arms
    moved_points['left_elbow'][1] = 0.8 + np.sin(frame / 10.0) * 0.2
    moved_points['right_elbow'][1] = 0.8 - np.sin(frame / 10.0) * 0.2
    moved_points['left_hand'][1] = 0.4 + np.sin(frame / 10.0) * 0.2
    moved_points['right_hand'][1] = 0.4 - np.sin(frame / 10.0) * 0.2
    
    return moved_points

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter([points[p][0] for p in points], [points[p][1] for p in points], s=10, c='white')

# Create the lines
lines = []
for connection in connections:
    line, = ax.plot([points[connection[0]][0], points[connection[1]][0]], [points[connection[0]][1], points[connection[1]][1]], c='white')
    lines.append(line)

# Animation function
def animate(frame):
    moved_points = move_points(frame)
    scatter.set_offsets([[moved_points[p][0], moved_points[p][1]] for p in moved_points])
    for i, connection in enumerate(connections):
        lines[i].set_data([moved_points[connection[0]][0], moved_points[connection[1]][0]], [moved_points[connection[0]][1], moved_points[connection[1]][1]])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
