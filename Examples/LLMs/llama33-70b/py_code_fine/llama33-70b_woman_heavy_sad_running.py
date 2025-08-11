
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 points for the point-light stimulus
# Each point represents a joint or landmark on the body
points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_wrist',
    'left_shoulder', 'left_elbow', 'left_wrist', 'right_hip', 'right_knee',
    'right_ankle', 'left_hip', 'left_knee', 'left_ankle', 'torso'
]

# Define the initial positions of the points
# These positions will be used as the starting point for the animation
initial_positions = {
    'head': np.array([0, 10]),
    'neck': np.array([0, 8]),
    'right_shoulder': np.array([3, 6]),
    'right_elbow': np.array([5, 4]),
    'right_wrist': np.array([7, 2]),
    'left_shoulder': np.array([-3, 6]),
    'left_elbow': np.array([-5, 4]),
    'left_wrist': np.array([-7, 2]),
    'right_hip': np.array([2, 0]),
    'right_knee': np.array([3, -2]),
    'right_ankle': np.array([2, -4]),
    'left_hip': np.array([-2, 0]),
    'left_knee': np.array([-3, -2]),
    'left_ankle': np.array([-2, -4]),
    'torso': np.array([0, 2])
}

# Define the movement of each point over time
# This will be used to create the animation
def get_position(point, frame):
    position = initial_positions[point]
    
    # Simulate the movement of each point based on the action (running)
    if point == 'head':
        position[1] += np.sin(frame / 10.0) * 2
    elif point == 'neck':
        position[1] += np.sin(frame / 10.0) * 1.5
    elif point in ['right_shoulder', 'left_shoulder']:
        position[1] += np.sin(frame / 10.0) * 1
    elif point in ['right_elbow', 'left_elbow']:
        position[1] += np.sin(frame / 10.0) * 2
        position[0] += np.sin(frame / 5.0) * 1
    elif point in ['right_wrist', 'left_wrist']:
        position[1] += np.sin(frame / 10.0) * 3
        position[0] += np.sin(frame / 5.0) * 2
    elif point in ['right_hip', 'left_hip']:
        position[1] += np.sin(frame / 10.0) * 1
    elif point in ['right_knee', 'left_knee']:
        position[1] += np.sin(frame / 10.0) * 2
        position[0] += np.sin(frame / 5.0) * 1
    elif point in ['right_ankle', 'left_ankle']:
        position[1] += np.sin(frame / 10.0) * 3
        position[0] += np.sin(frame / 5.0) * 2
    elif point == 'torso':
        position[1] += np.sin(frame / 10.0) * 0.5
    
    return position

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

points_to_plot = []
for point in points:
    points_to_plot.append(ax.plot([], [], 'o', markersize=5, color='white')[0])

def animate(frame):
    for i, point in enumerate(points):
        position = get_position(point, frame)
        points_to_plot[i].set_data(position[0], position[1])
    return points_to_plot

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
