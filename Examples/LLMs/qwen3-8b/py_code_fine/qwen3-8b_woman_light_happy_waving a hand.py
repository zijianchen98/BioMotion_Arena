
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

# Define the body parts and their positions (simplified for a waving hand)
body_parts = {
    'shoulder': np.array([0.0, 0.6]),
    'elbow': np.array([0.2, 0.4]),
    'wrist': np.array([0.4, 0.2]),
    'hand': np.array([0.5, 0.1]),
    'hip': np.array([0.0, -0.4]),
    'knee': np.array([0.1, -0.2]),
    'ankle': np.array([0.2, 0.0]),
    'foot': np.array([0.3, -0.1]),
    'head': np.array([0.0, 0.8]),
    'neck': np.array([0.0, 0.6]),  # same as shoulder for simplicity
    'spine': np.array([0.0, 0.4]),
    'shoulder2': np.array([-0.2, 0.6]),
    'elbow2': np.array([-0.4, 0.4]),
    'wrist2': np.array([-0.6, 0.2]),
    'hand2': np.array([-0.7, 0.1]),
    'hip2': np.array([-0.2, -0.4]),
    'knee2': np.array([-0.3, -0.2]),
    'ankle2': np.array([-0.4, 0.0]),
    'foot2': np.array([-0.5, -0.1]),
}

# Create point lights
point_lights = {}
for part in body_parts:
    point_lights[part] = Circle(body_parts[part], 0.02, color='white')

# Add point lights to the plot
for light in point_lights.values():
    ax.add_patch(light)

# Define the motion parameters
def update(frame):
    # Define the motion of the hand (waving motion)
    hand_angle = 0.5 * np.sin(2 * np.pi * frame / 10)
    hand_offset = np.array([0.0, 0.1 * np.sin(2 * np.pi * frame / 10)])
    hand_pos = body_parts['hand'] + hand_offset
    body_parts['hand'] = hand_pos

    # Update the position of the hand light
    point_lights['hand'].center = hand_pos

    # Define the motion of the wrist
    wrist_angle = 0.3 * np.sin(2 * np.pi * frame / 10)
    wrist_offset = np.array([0.0, 0.05 * np.sin(2 * np.pi * frame / 10)])
    wrist_pos = body_parts['wrist'] + wrist_offset
    body_parts['wrist'] = wrist_pos

    # Update the position of the wrist light
    point_lights['wrist'].center = wrist_pos

    # Define the motion of the elbow
    elbow_angle = 0.2 * np.sin(2 * np.pi * frame / 10)
    elbow_offset = np.array([0.0, 0.03 * np.sin(2 * np.pi * frame / 10)])
    elbow_pos = body_parts['elbow'] + elbow_offset
    body_parts['elbow'] = elbow_pos

    # Update the position of the elbow light
    point_lights['elbow'].center = elbow_pos

    # Define the motion of the shoulder
    shoulder_angle = 0.1 * np.sin(2 * np.pi * frame / 10)
    shoulder_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    shoulder_pos = body_parts['shoulder'] + shoulder_offset
    body_parts['shoulder'] = shoulder_pos

    # Update the position of the shoulder light
    point_lights['shoulder'].center = shoulder_pos

    # Define the motion of the other hand (mirror image)
    hand2_angle = 0.5 * np.sin(2 * np.pi * frame / 10)
    hand2_offset = np.array([0.0, 0.1 * np.sin(2 * np.pi * frame / 10)])
    hand2_pos = body_parts['hand2'] + hand2_offset
    body_parts['hand2'] = hand2_pos

    # Update the position of the hand2 light
    point_lights['hand2'].center = hand2_pos

    # Define the motion of the wrist2
    wrist2_angle = 0.3 * np.sin(2 * np.pi * frame / 10)
    wrist2_offset = np.array([0.0, 0.05 * np.sin(2 * np.pi * frame / 10)])
    wrist2_pos = body_parts['wrist2'] + wrist2_offset
    body_parts['wrist2'] = wrist2_pos

    # Update the position of the wrist2 light
    point_lights['wrist2'].center = wrist2_pos

    # Define the motion of the elbow2
    elbow2_angle = 0.2 * np.sin(2 * np.pi * frame / 10)
    elbow2_offset = np.array([0.0, 0.03 * np.sin(2 * np.pi * frame / 10)])
    elbow2_pos = body_parts['elbow2'] + elbow2_offset
    body_parts['elbow2'] = elbow2_pos

    # Update the position of the elbow2 light
    point_lights['elbow2'].center = elbow2_pos

    # Define the motion of the shoulder2
    shoulder2_angle = 0.1 * np.sin(2 * np.pi * frame / 10)
    shoulder2_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    shoulder2_pos = body_parts['shoulder2'] + shoulder2_offset
    body_parts['shoulder2'] = shoulder2_pos

    # Update the position of the shoulder2 light
    point_lights['shoulder2'].center = shoulder2_pos

    # Define the motion of the hip and foot (simple oscillation)
    hip_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    hip_pos = body_parts['hip'] + hip_offset
    body_parts['hip'] = hip_pos
    point_lights['hip'].center = hip_pos

    foot_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    foot_pos = body_parts['foot'] + foot_offset
    body_parts['foot'] = foot_pos
    point_lights['foot'].center = foot_pos

    hip2_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    hip2_pos = body_parts['hip2'] + hip2_offset
    body_parts['hip2'] = hip2_pos
    point_lights['hip2'].center = hip2_pos

    foot2_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    foot2_pos = body_parts['foot2'] + foot2_offset
    body_parts['foot2'] = foot2_pos
    point_lights['foot2'].center = foot2_pos

    # Define the motion of the spine
    spine_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    spine_pos = body_parts['spine'] + spine_offset
    body_parts['spine'] = spine_pos
    point_lights['spine'].center = spine_pos

    # Define the motion of the neck
    neck_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    neck_pos = body_parts['neck'] + neck_offset
    body_parts['neck'] = neck_pos
    point_lights['neck'].center = neck_pos

    # Define the motion of the head
    head_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    head_pos = body_parts['head'] + head_offset
    body_parts['head'] = head_pos
    point_lights['head'].center = head_pos

    # Define the motion of the knee
    knee_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    knee_pos = body_parts['knee'] + knee_offset
    body_parts['knee'] = knee_pos
    point_lights['knee'].center = knee_pos

    # Define the motion of the ankle
    ankle_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    ankle_pos = body_parts['ankle'] + ankle_offset
    body_parts['ankle'] = ankle_pos
    point_lights['ankle'].center = ankle_pos

    # Define the motion of the knee2
    knee2_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    knee2_pos = body_parts['knee2'] + knee2_offset
    body_parts['knee2'] = knee2_pos
    point_lights['knee2'].center = knee2_pos

    # Define the motion of the ankle2
    ankle2_offset = np.array([0.0, 0.02 * np.sin(2 * np.pi * frame / 10)])
    ankle2_pos = body_parts['ankle2'] + ankle2_offset
    body_parts['ankle2'] = ankle2_pos
    point_lights['ankle2'].center = ankle2_pos

    # Return the artist to animate
    return list(point_lights.values())

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
