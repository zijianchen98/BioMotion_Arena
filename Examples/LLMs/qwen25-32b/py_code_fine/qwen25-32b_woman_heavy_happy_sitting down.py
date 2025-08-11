
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.5, 0.9], [0.4, 0.8], [0.6, 0.8],  # Head
    [0.3, 0.7], [0.7, 0.7],               # Shoulders
    [0.2, 0.6], [0.8, 0.6],               # Hips
    [0.1, 0.5], [0.9, 0.5],               # Knees
    [0.0, 0.4], [1.0, 0.4],               # Feet
    [0.4, 0.5], [0.6, 0.5],               # Hands
    [0.3, 0.4], [0.7, 0.4]                # Elbows
])

# Define the path for sitting down motion
def sitting_down_motion(t):
    """
    Returns the vertical displacement of each point-light based on time t.
    """
    amplitude = 0.1 * np.sin(np.pi * t / 10)
    displacement = np.zeros((15, 2))
    displacement[:, 1] = -amplitude
    return displacement

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look

points, = ax.plot([], [], 'wo', markersize=5)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    displacement = sitting_down_motion(frame)
    new_positions = initial_positions + displacement
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 100),
                    init_func=init, blit=True, interval=50)

plt.show()
