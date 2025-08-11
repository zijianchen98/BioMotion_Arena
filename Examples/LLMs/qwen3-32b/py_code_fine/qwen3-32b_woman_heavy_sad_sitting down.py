
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define the joint positions relative to a central body point (in cm)
def get_sad_woman_sitting_down_frame(t):
    # t ranges from 0 to 1, representing the progression of the action

    # Define base positions (at rest)
    spine_length = 80
    head_length = 20
    shoulder_width = 40
    arm_length = 60
    leg_length = 90
    hip_width = 30
    torso_angle = math.pi / 6  # Slight forward bend for sad posture
    head_angle = math.pi / 4   # Head down for sad posture

    # Torso and head
    spine = np.array([0, 0])
    head = spine + np.array([0, head_length]) + np.array([0, 0]) * math.sin(t * math.pi / 2)
    upper_torso = spine + np.array([0, spine_length / 2])
    lower_torso = spine + np.array([0, -spine_length / 2])

    # Shoulders
    left_shoulder = spine + np.array([-shoulder_width / 2, 0]) + np.array([0, 0]) * math.sin(t * math.pi / 2)
    right_shoulder = spine + np.array([shoulder_width / 2, 0]) + np.array([0, 0]) * math.sin(t * math.pi / 2)

    # Arms
    arm_bend = 0.5 * math.pi
    left_elbow = left_shoulder + np.array([0, -arm_length / 2]) + np.array([-arm_length / 2 * math.sin(arm_bend), -arm_length / 2 * math.cos(arm_length / 2 * math.cos(arm_bend))]) * (1 - t)
    left_hand = left_elbow + np.array([0, -arm_length / 2]) + np.array([-arm_length / 2 * math.sin(arm_bend), -arm_length / 2 * math.cos(arm_length / 2 * math.cos(arm_bend))]) * (1 - t)

    right_elbow = right_shoulder + np.array([0, -arm_length / 2]) + np.array([arm_length / 2 * math.sin(arm_bend), -arm_length / 2 * math.cos(arm_length / 2 * math.cos(arm_bend))]) * (1 - t)
    right_hand = right_elbow + np.array([0, -arm_length / 2]) + np.array([arm_length / 2 * math.sin(arm_bend), -arm_length / 2 * math.cos(arm_length / 2 * math.cos(arm_bend))]) * (1 - t)

    # Hips and legs
    left_hip = spine + np.array([-hip_width / 2, -spine_length / 2])
    right_hip = spine + np.array([hip_width / 2, -spine_length / 2])

    # Legs bend as she sits
    leg_bend = math.pi / 3 * t
    left_knee = left_hip + np.array([0, -leg_length / 2]) + np.array([-leg_length / 2 * math.sin(leg_bend), -leg_length / 2 * math.cos(leg_bend)])
    left_foot = left_knee + np.array([0, -leg_length / 2]) + np.array([-leg_length / 2 * math.sin(leg_bend), -leg_length / 2 * math.cos(leg_bend)])

    right_knee = right_hip + np.array([0, -leg_length / 2]) + np.array([leg_length / 2 * math.sin(leg_bend), -leg_length / 2 * math.cos(leg_bend)])
    right_foot = right_knee + np.array([0, -leg_length / 2]) + np.array([leg_length / 2 * math.sin(leg_bend), -leg_length / 2 * math.cos(leg_bend)])

    # Add slight downward head tilt and forward torso lean for sad posture
    head += np.array([0, -head_length * 0.3]) * t
    upper_torso += np.array([0, -spine_length * 0.15]) * t
    lower_torso += np.array([0, -spine_length * 0.15]) * t

    # Combine all points into a single array
    points = np.array([
        head,
        upper_torso,
        lower_torso,
        left_shoulder,
        right_shoulder,
        left_elbow,
        left_hand,
        right_elbow,
        right_hand,
        left_hip,
        right_hip,
        left_knee,
        left_foot,
        right_knee,
        right_foot
    ])

    # Translate the entire body to center it on the screen
    center = np.array([400, 300])
    points += center

    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(0, 800)
ax.set_ylim(0, 600)
ax.axis('off')

# Create scatter plot for the 15 points
points, = ax.plot([], [], 'wo', markersize=8)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(t):
    frame = get_sad_woman_sitting_down_frame(t)
    x = frame[:, 0]
    y = frame[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 1, 60), init_func=init, blit=True, interval=50)

plt.show()
