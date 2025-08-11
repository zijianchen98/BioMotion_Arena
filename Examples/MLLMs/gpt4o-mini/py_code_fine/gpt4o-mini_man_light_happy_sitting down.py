
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
frames = 100
fps = 30
duration = frames / fps

# Initialize positions for point lights representing a happy man sitting down
# The positions are manually defined for a sitting down action
# Each light corresponds to a body part

# Set initial positions (x, y)
initial_positions = np.array([
    [0, 2],   # Head
    [-1, 1.5], [1, 1.5],  # Shoulders
    [-1, 1], [0, 1], [1, 1],  # Elbows
    [-0.5, 0], [0, 0], [0.5, 0],  # Hips
    [-1, -1], [1, -1],  # Thighs
    [-0.5, -2], [0, -2], [0.5, -2],  # Knees
    [0, -3]   # Feet
])

# Define a simple sitting motion
def sitting_motion(frame):
    # Animation of sitting direction movement
    new_positions = initial_positions.copy()
    
    # Modifying Y positions for motion (Simulate smooth sitting)
    # Frame manipulation
    if frame < frames // 2:
        new_positions[:, 1] -= frame * 0.02  # Slight downward motion
    else:
        new_positions[:, 1] -= (frames-frame) * 0.02  # Return upward motion

    return new_positions.T  # Return transposed

# Create animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    positions = sitting_motion(frame)
    points.set_data(positions[0], positions[1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init,
                              blit=True, repeat=True, interval=1000/fps)

plt.show()
