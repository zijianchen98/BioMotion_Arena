
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the human body
# 15 points: head, torso, left shoulder, left elbow, left wrist, left hip, left knee, left ankle,
#            right shoulder, right elbow, right wrist, right hip, right knee, right ankle
point_light_locations = np.array([
    [0, 0.5],  # head
    [0, 0.3],  # torso
    [-0.2, 0.4],  # left shoulder
    [-0.3, 0.3],  # left elbow
    [-0.4, 0.2],  # left wrist
    [-0.2, 0.1],  # left hip
    [-0.3, 0.0],  # left knee
    [-0.4, -0.1],  # left ankle
    [0.2, 0.4],  # right shoulder
    [0.3, 0.3],  # right elbow
    [0.4, 0.2],  # right wrist
    [0.2, 0.1],  # right hip
    [0.3, 0.0],  # right knee
    [0.4, -0.1],  # right ankle
    [0, 0.1]  # bottom of torso
])

# Define the keyframes for the sitting down action
keyframes = np.array([
    # initial standing position
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # start sitting down
    [0, -0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-0.1, -0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-0.2, -0.3, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    # sitting down
    [-0.3, -0.4, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, -0.1],
    # final sitting position
    [-0.4, -0.5, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, -0.2]
])

# Define the interpolation function
def interpolate(keyframes, num_frames):
    interpolated_frames = np.zeros((num_frames, len(keyframes[0])))
    for i in range(len(keyframes) - 1):
        for j in range(num_frames // (len(keyframes) - 1)):
            t = j / (num_frames // (len(keyframes) - 1))
            interpolated_frames[i * (num_frames // (len(keyframes) - 1)) + j] = keyframes[i] + t * (keyframes[i + 1] - keyframes[i])
    return interpolated_frames

# Interpolate the keyframes to get the final animation frames
num_frames = 100
animation_frames = interpolate(keyframes, num_frames)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')
ax.set_axis_off()

# Create the point-light stimuli
point_lights = ax.scatter(point_light_locations[:, 0], point_light_locations[:, 1], s=50, c='w')

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.set_axis_off()
    point_light_locations_animated = point_light_locations + animation_frames[i]
    ax.scatter(point_light_locations_animated[:, 0], point_light_locations_animated[:, 1], s=50, c='w')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

plt.show()
