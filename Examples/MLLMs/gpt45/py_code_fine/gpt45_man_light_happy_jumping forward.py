
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up plot
fig, ax = plt.subplots()
ax.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(-2.5, 1)

# Define body parts as 15 points: head(1), shoulders(2), elbows(2), wrists(2), hips(2), knees(2), ankles(2), torso-upper(1), torso-lower(1)
dots, = ax.plot([], [], 'wo', markersize=8)

# Waving hand animation data
frames = 100
t = np.linspace(0, 2 * np.pi, frames)

# steady points coordinates
head = np.array([0, 0.8])
shoulder_left = np.array([-0.3, 0.5])
shoulder_right = np.array([0.3, 0.5])
torso_upper = np.array([0, 0.3])
torso_lower = np.array([0, 0])
hip_left = np.array([-0.2, -0.2])
hip_right = np.array([0.2, -0.2])
knee_left = np.array([-0.25, -1.0])
knee_right = np.array([0.25, -1.0])
ankle_left = np.array([-0.25, -1.8])
ankle_right = np.array([0.25, -1.8])

# waving hand (right arm) coordinates depending on the frames
def waving_hand_coords(frame):
    elbow_angle = np.pi/6 * np.sin(3*t[frame]) + np.pi/3
    wrist_angle = elbow_angle + np.pi/4 * np.sin(3*t[frame])

    elbow_right = shoulder_right + np.array([0.4*np.cos(elbow_angle), 0.4*np.sin(elbow_angle)])
    wrist_right = elbow_right + np.array([0.35*np.cos(wrist_angle), 0.35*np.sin(wrist_angle)])

    return elbow_right, wrist_right

# other arm static
elbow_left = shoulder_left + np.array([-0.35, -0.2])
wrist_left = elbow_left + np.array([-0.3, -0.3])

def animate(frame):
    elbow_right, wrist_right = waving_hand_coords(frame)
    
    x = np.array([head[0], shoulder_left[0], shoulder_right[0], torso_upper[0], torso_lower[0],
                  elbow_left[0], wrist_left[0], elbow_right[0], wrist_right[0], hip_left[0], hip_right[0],
                  knee_left[0], knee_right[0], ankle_left[0], ankle_right[0]])
    
    y = np.array([head[1], shoulder_left[1], shoulder_right[1], torso_upper[1], torso_lower[1],
                  elbow_left[1], wrist_left[1], elbow_right[1], wrist_right[1], hip_left[1], hip_right[1],
                  knee_left[1], knee_right[1], ankle_left[1], ankle_right[1]])
    
    dots.set_data(x, y)
    return dots,

fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ani = FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

plt.show()
