
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_lights = 15
frames = 100
duration = 5  # seconds

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # white points

# Initial positions (assuming a 'bowing' configuration)
initial_positions = np.array([
    [0, 8],  # head
    [-2, 6], [0, 6], [2, 6],  # shoulders
    [-3, 4], [-1, 4], [1, 4], [3, 4],  # arms
    [-2, 2], [0, 2], [2, 2],  # chest
    [-2, 0], [0, 0], [2, 0],  # hips
    [0, -2], [0, -4]  # legs
])

# For bowing action, generate points positions in a 'bowing' style
def get_bowing_positions(frame):
    stage = frame / frames
    positions = initial_positions.copy()
    
    # Simulate bowing movement
    for i in range(len(positions)):
        if i == 0:  # head goes down
            positions[i][1] -= stage * 5
        elif i < 4:  # shoulders
            positions[i][1] -= stage * 4
        elif i < 8:  # arms
            positions[i][1] -= stage * 3
        elif i < 12:  # chest
            positions[i][1] -= stage * 2
        elif i < 14:  # hips
            positions[i][1] -= stage * 1
        else:  # legs
            positions[i][1] -= stage * 1
    
    return positions

# Animation update function
def update(frame):
    positions = get_bowing_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/30, blit=True)

# Show animation
plt.show()
