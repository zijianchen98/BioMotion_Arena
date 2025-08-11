
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights representing the sadman sitting down
initial_positions = {
    'head': np.array([0.5, 0.7]),
    'left_shoulder': np.array([0.4, 0.6]),
    'right_shoulder': np.array([0.6, 0.6]),
    'left_elbow': np.array([0.3, 0.5]),
    'right_elbow': np.array([0.7, 0.5]),
    'left_wrist': np.array([0.2, 0.4]),
    'right_wrist': np.array([0.8, 0.4]),
    'left_hip': np.array([0.4, 0.4]),
    'right_hip': np.array([0.6, 0.4]),
    'left_knee': np.array([0.4, 0.3]),
    'right_knee': np.array([0.6, 0.3]),
    'left_ankle': np.array([0.4, 0.2]),
    'right_ankle': np.array([0.6, 0.2]),
    'left_foot': np.array([0.35, 0.1]),
    'right_foot': np.array([0.65, 0.1])
}

# Function to simulate the motion of sitting down
def sit_down(t):
    positions = initial_positions.copy()
    # Simulate the head lowering
    positions['head'] -= np.array([0, t * 0.05])
    # Simulate shoulders moving slightly forward
    positions['left_shoulder'] += np.array([t * 0.02, -t * 0.02])
    positions['right_shoulder'] += np.array([-t * 0.02, -t * 0.02])
    # Simulate arms bending at the elbows
    positions['left_elbow'] += np.array([-t * 0.02, -t * 0.05])
    positions['right_elbow'] += np.array([t * 0.02, -t * 0.05])
    # Simulate hands moving down
    positions['left_wrist'] += np.array([-t * 0.02, -t * 0.08])
    positions['right_wrist'] += np.array([t * 0.02, -t * 0.08])
    # Simulate hips lowering
    positions['left_hip'] -= np.array([0, t * 0.05])
    positions['right_hip'] -= np.array([0, t * 0.05])
    # Simulate knees bending
    positions['left_knee'] -= np.array([0, t * 0.1])
    positions['right_knee'] -= np.array([0, t * 0.1])
    # Simulate ankles lowering
    positions['left_ankle'] -= np.array([0, t * 0.1])
    positions['right_ankle'] -= np.array([0, t * 0.1])
    # Simulate feet moving slightly outwards
    positions['left_foot'] += np.array([-t * 0.02, 0])
    positions['right_foot'] += np.array([t * 0.02, 0])
    
    return list(positions.values())

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

points, = ax.plot([], [], 'wo', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    x, y = zip(*sit_down(i / 20))
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, animate, frames=range(20), init_func=init, blit=True, interval=100)

plt.show()
