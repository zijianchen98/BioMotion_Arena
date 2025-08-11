
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))

# Define the structure of the walking person in terms of body parts
# Positions in the format [x, y]. This is simplified for illustration.
body_parts = [
    (0, 9),   # Head
    (-1, 8), (1, 8),   # Shoulders
    (-1, 7), (1, 7),   # Elbows
    (0, 6),   # Body
    (-1, 5), (1, 5),   # Hips
    (-1, 4), (1, 4),   # Knees
    (0, 3),   # Feet
]

# Assign initial positions to the points
for i, (x, y) in enumerate(body_parts):
    points[i] = np.array([x, y])

# Walking motion parameters
step_size = 0.1
step_up = np.array([0, 0.1])
step_side = np.array([0.1, 0])  # Sideways motion for walking

# Animation update function
def update(frame):
    global points
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(0, 10)
    
    # Simulate the walking motion
    points[1:9:2] += step_side  # Move left side points
    points[2:9:2] += -step_side  # Move right side points
    points[3:9:2] += step_up  # Move knees up slightly

    # Introduce smoothness by alternating motion
    if frame % 10 < 5:
        points[3:9:2] += -step_up  # Move knees down slightly

    # Update plot with the points
    plt.scatter(points[:, 0], points[:, 1], color='white')
    plt.gca().set_facecolor('black')  # Set background to black

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
