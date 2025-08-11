
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FRAME_RATE = 30
DURATION = 2  # in seconds

# Initialize points
np.random.seed(42)
points = np.random.rand(NUM_POINTS, 2)

# Animation function
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    # Simulate jumping forward
    points[:, 0] += 0.01  # Simple horizontal movement
    
    # Simple biomechanics: Vertical component
    vertical_movement = np.sin(frame * 0.1)
    points[:, 1] += vertical_movement
    
    # Wrap around if out of bounds
    points[points > 1] -= 2
    points[points < -1] += 2
    
    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(0, DURATION * FRAME_RATE), interval=1000/FRAME_RATE, blit=False
)

# Display the animation
plt.show()
