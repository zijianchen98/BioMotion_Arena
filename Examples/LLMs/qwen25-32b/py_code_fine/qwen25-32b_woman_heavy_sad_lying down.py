
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights representing the sadwoman lying down
initial_positions = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.6],  # Left Shoulder
    [0.6, 0.6],  # Right Shoulder
    [0.35, 0.7], # Left Elbow
    [0.65, 0.7], # Right Elbow
    [0.3, 0.8],  # Left Hand
    [0.7, 0.8],  # Right Hand
    [0.5, 0.4],  # Hip
    [0.4, 0.3],  # Left Knee
    [0.6, 0.3],  # Right Knee
    [0.35, 0.2], # Left Foot
    [0.65, 0.2], # Right Foot
    [0.45, 0.5], # Left Hip
    [0.55, 0.5], # Right Hip
    [0.5, 0.55]  # Chest
])

# Function to simulate a lying down motion
def lying_down_motion(t):
    amplitude = 0.05
    frequency = 0.5
    phase_shifts = np.random.uniform(-np.pi, np.pi, size=(15,))
    
    oscillations = amplitude * np.sin(frequency * t + phase_shifts)
    oscillations[5:9] *= 0.5  # Reduce hand and hip movements
    oscillations[9:] *= 0.2   # Further reduce foot movements
    
    return oscillations.reshape((-1, 1))

# Setup the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Update function for the animation
def update(frame):
    oscillations = lying_down_motion(frame / 10.0)
    new_positions = initial_positions + oscillations
    scat.set_offsets(new_positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
