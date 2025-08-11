
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

points, = ax.plot([], [], 'o', color='white')

# Walk cycle keyframes
def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / 10.0

    # Define the positions of the points for a walking motion
    head = [5, 9 - 0.5 * np.sin(2 * np.pi * t)]
    neck = [5, 8 - 0.5 * np.sin(2 * np.pi * t)]
    shoulders = [4, 7 - 0.5 * np.sin(2 * np.pi * t)], [6, 7 - 0.5 * np.sin(2 * np.pi * t)]
    elbows = [3, 6.5 - 0.5 * np.sin(2 * np.pi * t)], [7, 6.5 - 0.5 * np.sin(2 * np.pi * t)]
    wrists = [2, 6 - 0.5 * np.sin(2 * np.pi * t)], [8, 6 - 0.5 * np.sin(2 * np.pi * t)]
    hips = [4.5, 6 - 0.25 * np.sin(2 * np.pi * t)], [5.5, 6 - 0.25 * np.sin(2 * np.pi * t)]
    knees = [4.3, 4 - 0.4 * np.sin(2 * np.pi * t)], [5.7, 4 - 0.4 * np.sin(2 * np.pi * t)]
    ankles = [4.1, 2 - 0.6 * np.sin(2 * np.pi * t)], [5.9, 2 - 0.6 * np.sin(2 * np.pi * t)]

    x_data = [head[0], neck[0], shoulders[0][0], elbows[0][0], wrists[0][0],
               shoulders[1][0], elbows[1][0], wrists[1][0],
               hips[0][0], knees[0][0], ankles[0][0],
               hips[1][0], knees[1][0], ankles[1][0]]

    y_data = [head[1], neck[1], shoulders[0][1], elbows[0][1], wrists[0][1],
               shoulders[1][1], elbows[1][1], wrists[1][1],
               hips[0][1], knees[0][1], ankles[0][1],
               hips[1][1], knees[1][1], ankles[1][1]]

    points.set_data(x_data, y_data)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, init_func=init, blit=True, interval=100)

plt.show()
