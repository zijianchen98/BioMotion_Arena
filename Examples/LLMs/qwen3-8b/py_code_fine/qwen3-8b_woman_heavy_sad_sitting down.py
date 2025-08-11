
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions (body parts)
# These positions are relative to the center of the body
# Based on a sad woman sitting down, we model the body parts as a skeleton
# Positions are in normalized coordinates, centered at (0, 0)

# Body parts (15 points)
body_parts = {
    'head': (0, 0.5),
    'neck': (0, 0.3),
    'shoulder_left': (-0.2, 0.2),
    'elbow_left': (-0.3, 0.05),
    'wrist_left': (-0.3, -0.05),
    'hand_left': (-0.3, -0.2),
    'shoulder_right': (0.2, 0.2),
    'elbow_right': (0.3, 0.05),
    'wrist_right': (0.3, -0.05),
    'hand_right': (0.3, -0.2),
    'hip_left': (-0.2, -0.3),
    'knee_left': (-0.3, -0.5),
    'ankle_left': (-0.3, -0.7),
    'foot_left': (-0.3, -0.9),
    'hip_right': (0.2, -0.3),
    'knee_right': (0.3, -0.5),
    'ankle_right': (0.3, -0.7),
    'foot_right': (0.3, -0.9),
}

# Select 15 body parts (excluding one foot for simplicity)
selected_parts = list(body_parts.values())[:15]

# Create point-light circles
points = [Circle((x, y), 0.02, color='white') for x, y in selected_parts]
for point in points:
    ax.add_patch(point)

# Define the motion trajectory (simplified smooth motion for sitting down)
def motion(t):
    # Simulate a sitting motion over time (0 to 1)
    # We use sine waves for smooth movement
    # Each part moves in a way that mimics a realistic sitting motion
    # This is a simplified biomechanical model

    # Time scaling
    t_scaled = t * 2  # faster motion

    # Define motion for each part
    positions = []
    for x, y in selected_parts:
        # Head: lowers slowly
        head_x = x * (1 - t_scaled)
        head_y = y * (1 - t_scaled)
        positions.append((head_x, head_y))

        # Neck: follows head
        neck_x = x * (1 - t_scaled)
        neck_y = y * (1 - t_scaled)
        positions.append((neck_x, neck_y))

        # Left shoulder: lowers slightly
        left_shoulder_x = x * (1 - t_scaled * 0.8)
        left_shoulder_y = y * (1 - t_scaled * 0.7)
        positions.append((left_shoulder_x, left_shoulder_y))

        # Left elbow: lowers
        left_elbow_x = x * (1 - t_scaled * 0.6)
        left_elbow_y = y * (1 - t_scaled * 0.5)
        positions.append((left_elbow_x, left_elbow_y))

        # Left wrist: lowers
        left_wrist_x = x * (1 - t_scaled * 0.4)
        left_wrist_y = y * (1 - t_scaled * 0.3)
        positions.append((left_wrist_x, left_wrist_y))

        # Left hand: lowers
        left_hand_x = x * (1 - t_scaled * 0.2)
        left_hand_y = y * (1 - t_scaled * 0.1)
        positions.append((left_hand_x, left_hand_y))

        # Right shoulder: lowers slightly
        right_shoulder_x = x * (1 - t_scaled * 0.8)
        right_shoulder_y = y * (1 - t_scaled * 0.7)
        positions.append((right_shoulder_x, right_shoulder_y))

        # Right elbow: lowers
        right_elbow_x = x * (1 - t_scaled * 0.6)
        right_elbow_y = y * (1 - t_scaled * 0.5)
        positions.append((right_elbow_x, right_elbow_y))

        # Right wrist: lowers
        right_wrist_x = x * (1 - t_scaled * 0.4)
        right_wrist_y = y * (1 - t_scaled * 0.3)
        positions.append((right_wrist_x, right_wrist_y))

        # Right hand: lowers
        right_hand_x = x * (1 - t_scaled * 0.2)
        right_hand_y = y * (1 - t_scaled * 0.1)
        positions.append((right_hand_x, right_hand_y))

        # Hip left: lowers
        hip_left_x = x * (1 - t_scaled * 0.9)
        hip_left_y = y * (1 - t_scaled * 0.8)
        positions.append((hip_left_x, hip_left_y))

        # Knee left: lowers
        knee_left_x = x * (1 - t_scaled * 0.7)
        knee_left_y = y * (1 - t_scaled * 0.6)
        positions.append((knee_left_x, knee_left_y))

        # Ankle left: lowers
        ankle_left_x = x * (1 - t_scaled * 0.5)
        ankle_left_y = y * (1 - t_scaled * 0.4)
        positions.append((ankle_left_x, ankle_left_y))

        # Hip right: lowers
        hip_right_x = x * (1 - t_scaled * 0.9)
        hip_right_y = y * (1 - t_scaled * 0.8)
        positions.append((hip_right_x, hip_right_y))

        # Knee right: lowers
        knee_right_x = x * (1 - t_scaled * 0.7)
        knee_right_y = y * (1 - t_scaled * 0.6)
        positions.append((knee_right_x, knee_right_y))

        # Ankle right: lowers
        ankle_right_x = x * (1 - t_scaled * 0.5)
        ankle_right_y = y * (1 - t_scaled * 0.4)
        positions.append((ankle_right_x, ankle_right_y))

    return positions

# Animation function
def animate(t):
    positions = motion(t)
    for i, point in enumerate(points):
        point.set_center(positions[i])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
