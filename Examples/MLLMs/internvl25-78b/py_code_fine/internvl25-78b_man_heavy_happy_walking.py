
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.axis('off')

# Define the initial positions of the points (should be adjusted for actual walking motion)
points = np.array([
    [5, 9],  # Head
    [4, 8], [6, 8],  # Shoulders
    [3, 7], [7, 7],  # Elbows
    [4, 6], [6, 6],  # Hips
    [3.5, 5], [6.5, 5],  # Knees
    [3, 4], [7, 4],  # Ankles
    [3.5, 2], [6.5, 2],  # Heels
    [4.5, 1], [5.5, 1],  # Hands
    [5, 0]  # Pelvis
])

# Create a scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

def update(frame):
    global points

    # Update positions based on walking motion
    step = 0.1 * np.sin(frame / 10)
    points[8:10, 1] -= step  # Heels move up and down
    points[6:8, 1] -= step / 2  # Ankles follow heels
    points[0, 1] += step / 4  # Head bobs slightly

    # Walking gait adjustments
    points[3:5, 0] += step * 2  # Elbows move backward
    points[11:13, 0] -= step * 2  # Hands move forward
    points[4:6, 0] += step  # Hips sway
    points[2:4, 0] += step / 2  # Shoulders sway

    # Update scatter plot
    sc.set_offsets(points)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=False)

plt.show()
