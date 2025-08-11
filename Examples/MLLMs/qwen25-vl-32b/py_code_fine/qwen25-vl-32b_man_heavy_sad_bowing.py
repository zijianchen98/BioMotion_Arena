
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, -0.5],
    'right_shoulder': [0.5, -0.5],
    'left_elbow': [-1, -1],
    'right_elbow': [1, -1],
    'left_wrist': [-1.5, -1.5],
    'right_wrist': [1.5, -1.5],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-1, -2.5],
    'right_knee': [1, -2.5],
    'left_ankle': [-1.5, -3.5],
    'right_ankle': [1.5, -3.5],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array([
    initial_positions['head'],
    initial_positions['torso'],
    initial_positions['left_shoulder'],
    initial_positions['right_shoulder'],
    initial_positions['left_elbow'],
    initial_positions['right_elbow'],
    initial_positions['left_wrist'],
    initial_positions['right_wrist'],
    initial_positions['left_hip'],
    initial_positions['right_hip'],
    initial_positions['left_knee'],
    initial_positions['right_knee'],
    initial_positions['left_ankle'],
    initial_positions['right_ankle'],
])

# Define the final positions for the "bowing" pose
final_positions = {
    'head': [0, 0.5],  # Head slightly lowered
    'torso': [0, -0.5],  # Torso bent forward
    'left_shoulder': [-0.5, -1],  # Shoulders shifted back
    'right_shoulder': [0.5, -1],
    'left_elbow': [-1, -1.5],  # Arms hanging down
    'right_elbow': [1, -1.5],
    'left_wrist': [-1.5, -2],  # Hands dangling
    'right_wrist': [1.5, -2],
    'left_hip': [-0.5, -2],  # Hips shifted back
    'right_hip': [0.5, -2],
    'left_knee': [-1, -3],  # Legs slightly bent
    'right_knee': [1, -3],
    'left_ankle': [-1.5, -4],  # Feet on the ground
    'right_ankle': [1.5, -4],
}

# Convert the final positions to a list of coordinates
final_coords = np.array([
    final_positions['head'],
    final_positions['torso'],
    final_positions['left_shoulder'],
    final_positions['right_shoulder'],
    final_positions['left_elbow'],
    final_positions['right_elbow'],
    final_positions['left_wrist'],
    final_positions['right_wrist'],
    final_positions['left_hip'],
    final_positions['right_hip'],
    final_positions['left_knee'],
    final_positions['right_knee'],
    final_positions['left_ankle'],
    final_positions['right_ankle'],
])

# Interpolate between initial and final positions
num_frames = 60  # Number of frames in the animation
interpolated_coords = []
for t in np.linspace(0, 1, num_frames):
    interpolated_coords.append(
        (1 - t) * initial_coords + t * final_coords
    )

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    coords = interpolated_coords[frame]
    scat.set_offsets(coords)
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50
)

# Display the animation
plt.show()
