
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 100  # duration in milliseconds
frames = 60  # total frames for the animation

# Create a figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize the points
points = np.zeros((num_points, 2))

# Function to update the points
def update(frame):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('black')
    
    # Update the positions of points to simulate bowing
    for i in range(num_points):
        # Generate bowing motion
        if i < 5:  # Head -> shoulders
            points[i] = [0, 1 - 0.1 * i - 0.1 * np.sin(frame / 10)]
        elif i < 10:  # Arms
            points[i] = [-0.5 + 0.1 * (i - 5), 0.5 - 0.05 * np.sin(frame / 10)]
        else:  # Feet
            points[i] = [-0.5 + 0.1 * (i - 10), 0 - 0.1 * np.sin(frame / 10)]
    
    # Plot points
    ax.plot(points[:, 0], points[:, 1], 'wo', markersize=10)  # 'wo' for white points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=duration)

# Show the animation
plt.show()
