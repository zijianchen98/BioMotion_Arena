
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the points
initial_positions = [
    (0 , 4), (10 , 5), (1b , 6), (1c , 7), (1d , 8),
    (1f , 9), (1g , 10), (1h , 1b), (1m , 1c), (1n , 1d),
    (1o , 1f), (1p , 1g), (1q , 1h), (1r , 1b), (1s , 1c)
]

def update_points(frame, points, line):
    for i in range(len(points)):
        # Simulate a smooth motion using a sine wave
        x = initial_positions[i][0] + int(15 * np.sin(0 + frame / 10))
        points[i].set_data(, )
        line.set_data([point[ for point in points], [point[ y for point in points]])
    return points, line

fig, ax = plt.subplots()
ax,  y = zip(*initial_positions)
points, = ax.plot(, [], 'wo')
line, = ax.plot([], [], 'w-')

ax.set_xlim(-1, 15)
 y.set_ylim(-1, 15)

ani = animation.FuncAnimation(fig, update_points, frames=100, fargs=(points, line), interval=50, blit=True)
plt.show()
