
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 joint positions in a canonical "sad" posture (in meters)
joints_3d = np.array([
    [ 0.0, 1.80,  0.0],  # head top
    [ 0.0, 1.60,  0.0],  # neck
    [-0.20, 1.50,  0.00],  # left shoulder
    [ 0.20, 1.50,  0.00],  # right shoulder
    [-0.40, 1.20,  0.00],  # left elbow
    [ 0.40, 1.20,  0.00],  # right elbow
    [-0.50, 0.90,  0.00],  # left wrist
    [ 0.50, 0.90,  0.00],  # right wrist
    [ 0.00, 1.10,  0.00],  # navel
    [-0.20, 1.00,  0.00],  # left hip
    [ 0.20, 1.00,  0.00],  # right hip
    [-0.20, 0.60,  0.00],  # left knee
    [ 0.20, 0.60,  0.00],  # right knee
    [-0.20, 0.10,  0.00],  # left ankle
    [ 0.20, 0.10,  0.00],  # right ankle
])

# Animation parameters
frames = 240         # total number of frames
fps = 30             # frames per second
rotation_speed = 2 * np.pi / frames  # full 360° over all frames
scale = 250          # scale factor for projection
width, height = 600, 600

# Set up the figure and axis
fig = plt.figure(figsize=(6,6), facecolor='black')
ax = plt.axes(xlim=(0, width), ylim=(0, height))
ax.set_facecolor('black')
ax.axis('off')

# Initialize scatter plot for the 15 points
scatter = ax.scatter([], [], s=60, c='white')

def orthographic_project(points3d, theta):
    """
    Rotate the 3D points around the Y-axis by angle theta,
    then do an orthographic projection onto the XY-plane,
    scale and translate to screen coordinates.
    """
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    # Rotation matrix around Y-axis
    R = np.array([
        [ cos_t, 0, sin_t],
        [     0, 1,     0],
        [-sin_t, 0, cos_t]
    ])
    rotated = points3d.dot(R.T)
    # Orthographic projection: drop the Z coordinate
    proj_x = rotated[:,0]
    proj_y = rotated[:,1]
    # Scale and center
    screen_x = proj_x * scale + width / 2
    screen_y = proj_y * scale + height / 8   # lift up a bit
    return np.vstack([screen_x, screen_y]).T

def init():
    scatter.set_offsets([])
    return scatter,

def animate(frame):
    theta = rotation_speed * frame
    pts2d = orthographic_project(joints_3d, theta)
    scatter.set_offsets(pts2d)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=frames, interval=1000/fps, blit=True
)

# Display the animation
plt.show()
