
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 0],
    [-10, 10],
    [0, 10],
    [10, 10],
    [-15, 20],
    [-5, 20],
    [5, 20],
    [15, 20],
    [-10, 30],
    [0, 30],
    [10, 30],
    [0, 40],
    [-5, 50],
    [5, 50],
    [0, 60]
])


def update(frame_num, data, line):
    # Animate the point lights turning around
    angle = frame_num * 0.1  # Adjust the speed of rotation
    rotated_positions = np.zeros_like(initial_positions)
    for i in range(len(initial_positions)):
      x, y = initial_positions[i]
      rotated_x = x * np.cos(angle) - y * np.sin(angle)
      rotated_y = x * np.sin(angle) + y * np.cos(angle)
      rotated_positions[i] = [rotated_x + 20, rotated_y + 20] #Adding offset for better visualization
    line.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return line,


fig = plt.figure(figsize=(6, 8))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-50, 50), ylim=(-20, 80))
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background to black


line, = ax.plot([], [], 'wo', markersize=8)  # 'wo' for white circles
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, line),
                              frames=200, interval=50, blit=True)

plt.title("Biological Motion: Happy Man Turning Around")
plt.axis('off')
plt.show()

