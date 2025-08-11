
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
num_frames = 100
circle_radius = 1.0

# Generate points for the skeleton (3D positions in 2D Plane)
def generate_points(frame):
    # Base positions (Y-coordinates)
    base_positions = np.linspace(-1, 1, num_points)
    
    # Calculate angle for rotation (turning)
    angle = 2 * np.pi * frame / num_frames
    
    # Calculate x position based on the 'turning around' action
    x_positions = np.cos(angle) * circle_radius
    y_positions = base_positions  # Use base Y coordinates
    return x_positions, y_positions

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Animation function
def update(frame):
    x, y = generate_points(frame)
    points.set_data(x, y)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=50)

# Display the animation
plt.axis('off')  # Turn off the axis
plt.show()
