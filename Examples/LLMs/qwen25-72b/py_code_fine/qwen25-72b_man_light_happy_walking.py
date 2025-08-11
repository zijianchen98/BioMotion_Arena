
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the points
points = np.array([
    [0, 0],  # Torso center
    [-1, 1], [1, 1],  # Shoulders
    [-1.5, 1.5], [1.5, 1.5],  # Elbows
    [-2, 2], [2, 2],  # Hands
    [-0.5, -1], [0.5, -1],  # Hips
    [-1, -2], [1, -2],  # Knees
    [-1.5, -3], [1.5, -3],  # Ankles
    [-2, -4], [2, -4]  # Feet
])

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Define the walking animation
def update(frame):
    # Update the positions of the points
    angle = frame * 0.1
    for i in range(len(points)):
        if i == 0:  # Torso center
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [1, 2]:  # Shoulders
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [3, 4]:  # Elbows
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [5, 6]:  # Hands
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [7, 8]:  # Hips
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [9, 10]:  # Knees
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [11, 12]:  # Ankles
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
        elif i in [13, 14]:  # Feet
            points[i, 0] += 0.05 * np.cos(angle)
            points[i, 1] += 0.05 * np.sin(angle)
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
