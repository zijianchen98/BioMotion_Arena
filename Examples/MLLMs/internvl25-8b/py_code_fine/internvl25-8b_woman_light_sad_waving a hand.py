
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_circle(xy, rad, shape):
    circle = plt.Circle(xy, rad, fill=False, color='white')
    shape.append(circle)

def update(frame, shapes):
    num_points = 15
    center = (0.5, 0.5)
    point_size = 1.0
    max_velocity = 0.15

    if frame % num_points < num_points / 4:
        direction = np.array([-0.9, 0])
        velocity = max_velocity * np.sin(np.pi * frame / 6) * direction
    elif frame % num_points < num_points * 2 / 4:
        direction = np.array([0, -0.9])
        velocity = max_velocity * np.sin(np.pi * frame / 6) * direction
    elif frame % num_points < 3 * num_points / 4:
        direction = np.array([-0.9, 0])
        velocity = -max_velocity * np.sin(np.pi * frame / 6) * direction
    else:
        direction = np.array([0, -0.9])
        velocity = -max_velocity * np.sin(np.pi * frame / 6) * direction

    for shape in shapes:
        for c in shape:
            c.set_xy(center + velocity + direction * np.sin(np.pi * frame / 6))

    return shapes

fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
shape = []

for i in range(15):
    create_circle(np.array([0.5, 0.5]), 0.05, shape)

ani = animation.FuncAnimation(fig, update, frames=180, blit=True, fargs=(shape,), interval=10, repeat=False)
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.show()
