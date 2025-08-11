
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure, axis, and the background
fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1, 1), ylim=(-1, 1))
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0.0, 0.5],   # Head
    [-0.3, 0.4],  # Left shoulder
    [0.3, 0.4],   # Right shoulder
    [-0.4, 0.2],  # Left elbow
    [0.4, 0.2],   # Right elbow
    [-0.6, 0.0],  # Left wrist
    [0.6, 0.0],   # Right wrist
    [-0.3, -0.2], # Left hip
    [0.3, -0.2],  # Right hip
    [-0.2, -0.4], # Left knee
    [0.2, -0.4],  # Right knee
    [-0.1, -0.6], # Left ankle
    [0.1, -0.6],  # Right ankle
    [0.0, -0.8],  # Center body position
])

# Define the animation function
def animate(frame):
    # Calculate new positions for the point lights
    # Simulate a slight swaying motion for realism
    sway = 0.03 * np.sin(frame / 10.0) 
    positions = initial_positions.copy()
    
    # Update positions with slight perturbations
    positions[:, 0] += sway * np.sin(np.linspace(0, 2 * np.pi, 15))
    positions[:, 1] += sway * np.cos(np.linspace(0, 2 * np.pi, 15))
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
