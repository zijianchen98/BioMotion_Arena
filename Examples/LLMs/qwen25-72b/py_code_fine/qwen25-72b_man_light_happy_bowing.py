
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for the happyman
key_points = [
    'head', 'neck', 'shoulder_left', 'elbow_left', 'wrist_left',
    'shoulder_right', 'elbow_right', 'wrist_right', 'hip_left',
    'knee_left', 'ankle_left', 'hip_right', 'knee_right', 'ankle_right', 'waist'
]

# Initial positions of the points
positions = {
    'head': [0, 1.5],
    'neck': [0, 1.0],
    'shoulder_left': [-0.5, 0.8],
    'elbow_left': [-0.7, 0.5],
    'wrist_left': [-0.9, 0.2],
    'shoulder_right': [0.5, 0.8],
    'elbow_right': [0.7, 0.5],
    'wrist_right': [0.9, 0.2],
    'hip_left': [-0.3, -0.2],
    'knee_left': [-0.4, -0.6],
    'ankle_left': [-0.5, -1.0],
    'hip_right': [0.3, -0.2],
    'knee_right': [0.4, -0.6],
    'ankle_right': [0.5, -1.0],
    'waist': [0, -0.4]
}

# Function to update the positions for the bowing animation
def update_positions(frame):
    angle = np.radians(15 * np.sin(2 * np.pi * frame / 60))
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    
    for key in positions:
        x, y = positions[key]
        if key != 'waist':
            new_x = (x - positions['waist'][0]) * cos_angle - (y - positions['waist'][1]) * sin_angle + positions['waist'][0]
            new_y = (x - positions['waist'][0]) * sin_angle + (y - positions['waist'][1]) * cos_angle + positions['waist'][1]
            positions[key] = [new_x, new_y]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Initialization function
def init():
    for point in points:
        point.set_data([], [])
    return points

# Animation update function
def animate(frame):
    update_positions(frame)
    for i, key in enumerate(key_points):
        x, y = positions[key]
        points[i].set_data(x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=120, interval=50, blit=True)

# Display the animation
plt.show()
