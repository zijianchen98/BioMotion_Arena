
import time
import math
import matplotlib.pyplot as plt

# Points representing the sadman, coordinates are simplified for demonstration
points = [
    (5, 1), (7, 1), (9, 1),  # Arms
    (4, 2), (6, 2), (8, 2),  # Body
    (4, 3), (6, 3), (8, 3),  # Body
    (4, 4), (6, 4), (8, 4),  # Body
    (4, 5), (6, 5), (8, 5),  # Head
]

velocity = 0.1  # Speed of the wave

def update():
    global points
    for i in range(len(points)):
        px, py = points[i]
        if i < 3:
            points[i] = (px, py + math.sin(time.time())*velocity)
        else:
            points[i] = (px, py - math.sin(time.time())*velocity)
    return (points,)

# Setup for the animation using matplotlib
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
line, = ax.plot(points[0][0], points[0][1], 'o', color='white')

def init():
    line.set_data([p[0] for p in points], [p[1] for p in points])
    return line,

def animate():
    line.set_data([p[0] for p in points], [p[1] for p in points])
    return line,

ani = pltanimation.FuncAnimation(fig, animate, frames=150, fargs=(line,),
                                 init_func=init, blit=True, interval=100)

plt.show()
