
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
FIGSIZE = (8, 6)

# Create figure and axis
fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points (simplified model of a running person)
# These coordinates are just a starting point and need refinement for realism
initial_positions = np.array([
    [0.0, 0.0],  # Head
    [-0.1, 0.4], # Left Shoulder
    [0.1, 0.4],  # Right Shoulder
    [-0.15, 0.6],# Left Elbow
    [0.15, 0.6], # Right Elbow
    [-0.2, 0.8], # Left Hand
    [0.2, 0.8],  # Right Hand
    [0.0, 0.2],  # Chest
    [0.0, -0.2], # Waist
    [-0.2, -0.4],# Left Hip
    [0.2, -0.4], # Right Hip
    [-0.3, -0.6],# Left Knee
    [0.3, -0.6], # Right Knee
    [-0.2, -0.8],# Left Foot
    [0.2, -0.8]  # Right Foot
])

# Create scatter plot for the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / FPS
    positions = initial_positions.copy()

    # Simple sinusoidal motion for running
    phase_shift = np.linspace(0, 2 * np.pi, NUM_POINTS)
    amplitude = 0.1
    frequency = 1.5

    # Adjust y positions for running motion
    positions[:, 1] += amplitude * np.sin(frequency * t + phase_shift)

    # Adjust x positions for running motion
    positions[:, 0] += 0.1 * np.sin(frequency * t + phase_shift[::2])

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=int(FPS * DURATION), init_func=init, blit=True, repeat=True)

plt.show()
