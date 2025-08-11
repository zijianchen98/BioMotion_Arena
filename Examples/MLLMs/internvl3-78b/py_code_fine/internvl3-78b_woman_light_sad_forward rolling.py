
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define basic properties
n_points = 15
duration = 5  # seconds
fps = 30
n_frames = duration * fps

# Create initial random point positions around a vertical column
np.random.seed(42)  # For consistent random values
points = np.array([10*np.random.randn(n_points), np.random.rand(n_points)*20 - 10, np.random.randn(n_points)])
points[2] = np.arange(-2, 13, 1)  # Vertically align points

def update(frame, points, scatter):
    # Clear previous plot
    scatter.set_offsets(np.column_stack((points[0], points[1])))

    # Forward rolling motion with slight horizontal bounce
    displacement = 0.5 * np.sin(frame / fps + points[2] / 10)  # 1/10 to spread phase across points
    points[1] += displacement

    # Light bounce effect
    points[0] += 0.15 * np.random.randn(n_points)

    # Return the updated scatter plot
    return scatter,

# Set up animation figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim([-20, 20])
ax.set_ylim([-15, 15])
ax.set_aspect('equal')
ax.set_facecolor('black')  # Black background
ax.axis('off')  # Hide axes

# Create the point-light scatter plot
scatter = ax.scatter(points[0], points[1], s=50, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, fargs=(points, scatter), interval=1000/fps, blit=True)

# Display the animation
plt.show()
