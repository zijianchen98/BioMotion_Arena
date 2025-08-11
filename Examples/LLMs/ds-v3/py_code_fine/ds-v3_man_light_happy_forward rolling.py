
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 100
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the forward rolling motion (simplified)
def get_positions(t):
    # Main body trajectory (rolling_radius = 1.0
    x_center = 0.0
    y_center = -1.0 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    
    # Points representing the limbs and head in a rolling motion
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = x_center + 0.8 * np.cos(angles + 2 * np.pi * t / num_frames)
    y = y_center + 0.8 * np.sin(angles + 2 * np.pi * t / num_frames)
    
    # Add variation to simulate limbs
    for i in range(num_points):
        if i % 3 == 0:  # Head and limbs
            x[i] += 0.2 * np.sin(4 * np.pi * t / num_frames)
            y[i] += 0.2 * np.cos(4 * np.pi * t / num_frames)
        elif i % 2 == 0:  # Other limbs
            x[i] += 0.1 * np.sin(3 * np.pi * t / num_frames + np.pi/4)
            y[i] += 0.1 * np.cos(3 * np.pi * t / num_frames + np.pi/4)
    
    return x, y

# Update function for animation
def update(frame):
    x, y = get_positions(frame)
    for i, point in enumerate(points):
        point.center = (x[i], y[i])
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
