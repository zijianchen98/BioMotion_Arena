
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights for a lying-down posture
initial_positions = {
    'head': [0, 0],
    'neck': [0, -1],
    'torso': [0, -2],
    'pelvis': [0, -3],
    'left_shoulder': [-1, 0],
    'right_shoulder': [1, 0],
    'left_elbow': [-2, -1],
    'right_elbow': [2, -1],
    'left_wrist': [-3, -2],
    'right_wrist': [3, -2],
    'left_hip': [-1, -3],
    'right_hip': [1, -3],
    'left_knee': [-2, -4],
    'right_knee': [2, -4],
    'left_ankle': [-3, -5],
    'right_ankle': [3, -5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the animation parameters
num_frames = 100  # Number of frames in the animation
frame_rate = 30   # Frames per second
duration = num_frames / frame_rate  # Duration of the animation in seconds

# Define the motion trajectory for each point-light
def get_motion_trajectory(coords, amplitude=0.2, frequency=0.5):
    """
    Generate a sinusoidal motion trajectory for each point-light.
    """
    t = np.linspace(0, duration, num_frames)
    x_motion = amplitude * np.sin(2 * np.pi * frequency * t)
    y_motion = amplitude * np.cos(2 * np.pi * frequency * t)
    
    # Apply the motion to each coordinate
    trajectories = []
    for coord in coords:
        x, y = coord
        x_traj = x + x_motion
        y_traj = y + y_motion
        trajectories.append(np.column_stack((x_traj, y_traj)))
    return np.array(trajectories)

# Generate the motion trajectories
trajectories = get_motion_trajectory(initial_coords)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-6, 1)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

def init():
    """Initialize the scatter plot."""
    scat.set_offsets([])
    return scat,

def update(frame):
    """Update the scatter plot for each frame."""
    current_positions = trajectories[:, frame].reshape(-1, 2)
    scat.set_offsets(current_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_frames,
    init_func=init,
    blit=True,
    interval=1000 / frame_rate  # Interval between frames in milliseconds
)

# Display the animation
plt.show()

# Optionally, save the animation as a video file
# ani.save('sad_man_lying_down.mp4', fps=frame_rate, writer='ffmpeg')
