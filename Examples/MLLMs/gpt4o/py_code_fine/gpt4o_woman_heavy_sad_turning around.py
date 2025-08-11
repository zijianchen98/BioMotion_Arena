
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the motion data for a sad woman turning around.
def generate_biological_motion(frame_number):
    """
    This function simulates biomechanically plausible motion for an animation of a sad woman turning around.
    :param frame_number: The current frame number for the animation.
    :return: A 2D array of coordinates for the 15 point-lights.
    """
    t = frame_number / 60  # Normalize time based on frame number.
    pos = np.zeros((15, 2))

    # Coordinates for approximate points of the body part locations.
    # These consist of:
    # 1 head, 2 shoulders, 2 elbows, 2 wrists, 2 hips, 2 knees, 2 ankles, 2 feet.
    pos[0] = [0, 4 + np.sin(2 * np.pi * t) * 0.1]  # Head (slight bobbing motion)

    pos[1] = [-1, 3 + np.sin(2 * np.pi * t + np.pi / 6) * 0.1]  # Left shoulder
    pos[2] = [1, 3 + np.sin(2 * np.pi * t + np.pi / 6) * 0.1]   # Right shoulder

    pos[3] = [-0.6, 2.5 + np.sin(2 * np.pi * t + np.pi / 3) * 0.1]  # Left elbow
    pos[4] = [0.6, 2.5 + np.sin(2 * np.pi * t + np.pi / 3) * 0.1]   # Right elbow

    pos[5] = [-0.7, 2 + np.sin(2 * np.pi * t) * 0.1]  # Left wrist
    pos[6] = [0.7, 2 + np.sin(2 * np.pi * t) * 0.1]   # Right wrist

    pos[7] = [-0.7, 1 + np.sin(2 * np.pi * t) * 0.1]  # Left hip
    pos[8] = [0.7, 1 + np.sin(2 * np.pi * t) * 0.1]   # Right hip

    pos[9] = [-0.5, 0 + np.sin(2 * np.pi * t + np.pi / 3) * 0.1]  # Left knee
    pos[10] = [0.5, 0 + np.sin(2 * np.pi * t + np.pi / 3) * 0.1]  # Right knee

    pos[11] = [-0.5, -1 + np.sin(2 * np.pi * t) * 0.1]  # Left ankle
    pos[12] = [0.5, -1 + np.sin(2 * np.pi * t) * 0.1]   # Right ankle

    pos[13] = [-0.4, -1.2 + np.sin(2 * np.pi * t) * 0.1]  # Left foot
    pos[14] = [0.4, -1.2 + np.sin(2 * np.pi * t) * 0.1]   # Right foot

    # Rotate the entire group of points around the center of the image.
    angle = t * 2 * np.pi  # Rotation angle.
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    pos = np.dot(pos, rotation_matrix)
    
    return pos

# Create animation.
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)  # White point-lights.

def init():
    # Initialize the animation frame.
    points.set_data([], [])
    return points,

def update(frame):
    # Update the positions of point-lights for each frame.
    pos = generate_biological_motion(frame)
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=120, init_func=init, blit=True, interval=30)

plt.show()
