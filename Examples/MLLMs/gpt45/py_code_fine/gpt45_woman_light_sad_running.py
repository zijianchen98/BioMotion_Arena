
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 4)
ax.set_axis_off()
fig.patch.set_facecolor('black')

points, = ax.plot([], [], 'wo', ms=8)

def body_coordinates(t):
    head = [0, 3 + 0.05*np.sin(2*t)]

    shoulders = np.array([
        [-0.5, 2.5 + 0.05*np.sin(2*t)],
        [0, 2.4 + 0.05*np.sin(2*t)],
        [0.5, 2.5 + 0.05*np.sin(2*t)]
    ])

    waist = np.array([
        [-0.4, 1.7 + 0.08*np.sin(2*t)],
        [0, 1.6 + 0.08*np.sin(2*t)],
        [0.4, 1.7 + 0.08*np.sin(2*t)]
    ])

    hip_left = [-0.3, 1.3 + 0.09*np.sin(2*t)]
    hip_right = [0.3, 1.3 - 0.09*np.sin(2*t)]

    knee_left = [-0.3 + 0.15*np.sin(t), 0.6 - 0.2*np.abs(np.cos(t))]
    knee_right = [0.3 + 0.15*np.sin(t+np.pi), 0.6 - 0.2*np.abs(np.cos(t+np.pi))]

    ankle_left = [-0.3 + 0.3*np.sin(t), -0.3*np.abs(np.cos(t))]
    ankle_right = [0.3 + 0.3*np.sin(t+np.pi), -0.3*np.abs(np.cos(t+np.pi))]

    foot_left = [ankle_left[0] + 0.2, ankle_left[1]-0.1]
    foot_right = [ankle_right[0] + 0.2, ankle_right[1]-0.1]

    coordinates = np.array([
        head,
        shoulders[0], shoulders[1], shoulders[2],
        waist[0], waist[1], waist[2],
        hip_left, hip_right,
        knee_left, knee_right,
        ankle_left, ankle_right,
        foot_left, foot_right
    ])

    return coordinates[:,0], coordinates[:,1]

def animate(i):
    t = 0.1*i
    x, y = body_coordinates(t)
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
