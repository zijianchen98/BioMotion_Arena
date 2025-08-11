
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the position of the points in frame 1
points_frame_1 = np.array([
    [0, 2],  # Head
    [-1, 1], [1, 1],  # Shoulders
    [-1.5, 0.5], [1.5, 0.5],  # Elbows
    [-2, 0], [2, 0],  # Hands
    [0, 0],  # Waist
    [-0.5, -0.5], [0.5, -0.5],  # Hips
    [-1, -1], [1, -1],  # Knees
    [-1.5, -1.5], [1.5, -1.5]  # Feet
])

# Define the position of the points in frame 2
points_frame_2 = np.array([
    [0, 2],  # Head
    [-1, 1.5], [1, 1.5],  # Shoulders
    [-1.5, 1], [1.5, 1],  # Elbows
    [-1.8, 0.5], [1.8, 0.5],  # Hands
    [0, 0.5],  # Waist
    [-0.5, 0], [0.5, 0],  # Hips
    [-0.5, -0.5], [0.5, -0.5],  # Knees
    [-1, -1], [1, -1]  # Feet
])

fig, ax = plt.subplots()
ax.set_facecolor('black')
scatter = ax.scatter([], [], color='white')

def update(frame):
    if frame % 2 == 0:
        positions = points_frame_1
    else:
        positions = points_frame_2
    
    positions += np.array([0, 0.1])
    scatter.set_offsets(positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=50, interval=100, blit=True)

plt.axis('off')
plt.show()
