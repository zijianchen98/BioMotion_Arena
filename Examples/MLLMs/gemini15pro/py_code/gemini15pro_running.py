
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need more frames for a smooth animation
# and realistic running motion.  Adjust these values to refine the animation.
key_frames = [
    # Frame 1
    [(1, 5), (2, 4), (3, 4), (4, 5), (2, 3), (3, 3), (1, 2), (2, 1.5), (3, 1.5), (4, 2), (1.5, 0), (3.5, 0), (2, -1), (3, -2), (2.5, -3)],
    # Frame 2 (Example - You'll need more frames)
    [(1.2, 5), (2.2, 4), (3.2, 4), (4.2, 5), (2.2, 3), (3.2, 3), (1.2, 2), (2.2, 1.5), (3.2, 1.5), (4.2, 2), (1.7, 0), (3.7, 0), (2.2, -1), (3.2, -2), (2.7, -3)]
]


fig, ax = plt.subplots()
ax.set_xlim([0, 5]) # Adjust limits as needed
ax.set_ylim([-4, 6])
ax.set_aspect('equal')  # Maintain aspect ratio
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')


def init():
    points.set_data([], [])
    return points,

def animate(i):
    frame = key_frames[i % len(key_frames)] # Loop through frames
    x = [p[0] for p in frame]
    y = [p[1] for p in frame]
    points.set_data(x, y)
    return points,


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(key_frames), interval=100, blit=True, repeat=True)

# To save the animation as a gif:
# ani.save('running_man.gif', writer='pillow', fps=10)

plt.show()


