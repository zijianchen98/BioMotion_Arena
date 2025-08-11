
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create initial positions of points (15 points)
def init_positions():
    # Initial positions of the points for a sitting motion
    positions = np.array([
        [0, 2], [0.5, 2], [1, 2], [1.5, 2], [2, 2], # Head
        [0.5, 1], [1.5, 1], # Shoulders
        [0.25, 0], [0.75, 0], [1.25, 0], [1.75, 0], # Arms
        [1, -1], [1.5, -1], [1, -2], [1.5, -2], [1.25, -3] # Torso and legs
    ])
    return positions

# Function to update the positions of the points
def update_positions(i, points):
    amplitude = 0.2
    frequency = 0.05
    offset = 0.01 * i
    
    # Update positions based on simple sine wave for a smooth sit down motion
    for j in range(len(points)):
        if j < 5:  # Head points
            points[j] = [points[j][0], 2 - amplitude * np.sin(frequency * i + offset)]
        elif j < 7:  # Shoulders
            points[j] = [points[j][0], 1 - amplitude * np.sin(frequency * i + offset)]
        elif j < 11:  # Arms
            points[j] = [points[j][0], points[j][1] - amplitude * np.sin(frequency * i + offset)]
        else:  # Torso and legs
            points[j] = [points[j][0], points[j][1] - amplitude * np.sin(frequency * i + offset)]
    
    return points

# Initialize positions
points = init_positions()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 3)
ax.set_ylim(-4, 3)
ax.axis('off')

# Create scatter plot for initial positions
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

def animate(i):
    global points
    points = update_positions(i, points)
    scatter.set_offsets(points)

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

plt.show()
