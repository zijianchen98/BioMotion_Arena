
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights representing the sadwoman
initial_positions = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.6],  # Left Shoulder
    [0.6, 0.6],  # Right Shoulder
    [0.3, 0.7],  # Left Elbow
    [0.7, 0.7],  # Right Elbow
    [0.2, 0.8],  # Left Hand
    [0.8, 0.8],  # Right Hand
    [0.4, 0.4],  # Left Hip
    [0.6, 0.4],  # Right Hip
    [0.3, 0.3],  # Left Knee
    [0.7, 0.3],  # Right Knee
    [0.2, 0.2],  # Left Foot
    [0.8, 0.2],  # Right Foot
    [0.5, 0.6],  # Chest
    [0.5, 0.3]   # Waist
])

# Function to simulate forward rolling motion
def forward_roll(t):
    amplitude = 0.3
    frequency = 0.05
    phase_shifts = np.linspace(0, 2 * np.pi, len(initial_positions))
    new_positions = initial_positions.copy()
    for i in range(len(new_positions)):
        angle = t * frequency + phase_shifts[i]
        displacement = amplitude * np.sin(angle)
        new_positions[i][0] += displacement
        new_positions[i][1] -= displacement
    return new_positions

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
points, = ax.plot([], [], 'wo', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    x, y = forward_roll(i).T
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, animate, frames=np.arange(0, 100), init_func=init, blit=True, interval=40)
plt.show()
