
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions over time (replace with your actual data)
# This example creates a simple jumping motion
n_frames = 30
t = np.linspace(0, 2 * np.pi, n_frames)
head_x = np.zeros(n_frames)
head_y = 2 * np.sin(t) + 5
shoulder_left_x = -1 + np.sin(t)/3
shoulder_left_y = 2 * np.sin(t) + 4
shoulder_right_x = 1 + np.sin(t)/3
shoulder_right_y = 2 * np.sin(t) + 4

elbow_left_x =  -2 - np.sin(t)
elbow_left_y = 2 * np.sin(t) + 3
elbow_right_x = 2 - np.sin(t)
elbow_right_y = 2 * np.sin(t) + 3

hand_left_x = -2 - 2*np.sin(t)
hand_left_y = 2*np.sin(t) + 2

hand_right_x = 2 -2* np.sin(t)
hand_right_y = 2*np.sin(t) + 2

hip_center_x = 0 
hip_center_y =  np.sin(t)
hip_left_x = -0.5 + np.sin(t)/3
hip_left_y = np.sin(t)
hip_right_x = 0.5+ np.sin(t)/3
hip_right_y =  np.sin(t)


knee_left_x = -1 - np.sin(t)
knee_left_y = -np.sin(t)
knee_right_x = 1 - np.sin(t)
knee_right_y = -np.sin(t)

foot_left_x = -1 - 2*np.sin(t)
foot_left_y = -2*np.sin(t)
foot_right_x = 1 -2*np.sin(t)
foot_right_y = -2*np.sin(t)

joint_positions = {
    "head": np.array([head_x, head_y]).T,
    "shoulder_left": np.array([shoulder_left_x, shoulder_left_y]).T,
    "shoulder_right": np.array([shoulder_right_x, shoulder_right_y]).T,
    "elbow_left": np.array([elbow_left_x, elbow_left_y]).T,
    "elbow_right": np.array([elbow_right_x, elbow_right_y]).T,
    "hand_left": np.array([hand_left_x, hand_left_y]).T,
    "hand_right": np.array([hand_right_x, hand_right_y]).T,
    "hip_center": np.array([hip_center_x, hip_center_y]).T,
    "hip_left": np.array([hip_left_x, hip_left_y]).T,
    "hip_right": np.array([hip_right_x, hip_right_y]).T,
    "knee_left": np.array([knee_left_x, knee_left_y]).T,
    "knee_right": np.array([knee_right_x, knee_right_y]).T,
    "foot_left": np.array([foot_left_x, foot_left_y]).T,
    "foot_right": np.array([foot_right_x, foot_right_y]).T,
}





# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black') # Set background color to black
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 8])
ax.set_aspect('equal') # Ensure correct aspect ratio

# Initialize the points
points = []
joint_names = list(joint_positions.keys())

for joint_name in joint_names:
    point, = ax.plot([], [], 'wo', markersize=8)
    points.append(point)

# Animation update function
def update(frame):
    for i, joint_name in enumerate(joint_names):
        x = joint_positions[joint_name][frame, 0]
        y = joint_positions[joint_name][frame, 1]

        points[i].set_data(x, y)

    return points


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)


plt.show()

