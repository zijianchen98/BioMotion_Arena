
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 400  # milliseconds
frames = 100

# Point-Light Positions
# These are loosely inspired positions for a simplified 'lie down' pose
points_initial = np.array([
    [0, 5],   # Head
    [-1, 4],  # Left shoulder
    [1, 4],   # Right shoulder
    [-1, 3],  # Left elbow
    [1, 3],   # Right elbow
    [-0.5, 2], # Left wrist
    [0.5, 2],  # Right wrist
    [-1, 1],  # Left hip
    [1, 1],   # Right hip
    [-1, 0],  # Left knee
    [1, 0],   # Right knee
    [-0.5, -1], # Left ankle
    [0.5, -1],  # Right ankle
    [0, -3],  # Pelvis
    [0, 4],   # Center of mass
    [0, 0]    # Center point for realism
])

# Movement function: a slight bobbing motion for realism
def update_points(t):
    bobbing = 0.2 * np.sin(t / 10)
    return points_initial + np.array([[0, bobbing]] * num_points)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Animation function
def animate(i):
    new_positions = update_points(i)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Setup the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=duration/frames, blit=True)

# Show the animation
plt.show()
