
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration for 15-point light structure of a jumping person
points = np.array([
    [0, 0],  # Head
    [0, 1],  # Neck
    [-1, 2],  [1, 2],  # Shoulders
    [-2, 3],  [2, 3],  # Hips
    [-0.5, 3.5],  [0.5, 3.5],  # Knees
    [-1, 4],  [1, 4],  # Ankles
    [-2.5, 1.5],  [2.5, 1.5],  # Elbows
    [-2, 2.4],  [2, 2.4],  # Wrists
    [-3, 3.1],  [3, 3.1],  # Hands
])

# Function to animate the jumping motion
def update(frame):
    # Vertical offset
    offset = np.sin(frame / 5) * 2

    # Update vertical position of each point
    for point in points:
        point[1] += offset

    # Drawing updates
    plt.clear()
    plt.scatter(points[:, 0], points[:, 1], color='white')
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.axis('off')

# Create the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Show the plot
plt.show()
