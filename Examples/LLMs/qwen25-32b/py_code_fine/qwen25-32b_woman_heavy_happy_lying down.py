
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the body parts and their initial positions
body_parts = ['head', 'left_shoulder', 'right_shoulder', 'left_hip', 'right_hip', 'left_elbow', 'right_elbow',
              'left_knee', 'right_knee', 'left_wrist', 'right_wrist', 'left_ankle', 'right_ankle', 'left_toe', 'right_toe']
positions = np.array([
    [0, 0], [-0.5, -0.5], [0.5, -0.5], [-0.5, -1.5], [0.5, -1.5],
    [-1.0, -0.5], [1.0, -0.5], [-1.0, -1.5], [1.0, -1.5],
    [-1.5, -0.5], [1.5, -0.5], [-1.0, -2.5], [1.0, -2.5],
    [-1.0, -3.0], [1.0, -3.0]
])

# Create figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 1)
ax.axis('off')  # Hide axes

# Scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Function to update the position of the lights
def update(frame):
    global positions
    
    # Simulate the lying down motion by oscillating the body parts
    t = frame / 50.0  # Time in seconds
    amplitude = 0.1  # Amplitude of the oscillation
    
    # Oscillate the shoulders and hips
    positions[1:5] += np.array([amplitude * np.sin(2 * np.pi * t), amplitude * np.cos(2 * np.pi * t)]).T
    # Oscillate the elbows and knees
    positions[5:9] += np.array([amplitude * np.sin(2 * np.pi * t + np.pi/2), amplitude * np.cos(2 * np.pi * t + np.pi/2)]).T
    # Oscillate the wrists and ankles
    positions[9:13] += np.array([amplitude * np.sin(2 * np.pi * t + np.pi), amplitude * np.cos(2 * np.pi * t + np.pi)]).T
    # Oscillate the toes
    positions[13:] += np.array([amplitude * np.sin(2 * np.pi * t + 3*np.pi/2), amplitude * np.cos(2 * np.pi * t + 3*np.pi/2)]).T
    
    # Update scatter plot data
    scat.set_offsets(positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
