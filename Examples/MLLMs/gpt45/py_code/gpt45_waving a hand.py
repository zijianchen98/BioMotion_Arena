
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1.5)
ax.set_facecolor('black')
plt.axis('off')

# Initial positions for the 15 points (head, shoulders, elbows, wrists, hips, knees, ankles, torso)
points, = ax.plot([], [], 'wo', markersize=8)

# Define basic fixed points (torso center, hips, knees, ankles, head)
torso_center = [0, 0.2]
right_hip = [-0.2, 0]
left_hip = [0.2, 0]
right_knee = [-0.2, -0.4]
left_knee = [0.2, -0.4]
right_ankle = [-0.2, -0.8]
left_ankle = [0.2, -0.8]
head = [0, 0.9]

shoulder_width = 0.3
shoulder_height = 0.4
right_shoulder = [-shoulder_width/2, shoulder_height]
left_shoulder = [shoulder_width/2, shoulder_height]

# Arm lengths
upper_arm_length = 0.3
lower_arm_length = 0.3

# Set waving arm parameters (right arm waves)
def arm_positions(angle):
    r_shoulder_x, r_shoulder_y = right_shoulder
    elbow_x = r_shoulder_x + upper_arm_length * np.cos(angle)
    elbow_y = r_shoulder_y + upper_arm_length * np.sin(angle)
    wrist_x = elbow_x + lower_arm_length * np.cos(angle + np.pi/4 * np.sin(angle*2))
    wrist_y = elbow_y + lower_arm_length * np.sin(angle + np.pi/4 * np.sin(angle*2))
    return [elbow_x, elbow_y], [wrist_x, wrist_y]

# Animation update function
def update(frame):
    angle = np.pi/4 * np.sin(frame / 10)

    elbow, wrist = arm_positions(angle)

    all_points = np.array([
        head,
        torso_center,
        right_shoulder,
        left_shoulder,
        right_hip,
        left_hip,
        right_knee,
        left_knee,
        right_ankle,
        left_ankle,
        elbow,             # right elbow moves
        wrist,             # right wrist moves
        [left_shoulder[0], left_shoulder[1]-upper_arm_length],  # left elbow static
        [left_shoulder[0], left_shoulder[1]-upper_arm_length-lower_arm_length],  # left wrist static
        [torso_center[0], torso_center[1]+0.2]  # mid-torso
    ])

    points.set_data(all_points[:,0], all_points[:,1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

plt.show()
