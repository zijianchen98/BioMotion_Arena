
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a sitting down action
key_points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_hand',
    'left_shoulder', 'left_elbow', 'left_hand', 'right_hip', 'right_knee',
    'right_foot', 'left_hip', 'left_knee', 'left_foot', 'pelvis'
]

# Define the initial positions of the key points
initial_positions = np.array([
    [0, 1.8],  # head
    [0, 1.6],  # neck
    [0.2, 1.5],  # right_shoulder
    [0.4, 1.3],  # right_elbow
    [0.6, 1.1],  # right_hand
    [-0.2, 1.5],  # left_shoulder
    [-0.4, 1.3],  # left_elbow
    [-0.6, 1.1],  # left_hand
    [0.2, 1.0],  # right_hip
    [0.2, 0.7],  # right_knee
    [0.2, 0.4],  # right_foot
    [-0.2, 1.0],  # left_hip
    [-0.2, 0.7],  # left_knee
    [-0.2, 0.4],  # left_foot
    [0, 1.0]  # pelvis
])

# Define the final positions of the key points after sitting down
final_positions = np.array([
    [0, 0.8],  # head
    [0, 0.6],  # neck
    [0.2, 0.5],  # right_shoulder
    [0.4, 0.4],  # right_elbow
    [0.6, 0.3],  # right_hand
    [-0.2, 0.5],  # left_shoulder
    [-0.4, 0.4],  # left_elbow
    [-0.6, 0.3],  # left_hand
    [0.2, 0.3],  # right_hip
    [0.2, 0.2],  # right_knee
    [0.2, 0.1],  # right_foot
    [-0.2, 0.3],  # left_hip
    [-0.2, 0.2],  # left_knee
    [-0.2, 0.1],  # left_foot
    [0, 0.3]  # pelvis
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
point_lights = [plt.plot([], [], 'o', color='white')[0] for _ in range(len(key_points))]

# Function to initialize the animation
def init():
    for light in point_lights:
        light.set_data([], [])
    return point_lights

# Function to update the animation
def update(frame):
    t = frame / frames  # Interpolation parameter
    for i, light in enumerate(point_lights):
        x = (1 - t) * initial_positions[i][0] + t * final_positions[i][0]
        y = (1 - t) * initial_positions[i][1] + t * final_positions[i][1]
        light.set_data(x, y)
    return point_lights

# Number of frames
frames = 100

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
