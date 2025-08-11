
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
    (0, 5), (-1, 4), (1, 4), (-2, 3), (2, 3),
    (-3, 2), (3, 2), (-4, 1), (4, 1), (-5, 0),
    (5, 0), (-4, -1), (4, -1), (-3, -2), (3, -2)
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
        new_x = x + 0.1 * frame  # Jumping forward motion
        new_y = y + 0.1 * np.sin(frame / 10)  # Slight up and down motion
        new_positions.append((new_x, new_y))
    
    for i, (x, y) in enumerate(new_positions):
        points[i].set_data(x, y)
    
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

plt.show()
