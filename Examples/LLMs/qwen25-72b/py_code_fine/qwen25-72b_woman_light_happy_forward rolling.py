
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a forward roll
key_points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_hand',
    'left_shoulder', 'left_elbow', 'left_hand', 'spine', 'hip',
    'right_knee', 'right_ankle', 'left_knee', 'left_ankle', 'center_of_mass'
]

# Define the initial positions of the key points
initial_positions = {
    'head': [0, 1.5, 0],
    'neck': [0, 1.4, 0],
    'right_shoulder': [0.1, 1.3, -0.1],
    'right_elbow': [0.2, 1.2, -0.2],
    'right_hand': [0.3, 1.1, -0.3],
    'left_shoulder': [-0.1, 1.3, 0.1],
    'left_elbow': [-0.2, 1.2, 0.2],
    'left_hand': [-0.3, 1.1, 0.3],
    'spine': [0, 1.0, 0],
    'hip': [0, 0.8, 0],
    'right_knee': [0.1, 0.6, -0.1],
    'right_ankle': [0.2, 0.4, -0.2],
    'left_knee': [-0.1, 0.6, 0.1],
    'left_ankle': [-0.2, 0.4, 0.2],
    'center_of_mass': [0, 0.9, 0]
}

# Define the forward roll animation frames
def forward_roll(t):
    angle = t * np.pi / 2  # Roll angle
    positions = {}
    for key in key_points:
        x, y, z = initial_positions[key]
        new_x = x * np.cos(angle) - z * np.sin(angle)
        new_z = x * np.sin(angle) + z * np.cos(angle)
        positions[key] = [new_x, y, new_z]
    return positions

# Create the figure and axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d([-2, 2])
ax.set_ylim3d([0, 2])
ax.set_zlim3d([-2, 2])
ax.set_facecolor('black')
ax.set_axis_off()

# Initialize the scatter plot
scat = ax.scatter([], [], [], color='white')

# Update function for the animation
def update(frame):
    positions = forward_roll(frame / 100)
    x = [positions[key][0] for key in key_points]
    y = [positions[key][1] for key in key_points]
    z = [positions[key][2] for key in key_points]
    scat._offsets3d = (x, y, z)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()
