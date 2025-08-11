
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Initial positions of the 15 point-lights
initial_positions = np.array([
    [5.0, 5.0], [4.5, 5.5], [5.5, 5.5], [4.0, 6.0], [6.0, 6.0], 
    [3.5, 6.5], [5.0, 6.5], [6.5, 6.5], [4.0, 7.0], [5.0, 7.0], 
    [6.0, 7.0], [4.5, 7.5], [5.5, 7.5], [5.0, 8.0], [4.0, 9.0]
])

# Scatter plot of point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white')

# Function to update the point-lights' positions
def update(frame):
    positions = initial_positions.copy()
    t = frame / 20.0  # Normalize frame to time
    
    # Define wave-like motion for a sad running animation
    amplitude = 0.3
    frequency = 0.1
    phase_shift = 0.5
    
    for i in range(len(positions)):
        positions[i, 0] = 5.0 + amplitude * np.sin(2 * np.pi * frequency * t + i * phase_shift)
        positions[i, 1] = initial_positions[i, 1] + amplitude * np.cos(2 * np.pi * frequency * t + i * phase_shift)
    
    points.set_offsets(positions)
    return points,

# Animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
