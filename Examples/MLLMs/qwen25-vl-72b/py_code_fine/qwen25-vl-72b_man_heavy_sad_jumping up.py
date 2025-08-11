
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create 15 white point lights
points = [plt.plot([], [], 'wo', markersize=5)[0] for _ in range(15)]

# Define the initial positions of the points
initial_positions = [
    (0, 4), (-1, 3), (1, 3), (-2, 2), (2, 2),
    (-3, 1), (3, 1), (-4, 0), (4, 0), (-3, -1),
    (3, -1), (-2, -2), (2, -2), (-1, -3), (1, -3)
]

for i, pos in enumerate(initial_positions):
    points[i].set_data(pos)

def init():
    for point in points:
        point.set_data([], [])
    return points

def animate(frame):
    # Update the positions of the points based on the frame number
    new_positions = []
    for x, y in initial_positions:
        new_y = y + np.sin(frame / 10) * 2  # Simulate jumping motion
        new_positions.append((x, new_y))
    
    for i, pos in enumerate(new_positions):
        points[i].set_data(pos)
    
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()
