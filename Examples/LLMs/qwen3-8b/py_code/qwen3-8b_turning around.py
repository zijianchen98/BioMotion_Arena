
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 body points for a human turning around
body_points = {
    'head': np.array([0.0, 0.8]),
    'neck': np.array([0.0, 0.6]),
    'shoulder_left': np.array([-0.3, 0.4]),
    'elbow_left': np.array([-0.5, 0.2]),
    'wrist_left': np.array([-0.6, 0.0]),
    'hand_left': np.array([-0.5, -0.1]),
    'shoulder_right': np.array([0.3, 0.4]),
    'elbow_right': np.array([0.5, 0.2]),
    'wrist_right': np.array([0.6, 0.0]),
    'hand_right': np.array([0.5, -0.1]),
    'hip_left': np.array([-0.3, -0.4]),
    'knee_left': np.array([-0.5, -0.6]),
    'ankle_left': np.array([-0.6, -0.8]),
    'foot_left': np.array([-0.5, -0.9]),
    'hip_right': np.array([0.3, -0.4]),
    'knee_right': np.array([0.5, -0.6]),
    'ankle_right': np.array([0.6, -0.8]),
    'foot_right': np.array([0.5, -0.9]),
}

# Create circles for each point-light
circles = {name: Circle(point, 0.02, color='white') for name, point in body_points.items()}
for name, circle in circles.items():
    ax.add_patch(circle)

# Animation parameters
num_frames = 100
frame_duration = 50  # milliseconds

# Define the motion path for turning around
def animate(frame):
    angle = frame * 2 * np.pi / num_frames
    # Simulate a full turn around
    # Rotate the body around the origin
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    for name, point in body_points.items():
        body_points[name] = np.dot(rotation_matrix, point)
    # Update positions
    for name, circle in circles.items():
        circle.center = tuple(body_points[name])
    return circles.values()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=frame_duration, blit=True)

plt.show()
