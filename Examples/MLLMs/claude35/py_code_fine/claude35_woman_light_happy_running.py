
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
num_points = 15
frames = 100
duration = 5  # duration of animation in seconds

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)

# Initial positions of point-lights representing the body
# This will start as a standing pose which will transition to a running pose
initial_positions = np.array([
    [0, 0],  # Center of mass
    [0, 2],  # Head
    [-1, 1], [1, 1],  # Shoulders
    [-1, 0], [1, 0],  # Hips
    [-1.5, -1], [1.5, -1],  # Knees
    [-1.8, -2], [1.8, -2],  # Ankles
    [-1, 0.5], [1, 0.5],  # Elbows
    [-2, -1], [2, -1],  # Hands
    [-1, -0.5], [1, -0.5]  # Feet
]).T

# Function to calculate position updates for each frame
def update(frame):
    t = frame / (frames / 2)  # Normalized time
    # Define positions for running motion
    positions = initial_positions.copy()
    
    # Example of running motion (simple changes, not biomechanically accurate)
    # Modify y-coordinates for feet and knees to simulate running
    positions[0] += 0.1 * np.sin(t * np.pi)  # CoM oscillation for running
    
    # Update point light positions for a running effect
    positions[3][0] += np.sin(t * 3) * 0.2  # Left foot
    positions[3][1] += np.cos(t * 3) * 0.2  # Right foot

    points.set_data(positions[0], positions[1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000 / 30, blit=True)

# Show the animation
plt.axis('off')  # Turn off the axis
plt.show()
