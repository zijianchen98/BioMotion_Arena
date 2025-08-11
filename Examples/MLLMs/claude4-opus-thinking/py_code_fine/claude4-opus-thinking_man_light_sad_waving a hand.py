
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 3)
ax.set_facecolor('black')  # Set background to black

# Number of point-lights
num_points = 15
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define initial positions of point-lights
# Body parts representation, symmetric around a vertical line
body_parts = np.array([
    [0, 3],  # Head
    [-0.5, 2.5], [0, 2.5], [0.5, 2.5],  # Shoulders
    [-0.5, 2], [0, 2], [0.5, 2],  # Elbows
    [-0.5, 1.5], [-0.5, 1.0],  # Left arm (elbow & wrist)
    [0, 1.5], [0, 1],  # Body center
    [0.5, 1.5], [0.5, 1.0],  # Right arm (elbow & wrist)
    [-0.5, 0], [0.5, 0]  # Feet
])

# Animation function
def animate(frame):
    # Calculate wave motion for the hand (right arm)
    elbow_offset = np.sin(frame * 0.1) * 0.1
    wrist_offset = np.sin(frame * 0.1) * 0.2
    
    # Update right arm positions for waving action
    body_parts[7, 1] = 1.5 + elbow_offset  # Elbow
    body_parts[9, 1] = 1.0 + wrist_offset  # Wrist
    
    # Clear the previous points
    points.set_data([], [])
    
    # Set new positions
    points.set_data(body_parts[:, 0], body_parts[:, 1])
    
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 200), interval=50, blit=True)

# Show the animation
plt.show()
