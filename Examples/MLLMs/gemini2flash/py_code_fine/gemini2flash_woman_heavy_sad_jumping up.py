
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial coordinates of the 15 points
initial_coords = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],   # Right Elbow
    [-1.5, 0.5], # Left Hand
    [1.5, 0.5],  # Right Hand
    [-0.2, 1.0], # Spine Top
    [0.2, 1.0],  # Spine Top
    [0.0, 0.5],  # Spine Bottom
    [-0.3, 0.0], # Left Hip
    [0.3, 0.0],  # Right Hip
    [-0.7, -0.5],# Left Knee
    [0.7, -0.5], # Right Knee
    [0.0, -1.0], # Ankle
])

# Define the functions that describe the movement of each point
def head_motion(frame):
    return [0.0, 2.0 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def left_shoulder_motion(frame):
    return [-0.5 + 0.05 * np.sin(2 * np.pi * frame / num_frames), 1.5 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def right_shoulder_motion(frame):
    return [0.5 - 0.05 * np.sin(2 * np.pi * frame / num_frames), 1.5 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def left_elbow_motion(frame):
    return [-1.0 + 0.05 * np.sin(2 * np.pi * frame / num_frames), 1.0 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def right_elbow_motion(frame):
    return [1.0 - 0.05 * np.sin(2 * np.pi * frame / num_frames), 1.0 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def left_hand_motion(frame):
    return [-1.5 + 0.1 * np.sin(2 * np.pi * frame / num_frames), 0.5 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def right_hand_motion(frame):
    return [1.5 - 0.1 * np.sin(2 * np.pi * frame / num_frames), 0.5 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def spine_top_motion1(frame):
    return [-0.2, 1.0 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def spine_top_motion2(frame):
    return [0.2, 1.0 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def spine_bottom_motion(frame):
    return [0.0, 0.5 + 0.1 * np.sin(2 * np.pi * frame / num_frames)]

def left_hip_motion(frame):
    return [-0.3 + 0.05 * np.sin(2 * np.pi * frame / num_frames), 0.0 + 0.3 * np.sin(2 * np.pi * frame / num_frames)]

def right_hip_motion(frame):
    return [0.3 - 0.05 * np.sin(2 * np.pi * frame / num_frames), 0.0 + 0.3 * np.sin(2 * np.pi * frame / num_frames)]

def left_knee_motion(frame):
    return [-0.7 + 0.1 * np.sin(2 * np.pi * frame / num_frames), -0.5 + 0.3 * np.sin(2 * np.pi * frame / num_frames)]

def right_knee_motion(frame):
    return [0.7 - 0.1 * np.sin(2 * np.pi * frame / num_frames), -0.5 + 0.3 * np.sin(2 * np.pi * frame / num_frames)]

def ankle_motion(frame):
    return [0.0, -1.0 + 0.3 * np.sin(2 * np.pi * frame / num_frames)]


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the 15 points
points, = ax.plot([], [], 'wo', markersize=8)

# Define the animation function
def animate(frame):
    x = [
        head_motion(frame)[0],
        left_shoulder_motion(frame)[0],
        right_shoulder_motion(frame)[0],
        left_elbow_motion(frame)[0],
        right_elbow_motion(frame)[0],
        left_hand_motion(frame)[0],
        right_hand_motion(frame)[0],
        spine_top_motion1(frame)[0],
        spine_top_motion2(frame)[0],
        spine_bottom_motion(frame)[0],
        left_hip_motion(frame)[0],
        right_hip_motion(frame)[0],
        left_knee_motion(frame)[0],
        right_knee_motion(frame)[0],
        ankle_motion(frame)[0]
    ]
    y = [
        head_motion(frame)[1],
        left_shoulder_motion(frame)[1],
        right_shoulder_motion(frame)[1],
        left_elbow_motion(frame)[1],
        right_elbow_motion(frame)[1],
        left_hand_motion(frame)[1],
        right_hand_motion(frame)[1],
        spine_top_motion1(frame)[1],
        spine_top_motion2(frame)[1],
        spine_bottom_motion(frame)[1],
        left_hip_motion(frame)[1],
        right_hip_motion(frame)[1],
        left_knee_motion(frame)[1],
        right_knee_motion(frame)[1],
        ankle_motion(frame)[1]
    ]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Save the animation as a gif
ani.save('sadwoman_jumping.gif', writer='pillow', fps=25)

# Show the animation
plt.show()
