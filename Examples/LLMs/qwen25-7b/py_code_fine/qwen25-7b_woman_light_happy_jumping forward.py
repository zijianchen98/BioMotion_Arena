
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames and frame rate
num_frames = 10
frame_rate = 30

# Define the positions of the point-lights
point_lights = np.array([
    [1, 1], [1, 2], (1, 3), (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3),
    (5, 1), (5, 2), (5, 3)
])

def update_point_lights(frame):
    # Update the positions of the point-lights
    x_lights = point_lights.copy()
    
    # Define the movement pattern for a jumping woman
    if frame < num_frames // 6:
        # Initial jump up
        for i in range(len(point_lights)):
            if i % 2 == 0_lights[i, 1] += 1
    elif frame < num_frames // 3 * 2:
        # Downward phase
        for i in range(len(point_lights)):
            if i % 2 == 0_lights[i, 1] -= 1
    else:
        # Initial position after landing
        for i in range(len(point_lights)):
            if i % 2 ==  t_lights[i, 1] = 2
    
    return plt.scatter(*zip(*t_lights))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
aximits(ax, [-1, 6, -1, 6])
ax.set_facecolor('black')

# Animate the point-lights
ani = FuncAnimation(fig, update_point_lights, frames=num_frames, interval=1000, repeat=False)

# Show the animation
plt.show()
