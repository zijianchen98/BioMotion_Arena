
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation parameters
duration = 5  # seconds
fps = 30  # frames per second
num_frames = duration * fps

# Define the point locations for the jumping motion
def jumping_motion(frame):
    # Normalize frame number
    t = frame / num_frames

    # Head
    head_x = 0.0
    head_y = 0.9 + 0.05 * np.sin(2 * np.pi * t)

    # Shoulders
    shoulder_width = 0.2
    shoulder_y = 0.7 + 0.03 * np.sin(2 * np.pi * t)
    left_shoulder_x = -shoulder_width
    right_shoulder_x = shoulder_width

    # Elbows
    elbow_amplitude = 0.1
    elbow_frequency = 2
    left_elbow_x = -shoulder_width - elbow_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    right_elbow_x = shoulder_width + elbow_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    left_elbow_y = 0.5 + 0.03 * np.sin(2 * np.pi * t)
    right_elbow_y = 0.5 + 0.03 * np.sin(2 * np.pi * t)

    # Wrists
    wrist_amplitude = 0.15
    wrist_frequency = 2
    left_wrist_x = -shoulder_width - 1.5 * elbow_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    right_wrist_x = shoulder_width + 1.5 * elbow_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    left_wrist_y = 0.3 + 0.03 * np.sin(2 * np.pi * t)
    right_wrist_y = 0.3 + 0.03 * np.sin(2 * np.pi * t)

    # Torso
    torso_top_y = 0.6 + 0.03 * np.sin(2 * np.pi * t)
    torso_bottom_y = 0.2 + 0.1 * np.sin(2 * np.pi * t)
    torso_mid_x = 0
    torso_mid_y = 0.4 + 0.03 * np.sin(2 * np.pi * t)

    # Hips
    hip_width = 0.15
    hip_y = 0.1 + 0.15 * np.sin(2 * np.pi * t)
    left_hip_x = -hip_width
    right_hip_x = hip_width

    # Knees
    knee_amplitude = 0.2
    knee_frequency = 2
    left_knee_x = -hip_width + knee_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    right_knee_x = hip_width - knee_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    left_knee_y = -0.2 + 0.15 * np.sin(2 * np.pi * t)
    right_knee_y = -0.2 + 0.15 * np.sin(2 * np.pi * t)

    # Ankles
    ankle_amplitude = 0.1
    ankle_frequency = 2
    left_ankle_x = -hip_width + 1.5 * knee_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    right_ankle_x = hip_width - 1.5 * knee_amplitude * np.sin(2 * np.pi * elbow_frequency * t)
    left_ankle_y = -0.5 + 0.15 * np.sin(2 * np.pi * t)
    right_ankle_y = -0.5 + 0.15 * np.sin(2 * np.pi * t)

    # Return point coordinates
    x = [head_x, left_shoulder_x, right_shoulder_x, left_elbow_x, right_elbow_x, left_wrist_x, right_wrist_x,
         torso_mid_x, left_hip_x, right_hip_x, left_knee_x, right_knee_x, left_ankle_x, right_ankle_x, torso_mid_x]
    y = [head_y, shoulder_y, shoulder_y, left_elbow_y, right_elbow_y, left_wrist_y, right_wrist_y,
         torso_top_y, hip_y, hip_y, left_knee_y, right_knee_y, left_ankle_y, right_ankle_y, torso_bottom_y]

    return x, y

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.axis('off')

# Create the scatter plot
scat = ax.scatter([], [], s=50, c='white')

# Define the animation function
def animate(frame):
    x, y = jumping_motion(frame)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True)

# Save the animation
#ani.save('jumping_stickman.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

# Show the animation
plt.show()
