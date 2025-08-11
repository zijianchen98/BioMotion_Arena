
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
FRAMES = FPS * DURATION

# Initial positions and velocities for the point-lights
positions = np.random.rand(NUM_POINTS, 2) * 10 - 5  # Random initial positions within a range
velocities = np.zeros((NUM_POINTS, 2))

# Function to update the positions based on the forward rolling motion
def update_positions(frame):
    global positions, velocities
    
    # Simulate forward rolling motion by updating positions and velocities
    for i in range(NUM_POINTS):
        if frame < FRAMES / 2:
            # Accelerate forward and downward
            velocities[i] += [0.05, 0.03]
        else:
            # Decelerate and reverse direction
            velocities[i] -= [0.05, 0.03]
        
        # Apply velocity to position
        positions[i] += velocities[i]

        # Boundary conditions to keep the points within the plot
        if positions[i][0] > 10:
            positions[i][0] = 10
            velocities[i][0] *= -0.9  # Bounce effect
        elif positions[i][0] < -10:
            positions[i][0] = -10
            velocities[i][0] *= -0.9  # Bounce effect
        
        if positions[i][1] > 10:
            positions[i][1] = 10
            velocities[i][1] *= -0.9  # Bounce effect
        elif positions[i][1] < -10:
            positions[i][1] = -10
            velocities[i][1] *= -0.9  # Bounce effect

# Animation function
def animate(frame):
    update_positions(frame)
    scatter.set_offsets(positions)

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')  # Hide the axes
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = FuncAnimation(fig, animate, frames=FRAMES, interval=1000/FPS)

plt.show()
