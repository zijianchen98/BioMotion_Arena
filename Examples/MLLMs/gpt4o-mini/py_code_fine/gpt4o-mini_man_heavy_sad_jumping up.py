
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Point lights positions (x, y)
point_lights = np.array([
    [0, 0.8],  # Head
    [-0.1, 0.6], [0.1, 0.6],  # Shoulders
    [-0.2, 0.4], [0.2, 0.4],  # Elbows
    [-0.3, 0.2], [0.3, 0.2],  # Hands
    [-0.1, 0.0], [0.1, 0.0],  # Hips
    [-0.2, -0.2], [0.2, -0.2],  # Knees
    [-0.3, -0.4], [0.3, -0.4],  # Feet
    [0, -0.5]  # Center of mass (weight)
])

# Function to update frame
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    # Update positions to create jump motion
    jump_height = 0.5 * np.sin(np.pi * (frame / 10))  # Simulate jump
    for i in range(len(point_lights)):
        if i == 0:  # Head
            ax.plot(point_lights[i][0], point_lights[i][1] + jump_height, 'wo', markersize=10)
        elif i == 8:  # Hips
            ax.plot(point_lights[i][0], point_lights[i][1] + jump_height - 0.2, 'wo', markersize=10)
        else:
            ax.plot(point_lights[i][0], point_lights[i][1] + jump_height - (0.2 if i >= 8 else 0), 'wo', markersize=10)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=30, interval=100)

plt.show()
