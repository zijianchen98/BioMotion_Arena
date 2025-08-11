
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial points for the figure (arbitrary coordinates for illustration)
points = np.array([
    [0, 1], [0, 2], [-1, 3], [1, 3], [-1.5, 4], [1.5, 4], 
    [-0.5, 5], [0.5, 5], [0, 6], [-0.5, 7], [0.5, 7], [-1, 8],
    [1, 8], [-0.5, 9], [0.5, 9]
])

# Function to update the points positions in the animation
def update_points(t):
    global points
    # Simulate a waving hand motion (simple example, not biomechanically accurate)
    wave_height = 0.5 * np.sin(t)
    points[6:, 0] += wave_height  # Move the hand points horizontally
    return points,

# Animation update function
def animate(i):
    t = i / 20.0
    updated_points = update_points(t)
    scatter.set_offsets(updated_points[0])
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Plot the points
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=50)

plt.axis('off')
plt.show()
