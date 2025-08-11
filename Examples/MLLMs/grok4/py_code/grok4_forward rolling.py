
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_points = 15  # Number of point-lights
duration = 5      # Duration of the animation in seconds
fps = 30          # Frames per second
frames = duration * fps

# Function to simulate forward roll motion
def forward_roll_motion(t):
    # Simple sinusoidal motion for the rolling effect
    x = 0.1 * np.sin(2 * np.pi * t / duration)  # Side to side motion
    y = -t / duration * 2  # Moves downwards to simulate rolling down
    return x, y

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 1)
ax.set_facecolor('black')  # Background color

# Create point-light objects
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / fps  # Current time
    x_positions = np.linspace(-0.5, 0.5, num_points)
    y_positions = np.full(num_points, -1)  # Initial y positions
    
    # Update positions for animation
    for i in range(num_points):
        x, y = forward_roll_motion(t + i * 0.1)  # Offset for each point
        y_positions[i] = y + 1.5  # Adjust to keep points above the bottom
        points.set_data(x_positions[i] + x, y_positions[i])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

plt.show()
