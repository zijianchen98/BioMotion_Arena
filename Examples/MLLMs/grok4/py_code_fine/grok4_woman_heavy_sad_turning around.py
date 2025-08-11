
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configure the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.axis('off')

# Number of point lights
num_points = 15
points_artist, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize positions of point lights representing the biological motion
def init():
    points_artist.set_data([], [])
    return points_artist,

# Function to generate positions for the points simulating turning around
def update(frame):
    # Calculate angle for turning motion
    angle = frame * 0.1  # Change the speed of turning here

    # Create a sad posture (static in this case)
    # Points in a formation representing the sad woman
    y_positions = np.linspace(-1, 1, num_points)
    x_positions = np.sin(angle) * np.ones(num_points)

    # Simulating turning by altering the x positions
    points_artist.set_data(x_positions, y_positions)
    return points_artist,

# Create animation
anim = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
