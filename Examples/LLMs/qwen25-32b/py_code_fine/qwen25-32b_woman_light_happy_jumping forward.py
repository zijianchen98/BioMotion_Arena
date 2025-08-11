
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the point-lights representing the jumping woman
points = {
    'left_ankle': np.zeros((num_frames, 2)),
    'right_ankle': np.zeros((num_frames, 2)),
    'left_knee': np.zeros((num_frames, 2)),
    'right_knee': np.zeros((num_frames, 2)),
    'left_hip': np.zeros((num_frames, 2)),
    'right_hip': np.zeros((num_frames, 2)),
    'pelvis': np.zeros((num_frames, 2)),
    'spine': np.zeros((num_frames, 2)),
    'neck': np.zeros((num_frames, 2)),
    'head': np.zeros((num_frames, 2)),
    'left_wrist': np.zeros((num_frames, 2)),
    'right_wrist': np.zeros((num_frames, 2)),
    'left_elbow': np.zeros((num_frames, 2)),
    'right_elbow': np.zeros((num_frames, 2)),
    'shoulder': np.zeros((num_frames, 2))
}

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the point-lights
scat = ax.scatter([], [], s=50, c='white')

def init():
    scat.set_offsets([])
    return scat,

def animate(frame):
    # Define the position of each point-light based on the frame
    t = 2 * np.pi * frame / num_frames
    
    points['left_ankle'][frame] = [np.cos(t + np.pi), np.sin(t) - 1]
    points['right_ankle'][frame] = [np.cos(t), np.sin(t) - 1]
    points['left_knee'][frame] = [(np.cos(t + np.pi) + np.cos(t)) / 2, (np.sin(t) - 1 + np.sin(t) - 1) / 2 + 0.2 * np.sin(2*t)]
    points['right_knee'][frame] = [(np.cos(t) + np.cos(t + np.pi)) / 2, (np.sin(t) - 1 + np.sin(t) - 1) / 2 + 0.2 * np.sin(2*t)]
    points['left_hip'][frame] = [(np.cos(t + np.pi) + np.cos(t)) / 2, (np.sin(t) - 1 + np.sin(t) - 1) / 2 + 0.5]
    points['right_hip'][frame] = [(np.cos(t) + np.cos(t + np.pi)) / 2, (np.sin(t) - 1 + np.sin(t) - 1) / 2 + 0.5]
    points['pelvis'][frame] = [(np.cos(t + np.pi) + np.cos(t)) / 2, (np.sin(t) - 1 + np.sin(t) - 1) / 2 + 0.75]
    points['spine'][frame] = [0, 1]
    points['neck'][frame] = [0, 1.5]
    points['head'][frame] = [0, 2]
    points['left_wrist'][frame] = [-np.cos(t), 2 + np.sin(t)]
    points['right_wrist'][frame] = [np.cos(t), 2 + np.sin(t)]
    points['left_elbow'][frame] = [-np.cos(t)/2, 1.5 + np.sin(t)]
    points['right_elbow'][frame] = [np.cos(t)/2, 1.5 + np.sin(t)]
    points['shoulder'][frame] = [0, 1.25]

    # Update the scatter plot with the new positions
    scat.set_offsets(np.vstack(list(points.values())[frame]))
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True)

plt.show()
