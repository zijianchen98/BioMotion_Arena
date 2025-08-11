
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize parameters for the human motion representation
num_points = 15
point_positions = np.zeros((num_points, 2))
frames = 100  # Total frames for the animation

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation
def update(frame):
    # Update positions to mimic sitting down motion
    t = frame / frames * np.pi  # Normalize frame count to a value between 0 and pi
    # Define y-position for the sitting down action
    # Here we simulate a basic sitting down motion
    y_positions = np.linspace(1.0, -0.5, num_points) + 0.1 * np.sin(t)
    
    # Update x positions for arranging points in a human-like formation
    x_positions = np.linspace(-0.2, 0.2, num_points) 
    point_positions[:, 0] = x_positions
    point_positions[:, 1] = y_positions
    
    points.set_data(point_positions[:, 0], point_positions[:, 1])
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
