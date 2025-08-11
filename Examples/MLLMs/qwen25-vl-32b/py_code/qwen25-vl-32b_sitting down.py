
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points representing the human figure
initial_positions = {
    "head": [0, 1],
    "torso": [0, 0],
    "left_shoulder": [-0.5, 0.5],
    "right_shoulder": [0.5, 0.5],
    "left_elbow": [-1, 0.25],
    "right_elbow": [1, 0.25],
    "left_wrist": [-1.5, -0.25],
    "right_wrist": [1.5, -0.25],
    "left_hip": [-0.5, -0.5],
    "right_hip": [0.5, -0.5],
    "left_knee": [-1, -1],
    "right_knee": [1, -1],
    "left_ankle": [-1.5, -1.5],
    "right_ankle": [1.5, -1.5],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the animation parameters
num_frames = 100  # Number of frames in the animation
fps = 24  # Frames per second

# Define the motion trajectory for sitting down
def get_sitting_motion(frame):
    """
    This function defines the motion of each point over time.
    The motion is designed to simulate a person sitting down smoothly.
    """
    t = frame / num_frames  # Normalized time (0 to 1)
    
    # Define the motion for each body part
    head = initial_positions["head"]
    torso = np.array([0, -t])  # Torso moves downward
    left_shoulder = np.array([-0.5, 0.5 - t])
    right_shoulder = np.array([0.5, 0.5 - t])
    left_elbow = np.array([-1, 0.25 - t])
    right_elbow = np.array([1, 0.25 - t])
    left_wrist = np.array([-1.5, -0.25 - t])
    right_wrist = np.array([1.5, -0.25 - t])
    left_hip = np.array([-0.5, -0.5 - t * 2])  # Hip moves faster downward
    right_hip = np.array([0.5, -0.5 - t * 2])
    left_knee = np.array([-1, -1 - t * 2])
    right_knee = np.array([1, -1 - t * 2])
    left_ankle = np.array([-1.5, -1.5 - t * 2])
    right_ankle = np.array([1.5, -1.5 - t * 2])
    
    # Combine all points into a single array
    coords = np.array([
        head,
        torso,
        left_shoulder,
        right_shoulder,
        left_elbow,
        right_elbow,
        left_wrist,
        right_wrist,
        left_hip,
        right_hip,
        left_knee,
        right_knee,
        left_ankle,
        right_ankle,
    ])
    
    return coords

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look
points = ax.scatter([], [], s=50, c='white')  # White points on black background

# Animation update function
def update(frame):
    coords = get_sitting_motion(frame)
    points.set_offsets(coords)
    return points,

# Create the animation
animation = FuncAnimation(
    fig,
    update,
    frames=np.arange(num_frames),
    interval=1000 / fps,  # Duration of each frame in milliseconds
    blit=True,
)

# Display the animation
plt.show()
