
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights
NUM_LIGHTS = 15

# Define the motion parameters for a sad woman in a forward rolling motion
# These are simplified coordinates for a 3D motion projected to 2D
# This is a placeholder for realistic motion data, which would typically come from motion capture

def generate_motion_data(num_frames=100):
    # Generate smooth, biomechanically plausible motion data for a sad woman in a forward rolling motion
    # This is a simplified representation for demonstration purposes

    # Define key points (joints) of a human body
    joints = ['hips', 'spine', 'shoulder', 'elbow', 'wrist', 'hip_left', 'knee_left', 'ankle_left',
              'hip_right', 'knee_right', 'ankle_right', 'head', 'neck', 'shoulder_left', 'shoulder_right']

    # Generate smooth motion data for each joint
    motion_data = {joint: [] for joint in joints}

    for frame in range(num_frames):
        t = frame / num_frames
        # Simulate forward rolling motion with a slight sad posture
        # These are simplified and approximate values
        # You would replace this with actual motion capture data in a real scenario

        # Hips
        x = 0.0 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.1 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['hips'].append((x, y))

        # Spine
        x = 0.0 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.2 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['spine'].append((x, y))

        # Shoulder
        x = 0.1 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.3 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['shoulder'].append((x, y))

        # Elbow
        x = 0.1 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.4 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['elbow'].append((x, y))

        # Wrist
        x = 0.1 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.5 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['wrist'].append((x, y))

        # Hip left
        x = -0.05 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.1 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['hip_left'].append((x, y))

        # Knee left
        x = -0.05 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.2 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['knee_left'].append((x, y))

        # Ankle left
        x = -0.05 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.3 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['ankle_left'].append((x, y))

        # Hip right
        x = 0.05 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.1 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['hip_right'].append((x, y))

        # Knee right
        x = 0.05 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.2 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['knee_right'].append((x, y))

        # Ankle right
        x = 0.05 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.3 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['ankle_right'].append((x, y))

        # Head
        x = 0.0 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.1 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['head'].append((x, y))

        # Neck
        x = 0.0 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.0 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['neck'].append((x, y))

        # Shoulder left
        x = -0.1 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.3 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['shoulder_left'].append((x, y))

        # Shoulder right
        x = 0.1 + 0.1 * np.sin(2 * np.pi * t)
        y = -0.3 + 0.1 * np.cos(2 * np.pi * t)
        motion_data['shoulder_right'].append((x, y))

    # Interpolate the motion data to get smooth positions for each frame
    motion_data = {joint: np.array(motion_data[joint]) for joint in joints}

    # Generate point-light positions by sampling from the joints
    point_light_positions = []
    for _ in range(NUM_LIGHTS):
        # Randomly select a joint
        joint = np.random.choice(joints)
        # Sample a position from the joint's motion data
        frame_idx = np.random.randint(0, num_frames)
        x, y = motion_data[joint][frame_idx]
        point_light_positions.append((x, y))

    return point_light_positions

# Create the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Initialize the point lights
points = [Circle((0, 0), 0.02, color='white') for _ in range(NUM_LIGHTS)]
for point in points:
    ax.add_patch(point)

# Generate motion data
point_light_positions = generate_motion_data()

# Animation function
def animate(frame):
    for i, point in enumerate(points):
        # Interpolate between current and next position
        if frame < len(point_light_positions) - 1:
            pos = point_light_positions[frame]
        else:
            pos = point_light_positions[-1]
        point.center = pos
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(point_light_positions), interval=50, blit=True)

plt.show()
