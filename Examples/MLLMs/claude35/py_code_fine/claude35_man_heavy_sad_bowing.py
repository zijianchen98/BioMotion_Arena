
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Number of point-lights
num_lights = 15

# Initial positions of the point-lights (skeleton)
points = np.zeros((num_lights, 2))

# Define initial positions in a sad bowing posture
initial_positions = [
    (0, 1),  # Head
    (-0.5, 0.75), (0.5, 0.75),  # Shoulders
    (-0.75, 0.5), (0.75, 0.5),  # Elbows
    (-0.5, 0), (0.5, 0),  # Hands
    (-0.5, -0.75), (0.5, -0.75),  # Hips
    (-1, -1.5), (1, -1.5),  # Knees
    (-0.5, -2), (0.5, -2),  # Feet
    (0, 0),  # Center point for weight
    (0, -1.25)  # Weight point
]

for i, pos in enumerate(initial_positions):
    points[i] = pos

# Create the scatter plot for the points
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def animate(frame):
    # Modify the position to simulate bowing
    # Bow by moving points down and inward
    bow_angle = np.sin(frame * 0.1) * 0.5
    points[:, 1] -= bow_angle * 0.1  # Move down
    points[:, 0] = initial_positions[:, 0] * (1 - frame * 0.01)  # Move inward over frames
    
    # Update scatter plot
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 50), interval=50)

# Show the plot
plt.show()
