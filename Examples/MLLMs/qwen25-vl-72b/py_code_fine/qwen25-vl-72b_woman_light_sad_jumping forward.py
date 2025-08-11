
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.5], [0, 0.5], [0.5, 0.5],
    [-0.7, 0], [-0.3, 0], [0, 0], [0.3, 0], [0.7, 0],
    [-0.5, -0.5], [0, -0.5], [0.5, -0.5],
    [-0.3, -1], [0, -1], [0.3, -1]
])

# Function to simulate jumping forward motion
def update_points(num, points):
    amplitude = 0.5 * np.sin(0.1 * num)
    for i, point in enumerate(points):
        x, y = initial_positions[i]
        # Apply a slight horizontal shift to simulate forward motion
        x += 0.01 * num
        # Apply vertical displacement to simulate jumping
        y += amplitude + 0.05 * np.sin(0.2 * num + i * np.pi / 8)
        point.set_data(x, y)
    return points

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

points = [ax.plot([], [], 'wo', markersize=10)[0] for _ in range(15)]

ani = animation.FuncAnimation(fig, update_points, fargs=(points,), frames=200, interval=50, blit=True)

plt.show()
