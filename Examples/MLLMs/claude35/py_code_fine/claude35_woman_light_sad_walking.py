
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Generate points for a basic human figure (15 points representing joints)
def init_points():
    return np.array([
        [0, 2],   # Head
        [-0.5, 1.5],   # Left Shoulder
        [0.5, 1.5],   # Right Shoulder
        [-0.5, 1],   # Left Elbow
        [0.5, 1],   # Right Elbow
        [-0.5, 0.5],   # Left Wrist
        [0.5, 0.5],   # Right Wrist
        [-0.5, 0],   # Left Hip
        [0.5, 0],   # Right Hip
        [-1, -1],   # Left Knee
        [1, -1],    # Right Knee
        [-1.5, -2], # Left Ankle
        [1.5, -2],  # Right Ankle
        [0, -2],    # Torso Bottom
        [0, 0]      # Torso Top
    ])

points = init_points()
scatters = [ax.plot([], [], 'o', color='white')[0] for _ in range(points.shape[0])]

# Walking motion parameters
frames = 100
step_size = 0.05  # Adjust step size for walking
walk_cycle = 0.25  # Duration of one walking cycle

# Animation function
def animate(i):
    t = i / frames * 2 * np.pi  # Normalized time
    # Adjust points position to simulate walking motion
    sway = np.sin(3 * t) * 0.1
    
    # Update points' y-coordinates to simulate walking
    points[:, 0] += step_size * np.sin(t)  # Horizontal movement
    points[:, 1] += sway  # Vertical sway
    points[1, 1] += sway  # Adjust left shoulder/sway
    points[2, 1] += sway  # Adjust right shoulder/sway
    
    # Update scatter plot points
    for scatter, point in zip(scatters, points):
        scatter.set_data(point[0], point[1])
        
    return scatters

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
