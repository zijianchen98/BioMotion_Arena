
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15
duration = 5  # seconds
fps = 30  # frames per second
num_frames = duration * fps

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Initialize point lights positions (x, y)
points = np.zeros((num_points, 2))
# Define the initial positions for a sad running motion
points[:, 0] = np.random.uniform(0.4, 0.6, num_points)  # Random x positions
base_y = 0.5

# Set initial y positions for a sad woman's body posture
points[:5, 1] = base_y + np.array([-0.1, -0.05, 0, 0.05, 0.1])  # Head and shoulders
points[5:10, 1] = base_y - 0.15  # Body
points[10:, 1] = base_y - 0.2  # Lower body/legs

# Create points in the plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def update(frame):
    # Simulate running motion by updating y positions of points
    movement = 0.02 * np.sin(frame * np.pi / 15)  # Biomechanically plausible motion
    points[5:, 1] += movement / 2  # Higher body moves up, lower moves down
    points[5:, 1] = np.clip(points[5:, 1], 0.0, 1.0)  # Keep within bounds

    # Update scatter data
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval=1000 / fps)

# Display the animation
plt.show()
