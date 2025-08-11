
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame):
    num_points = 15

    # Define the initial positions of the points
    x = np.linspace(-0.625, 0.625, num_points)
    y = np.linspace(1.0, 1.0, num_points)
    points = np.array(list(zip(x, y)))

    # Modify the points for the motion
    if frame < 10:
        dy = (frame / 100) * 0.2
        new_points = points + np.array([0, dy * np.sin(-np.pi * x / 4)])
    elif 10 <= frame < 20:
        dy = -(frame / 100) * 0.2 + 0.2
        new_points = points + np.array([0, dy * np.sin(np.pi * x / 4)])
    elif 20 <= frame < 30:
        dy = (frame / 100) * 0.1 - 0.25
        new_points = points + np.array([0, dy * np.sin(np.pi * x / 2)])
    elif 30 <= frame < 40:
        dy = -(frame / 100) * 0.1 + 0.25
        new_points = points + np.array([0, dy * np.sin(np.pi * x / 2)])
    else:
        points = points + np.array([0, (frame / 100) * (-0.1 * np.sin(np.pi * x / 2))])

    # Update the positions of the points
    points[:num_points] = new_points[:num_points]
    return points

fig, ax = plt.subplots()
ax.set_xlim([-0.625, 0.625])
ax.set_ylim([0, 2.0])
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

scat = ax.scatter([], [], c='white', s=80)
ani = animation.FuncAnimation(fig, update, frames=range(0, 60), blit=True, interval=50, repeat=False)
plt.axis('off')

plt.show()
