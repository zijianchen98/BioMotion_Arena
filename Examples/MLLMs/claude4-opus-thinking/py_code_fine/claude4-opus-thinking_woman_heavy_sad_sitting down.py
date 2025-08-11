
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
frames = 60
duration = 5  # seconds
fps = frames / duration

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Generate point light coordinates for a sad woman sitting down
def generate_sitting_positions(frame):
    # Sedentary postures with slight movements to represent sitting down
    y_offset = -1 + (frame / frames) * 0.5  # Adjusting vertical position gradually
    x_positions = np.array([-0.2, 0.2, -0.2, 0.2, -0.5, 0.5, -0.5, 0.5, 0.0, 0.0, -0.3, 0.3, -0.15, 0.15, 0.0])
    y_positions = np.array([y_offset] * num_points)  # Keep y constant for standing posture
    return x_positions, y_positions

# Animation function
def init():
    points.set_data([], [])
    return points,

def update(frame):
    x_data, y_data = generate_sitting_positions(frame)
    points.set_data(x_data, y_data)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

# Show animation
plt.show()
