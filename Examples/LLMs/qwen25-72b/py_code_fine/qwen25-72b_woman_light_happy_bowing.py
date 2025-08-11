
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a woman's body
key_points = [
    "head", "neck", "right_shoulder", "right_elbow", "right_wrist",
    "left_shoulder", "left_elbow", "left_wrist", "hip", "right_knee",
    "right_ankle", "left_knee", "left_ankle", "right_hand", "left_hand"
]

# Define initial positions for the key points
initial_positions = {
    "head": [0, 1.5],
    "neck": [0, 1.0],
    "right_shoulder": [-0.5, 0.8],
    "right_elbow": [-0.7, 0.4],
    "right_wrist": [-0.9, 0.1],
    "left_shoulder": [0.5, 0.8],
    "left_elbow": [0.7, 0.4],
    "left_wrist": [0.9, 0.1],
    "hip": [0, -0.5],
    "right_knee": [-0.3, -1.0],
    "right_ankle": [-0.4, -1.5],
    "left_knee": [0.3, -1.0],
    "left_ankle": [0.4, -1.5],
    "right_hand": [-0.9, 0.1],
    "left_hand": [0.9, 0.1]
}

# Define the bowing motion
def bowing(t):
    angle = np.radians(30 * np.sin(2 * np.pi * t / 2))
    positions = {key: np.array(initial_positions[key]) for key in key_points}
    
    # Rotate the upper body
    for key in ["head", "neck", "right_shoulder", "right_elbow", "right_wrist", "left_shoulder", "left_elbow", "left_wrist"]:
        positions[key] = rotate_point(positions[key], angle)
    
    return positions

def rotate_point(point, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(rotation_matrix, point)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter([], [], s=100, color='white')

# Update function for the animation
def update(frame):
    positions = bowing(frame)
    x = [positions[key][0] for key in key_points]
    y = [positions[key][1] for key in key_points]
    scat.set_offsets(np.column_stack((x, y)))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2, 100), interval=50, repeat=True)

# Show the animation
plt.show()
