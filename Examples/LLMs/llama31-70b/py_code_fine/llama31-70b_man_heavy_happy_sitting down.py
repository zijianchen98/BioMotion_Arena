
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the happy man
point_lights = np.array([
    [0.0, 0.0],  # head
    [-0.2, 0.1],  # left shoulder
    [0.2, 0.1],  # right shoulder
    [-0.3, -0.2],  # left elbow
    [0.3, -0.2],  # right elbow
    [-0.4, -0.4],  # left wrist
    [0.4, -0.4],  # right wrist
    [0.0, -0.5],  # torso
    [-0.1, -0.6],  # left hip
    [0.1, -0.6],  # right hip
    [-0.2, -0.8],  # left knee
    [0.2, -0.8],  # right knee
    [-0.3, -1.0],  # left ankle
    [0.3, -1.0],  # right ankle
    [0.0, -0.9]  # body center
])

# Define the animation frames for the sitting down action
frames = 50
animation_frames = np.zeros((frames, 15, 2))

for i in range(frames):
    t = i / frames
    animation_frames[i] = point_lights.copy()
    
    # Move the body center down
    animation_frames[i][14] += np.array([0.0, -0.2 * t])
    
    # Move the head and torso down
    animation_frames[i][0] += np.array([0.0, -0.2 * t])
    animation_frames[i][7] += np.array([0.0, -0.2 * t])
    
    # Bend the knees
    animation_frames[i][11] += np.array([0.0, 0.1 * t])
    animation_frames[i][12] += np.array([0.0, 0.1 * t])
    
    # Move the arms
    animation_frames[i][1] += np.array([-0.1 * t, 0.1 * t])
    animation_frames[i][2] += np.array([0.1 * t, 0.1 * t])
    animation_frames[i][3] += np.array([-0.2 * t, 0.2 * t])
    animation_frames[i][4] += np.array([0.2 * t, 0.2 * t])
    
    # Move the elbows and wrists
    animation_frames[i][5] += np.array([-0.3 * t, 0.3 * t])
    animation_frames[i][6] += np.array([0.3 * t, 0.3 * t])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 0.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the first frame
points = ax.scatter(animation_frames[0][:, 0], animation_frames[0][:, 1], s=50, c='white')

# Define the animation function
def animate(i):
    points.set_offsets(animation_frames[i])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50)

plt.show()
