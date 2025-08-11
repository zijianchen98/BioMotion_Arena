
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a standing posture
initial_positions = np.array([
    [0, 0],   # Head
    [-0.1, -0.2], [0.1, -0.2],  # Shoulders
    [-0.2, -0.4], [0.2, -0.4],  # Elbows
    [-0.3, -0.6], [0.3, -0.6],  # Wrists
    [0, -0.8],  # Waist
    [-0.1, -1.0], [0.1, -1.0],  # Hips
    [-0.2, -1.2], [0.2, -1.2],  # Knees
    [-0.3, -1.4], [0.3, -1.4],  # Ankles
    [-0.4, -1.6], [0.4, -1.6]   # Feet
])

# Define the target positions of the points for a bowing posture
target_positions = np.array([
    [0, -0.5],  # Head
    [-0.1, -0.7], [0.1, -0.7],  # Shoulders
    [-0.2, -0.9], [0.2, -0.9],  # Elbows
    [-0.3, -1.1], [0.3, -1.1],  # Wrists
    [0, -1.3],  # Waist
    [-0.1, -1.5], [0.1, -1.5],  # Hips
    [-0.2, -1.7], [0.2, -1.7],  # Knees
    [-0.3, -1.9], [0.3, -1.9],  # Ankles
    [-0.4, -2.1], [0.4, -2.1]   # Feet
])

# Create a figure and axis with a black background
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-3, 1)
ax.axis('off')

# Create the point lights
points = []
for i in range(15):
    point, = ax.plot([], [], 'w.', markersize=10)
    points.append(point)

# Animation function
def animate(frame):
    t = frame / 100  # Time parameter from 0 to 1
    for i in range(15):
        x = (1 - t) * initial_positions[i][0] + t * target_positions[i][0]
        y = (1 - t) * initial_positions[i][1] + t * target_positions[i][1]
        points[i].set_data(x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

plt.show()
