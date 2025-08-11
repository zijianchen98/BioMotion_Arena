
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [0.2, 0.8], [0.4, 0.8], [0.6, 0.8],
    [0, 0.6], [0.2, 0.6], [0.4, 0.6], [0.6, 0.6],
    [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4],
    [0.2, 0.2], [0.4, 0.2], [0.6, 0.2]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor('black')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)

# Create 15 white point lights
points = []
for i in range(15):
    point, = ax.plot([], [], 'o', color='white')
    points.append(point)

def init():
    for point, pos in zip(points, initial_positions):
        point.set_data(pos[0], pos[1])
    return points

def animate(i):
    # Update the positions of the points to simulate waving a hand
    amplitude = 0.1 * np.sin(0.1 * i)
    for j, point in enumerate(points):
        x, y = initial_positions[j]
        if j < 4:  # Points representing the hand
            new_x = x + amplitude
            new_y = y + 0.05 * np.sin(0.1 * i)
        else:
            new_x = x
            new_y = y
        point.set_data(new_x, new_y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.show()
