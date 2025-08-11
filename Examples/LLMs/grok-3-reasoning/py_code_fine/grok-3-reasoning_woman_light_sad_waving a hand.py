
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_positions(t):
    f = 0.5  # frequency of waving
    theta1 = np.pi / 4  # shoulder angle
    theta2 = np.pi / 2 + (np.pi / 6) * np.sin(2 * np.pi * f * t)  # elbow angle

    # Fixed positions
    head = (0, 1.6)
    neck = (0, 1.5)
    chest = (0, 1.3)
    pelvis = (0, 1.0)
    l_shoulder = (-0.2, 1.35)
    l_elbow = (-0.2, 1.05)
    l_wrist = (-0.2, 0.75)
    r_shoulder = (0.2, 1.35)
    l_hip = (-0.1, 0.95)
    l_knee = (-0.1, 0.55)
    l_ankle = (-0.1, 0.15)
    r_hip = (0.1, 0.95)
    r_knee = (0.1, 0.55)
    r_ankle = (0.1, 0.15)

    # Calculate right arm positions
    shoulder_r = r_shoulder
    elbow_r = (shoulder_r[0] + 0.3 * np.sin(theta1), shoulder_r[1] - 0.3 * np.cos(theta1))
    wrist_r = (elbow_r[0] + 0.3 * np.sin(theta1 + theta2), elbow_r[1] - 0.3 * np.cos(theta1 + theta2))

    # List of all positions
    positions = [head, neck, chest, l_shoulder, l_elbow, l_wrist, r_shoulder, elbow_r, wrist_r, l_hip, l_knee, l_ankle, r_hip, r_knee, r_ankle]
    return positions

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
points, = ax.plot([], [], 'o', color='white', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(t):
    positions = get_positions(t)
    x = [p[0] for p in positions]
    y = [p[1] for p in positions]
    points.set_data(x, y)
    return points,

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 10, 100), init_func=init, blit=True)
plt.show()
