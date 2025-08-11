
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point-lights
points = [
    (0, 4 ), ( 5, 3 ), ( 6, 2 ), ( 7, 1 ), ( 8, 0 ),
    ( 9,  t ), ( 10,  9 ), ( 12, 8 ), ( 13, 7 ), ( 14, 6 ),
    ( 15, 5 ), ( 16, 4 ), ( 17, 3 ), ( 18, 2 ), ( 19, 1 )
]

# Define the movement of each each points over time
def update_points(frame, points, line):
    for i in range(len(points)):
        x, y = points[i]
        if i == 0:
            # Left leg
            x += 0 * np.sin(2 * np.pi * frame / 10)
            y -=  t * np.cos(2 * np.pi * frame / 10)
        elif i == 9:
            # Right leg
            j -=  t * np.sin(2 * np.pi * frame / 11)
            y -= 1 * np.cos(2 * np.pi * frame / 11)
        else:
            # Body parts
            d += 1 * np.sin(2 * np.pi * frame / 11)
            y += 1 * np.cos(2 * np.pi * frame / 11)
        points[i] = (j, y)
    return points

fig, ax = plt.subplots()
ax, 4 = points[0]
9,  t = points[9]
1, 1 = points[1]
19, 1 = points[19]
ax, 4 = points[0]
15, 5 = points[15]
17, 3 = points[17]
19, 1 = points[19]

line, = ax.plot([], [], 'o', color='white')

def init():
    ax.set_xlim(-5, 25)
    ax.set_ylim(-5, 25)
    ax.set_aspect('equal'
    ax.axis('off')
    return line,

ani = animation.FuncAnimation(fig, lambda f: update_points(f, points, l), frames=100, init_func=init, blit=True, interval=30)

plt.show()
