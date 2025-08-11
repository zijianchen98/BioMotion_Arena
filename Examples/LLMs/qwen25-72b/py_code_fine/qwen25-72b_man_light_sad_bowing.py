
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a simplified human figure
key_points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_hand',
    'left_shoulder', 'left_elbow', 'left_hand', 'hip', 'right_knee',
    'right_foot', 'left_knee', 'left_foot', 'right_hip', 'left_hip'
]

# Define initial positions of the key points
initial_positions = {
    'head': [0, 1.5],
    'neck': [0, 1.0],
    'right_shoulder': [-0.5, 0.8],
    'right_elbow': [-0.7, 0.6],
    'right_hand': [-0.9, 0.4],
    'left_shoulder': [0.5, 0.8],
    'left_elbow': [0.7, 0.6],
    'left_hand': [0.9, 0.4],
    'hip': [0, 0],
    'right_knee': [-0.3, -0.5],
    'right_foot': [-0.3, -1.0],
    'left_knee': [0.3, -0.5],
    'left_foot': [0.3, -1.0],
    'right_hip': [-0.2, 0],
    'left_hip': [0.2, 0]
}

# Define the bowing motion
def bow(t):
    angle = np.sin(t) * 0.3  # Bowing angle
    for key in initial_positions:
        x, y = initial_positions[key]
        if key in ['head', 'neck', 'right_shoulder', 'left_shoulder']:
            initial_positions[key] = [x * np.cos(angle) - y * np.sin(angle), x * np.sin(angle) + y * np.cos(angle)]
        else:
            initial_positions[key] = [x, y * (1 - angle)]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the point-lights
points = []
for _ in range(15):
    point, = ax.plot([], [], 'o', color='white')
    points.append(point)

# Update function for the animation
def update(frame):
    t = frame / 10.0  # Time in seconds
    bow(t)
    positions = [initial_positions[key] for key in key_points]
    for i, point in enumerate(points):
        point.set_data(positions[i])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(300), blit=True, repeat=True)

# Show the animation
plt.show()
