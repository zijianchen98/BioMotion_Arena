
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define the coordinates for the 15 points representing body parts
# This is based on biomechanical, realistic data to represent walking motion
def generate_walking_data(frames):
    # Using sine waves and offsets to create smooth walking motion
    # Coordinates were estimated to mimic human walking movement
    body_parts = {
        'head': [0, 5],
        'shoulder_left': [-1.5, 4],
        'shoulder_right': [1.5, 4],
        'elbow_left': [-3, 3],
        'elbow_right': [3, 3],
        'hand_left': [-4, 2.5],
        'hand_right': [4, 2.5],
        'hip_left': [-1.2, 2],
        'hip_right': [1.2, 2],
        'knee_left': [-1.5, 1],
        'knee_right': [1.5, 1],
        'foot_left': [-1.7, 0],
        'foot_right': [1.7, 0],
        'ankle_left': [-1.8, 0.5],
        'ankle_right': [1.8, 0.5],
    }

    # Simulate walking by adding sinusoidal motion
    data = {key: [] for key in body_parts.keys()}
    x_offset = np.pi / 8
    y_offset = np.pi / 12

    for frame in range(frames):
        t = frame / frames * 2 * np.pi  # Normalize frame to radians
        for part, (x, y) in body_parts.items():
            if "foot" in part or "knee" in part or "hip" in part:
                x_adj = x + np.sin(t - x_offset if 'left' in part else t + x_offset) * 0.5
                y_adj = y + np.sin(t - y_offset if 'left' in part else t + y_offset) * 0.3
            elif "hand" in part or "elbow" in part or "shoulder" in part:
                x_adj = x + np.sin(t if 'left' in part else t + x_offset) * 0.4
                y_adj = y + np.cos(t if 'left' in part else t + y_offset) * 0.2
            elif "head" in part:
                x_adj = x
                y_adj = y
            data[part].append([x_adj, y_adj])
    
    return data

# Function to update the animation frame
def update(frame):
    plt.cla()
    plt.axis([-5, 5, -2, 6])  # Set the axis to visualize walking properly
    plt.gca().set_facecolor('black')
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])

    for part, trajectory in walking_data.items():
        x, y = trajectory[frame]
        plt.plot(x, y, 'o', color='white', markersize=5)

# Number of frames for the animation
frames = 60
walking_data = generate_walking_data(frames)

# Create the animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=frames, interval=100)
plt.show()
