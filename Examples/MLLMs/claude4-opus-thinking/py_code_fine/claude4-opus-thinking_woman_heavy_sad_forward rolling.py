
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Define Parameters**
num_points = 15  # Total point lights
frames = 100  # Total frames in the animation
duration = 5  # Duration of the animation in seconds
fps = frames / duration  # Frames per second
background_color = 'black'
point_color = 'white'

# **Define Point-Light Positions**
# Initial positions of the points representing joints: head, shoulders, hips, knees, and feet
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.5],  # Left Shoulder
    [0.5, 0.5],   # Right Shoulder
    [-0.3, 0.2],  # Left Hip
    [0.3, 0.2],   # Right Hip
    [-0.4, 0],    # Left Knee
    [0.4, 0],     # Right Knee
    [-0.5, -0.5], # Left Foot
    [0.5, -0.5],  # Right Foot
    [0, 0],       # Center of the body
    [-0.2, 0.5],  # Additional points for smooth motion
    [0.2, 0.5],
    [-0.2, 0.2],
    [0.2, 0.2],
    [-0.3, -0.2],
    [0.3, -0.2],
])

# **Define Forward Rolling Motion**
def update_positions(frame):
    # Simulate forward rolling motion by changing the y-coordinates over frames
    theta = (frame / frames) * np.pi  # Calculate angle
    rolling_distance = np.sin(theta) * 0.5  # Simulate rolling
    
    # Update y-coordinates to represent the rolling action and some downward motion
    positions = initial_positions.copy()
    positions[:, 1] -= rolling_distance  # Modify y values to roll forward
    positions[:, 0] += np.sin(theta) * 0.1  # Small lateral movement for realism
    return positions

# **Set up the Plot**
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor(background_color)
points, = ax.plot([], [], 'o', color=point_color)

# **Initialization Function**
def init():
    points.set_data([], [])
    return points,

# **Animation Update Function**
def animate(frame):
    positions = update_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# **Create the Animation**
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000/fps, blit=True)

# **Show the Animation**
plt.show()
