
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('black')

ax.set_xlim([-2, 7])
ax.set_ylim([-1, 3])

# Initialize the points (15 joints)
dots, = ax.plot([], [], 'wo', markersize=8)

# Create motion trajectories for 15 joints (forward rolling human figure)
num_frames = 100
t = np.linspace(0, 2*np.pi, num_frames)

def create_rolling_frames(t):
    frames = []
    radius = 0.5
    for theta in t:
        # body orientation
        angle_offset = theta
        cx = 2 * theta / np.pi
        cy = radius

        joints = np.zeros((15, 2))

        # Head
        joints[0, :] = [cx, cy + 1.2]

        # Shoulders
        joints[1, :] = [cx + np.cos(angle_offset), cy + np.sin(angle_offset) + 0.7]
        joints[2, :] = [cx - np.cos(angle_offset), cy - np.sin(angle_offset) + 0.7]

        # Elbows
        joints[3, :] = joints[1, :] + np.array([np.cos(angle_offset + np.pi/2) * 0.5, np.sin(angle_offset + np.pi/2) * 0.5])
        joints[4, :] = joints[2, :] + np.array([-np.cos(angle_offset + np.pi/2) * 0.5, -np.sin(angle_offset + np.pi/2) * 0.5])

        # Wrists
        joints[5, :] = joints[3, :] + np.array([np.cos(angle_offset) * 0.3, np.sin(angle_offset) * 0.3])
        joints[6, :] = joints[4, :] + np.array([-np.cos(angle_offset) * 0.3, -np.sin(angle_offset) * 0.3])

        # Waist
        joints[7, :] = [cx, cy + 0.3]

        # Hips
        joints[8, :] = [cx + np.cos(angle_offset), cy + np.sin(angle_offset)]
        joints[9, :] = [cx - np.cos(angle_offset), cy - np.sin(angle_offset)]

        # Knees
        joints[10, :] = joints[8, :] + np.array([np.cos(angle_offset + np.pi/2) * 0.5, np.sin(angle_offset + np.pi/2) * 0.5])
        joints[11, :] = joints[9, :] + np.array([-np.cos(angle_offset + np.pi/2) * 0.5, -np.sin(angle_offset + np.pi/2) * 0.5])

        # Ankles
        joints[12, :] = joints[10, :] + np.array([np.cos(angle_offset) * 0.3, np.sin(angle_offset) * 0.3])
        joints[13, :] = joints[11, :] + np.array([-np.cos(angle_offset) * 0.3, -np.sin(angle_offset) * 0.3])

        # One extra joint to emphasize weight/heavy build (e.g., mid torso)
        joints[14, :] = [cx, cy + 0.5]

        frames.append(joints)
    return frames

points_frames = create_rolling_frames(t)

def init():
    dots.set_data([], [])
    return dots,

def animate(i):
    joints = points_frames[i % num_frames]
    dots.set_data(joints[:,0], joints[:,1])
    return dots,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=50, blit=True)

plt.show()
