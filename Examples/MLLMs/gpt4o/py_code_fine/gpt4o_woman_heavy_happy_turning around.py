
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_rotation_angles(frames, rotation_speed=360):
    """
    Generate rotation angles for the body over a given number of animation frames.
    """
    return np.linspace(0, rotation_speed, frames)

def generate_biological_motion_pattern(rotation_angle):
    """
    Generate coordinates for point-lights based on the current rotation angle.
    The structure follows a biomechanically plausible human body with point-lights.
    """
    # Define the initial positions of the joints in the body (15 points)
    body_points = np.array([
        [0, 5],    # Head
        [-1, 4], [1, 4],  # Shoulders
        [-1, 3], [1, 3],  # Elbows
        [-1, 2], [1, 2],  # Wrists
        [0, 3],    # Torso (spine point)
        [-1, 1], [1, 1],  # Hips
        [-1, 0], [1, 0],  # Knees
        [-1, -1], [1, -1], # Ankles
        [0, -2]   # Feet
    ])

    # Rotation matrix to simulate turning
    theta = np.radians(rotation_angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    # Apply rotation matrix to the points
    rotated_body_points = np.dot(body_points, rotation_matrix.T)
    return rotated_body_points

def animate(i):
    global rotation_angles
    rotating_points = generate_biological_motion_pattern(rotation_angles[i])
    scatter.set_offsets(rotating_points)

# Animation settings
frames = 100  # Number of frames in the animation
rotation_angles = generate_rotation_angles(frames)

# Plot settings
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_facecolor('black')  # Solid black background
scatter = ax.scatter([], [], color="white", marker="o", s=50)

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=100)

plt.show()
