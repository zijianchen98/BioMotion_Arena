
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights representing a lying down sadwoman
initial_positions = np.array([
    [0.4, 0.8], [0.6, 0.8], [0.5, 0.9], # head
    [0.3, 0.7], [0.7, 0.7],              # shoulders
    [0.2, 0.5], [0.8, 0.5],              # hips
    [0.3, 0.3], [0.7, 0.3],              # knees
    [0.2, 0.1], [0.8, 0.1]               # feet
])

# Define the movement pattern for each joint (simplified)
def update_positions(frame, points):
    amplitude = 0.05
    frequency = 0.1
    phase_shift = frame * 0.05
    
    for i in range(points.shape[0]):
        if i in [0, 1]:  # Head nodding
            points[i][1] += amplitude * np.sin(frame * frequency + phase_shift)
        elif i in [2]:   # Head side-to-side
            points[i][0] += amplitude * np.cos(frame * frequency + phase_shift)
        elif i in [3, 4]: # Shoulder heaving
            points[i][1] -= amplitude * np.sin(frame * frequency + phase_shift)
        elif i in [5, 6]: # Hip lifting
            points[i][1] += amplitude * np.sin(frame * frequency + phase_shift)
        elif i in [7, 8]: # Knee bending
            points[i][1] += amplitude * np.sin(frame * frequency + phase_shift)
        elif i in [9, 10]: # Foot wiggling
            points[i][0] += amplitude * np.cos(frame * frequency + phase_shift)
            
    return points

# Create the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Update function for the animation
def animate(frame):
    updated_positions = update_positions(frame, initial_positions.copy())
    scat.set_offsets(updated_positions)

# Generate the animation
animation = FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
