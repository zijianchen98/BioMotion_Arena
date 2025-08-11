
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 body joints for a human figure (simplified)
body_joints = [
    (0.0, 0.0),          # Hip
    (0.3, 0.0),          # Knee
    (0.6, 0.0),          # Ankle
    (0.4, 0.3),          # Hip (right)
    (0.6, 0.3),          # Knee (right)
    (0.8, 0.3),          # Ankle (right)
    (0.4, -0.3),         # Hip (left)
    (0.6, -0.3),         # Knee (left)
    (0.8, -0.3),         # Ankle (left)
    (0.0, 0.4),          # Spine
    (0.0, 0.6),          # Head
    (0.1, 0.5),          # Shoulder (right)
    (0.3, 0.5),          # Elbow (right)
    (0.5, 0.5),          # Wrist (right)
    (0.1, -0.5),         # Shoulder (left)
    (0.3, -0.5),         # Elbow (left)
    (0.5, -0.5),         # Wrist (left)
]

# Select only the 15 joints
body_joints = body_joints[:15]

# Create circles for the point lights
points = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Define a function to simulate jumping motion
def jump_motion(t, total_time=5):
    # Jumping motion: up and down
    # t: current time
    # total_time: total animation duration
    # y = -0.5 * (t / total_time - 1)**2 + 1
    y = -0.5 * (t / total_time - 1)**2 + 1
    # Apply some small random noise for realism
    noise = np.random.normal(0, 0.01, size=15)
    return np.array(body_joints) + np.array([0, y]) + noise

# Animation function
def animate(t):
    positions = jump_motion(t)
    for i, point in enumerate(points):
        point.center = positions[i]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
