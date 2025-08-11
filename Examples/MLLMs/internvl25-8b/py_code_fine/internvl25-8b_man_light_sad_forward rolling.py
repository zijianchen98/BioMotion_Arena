
import numpy as np
import matplotlib.pyplot as plt

def init():
    global num_points
    num_points = 15
    point_positions = np.zeros((num_points, 2))
    point_speeds = np.zeros((num_points, 2))
    for i in range(num_points):
        if i % 3 == 0:  # Base
            point_speeds[i] = [0, 1]
        elif i % 3 == 1:  # Arm
            angle = 30 * (i % 3)  # Different arm positions
            point_speeds[i] = [1, 1] * np.cos(np.radians(angle))  # Different x speeds
        else:  # Legs
            point_speeds[i] = [0.6, 0.1]
    return point_positions, point_speeds

def update(frame):
    global point_positions, point_speeds
    point_positions += point_speeds  # Update positions
    if frame % 60 == 20:  # Change direction every 60 frames
        point_speeds[:, 1] *= -1  # Flip y speeds
    return point_positions,

pos, speed = init()
fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1, 1), ylim=(-1, 1), aspect="equal")

def animate():
    ani = ax.animate(update, blit=True, interval=50, repeat=False, savefig='rolling_animation.gif')
    plt.draw()
    plt.pause(0.0001)

animate()
plt.close()
