
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to initialize the figure
def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-2, 2)
    return points,

# Function for the animation
def update(frame):
    # Update the positions of the points
    for i in range(len(positions)):
        # Simple model of sitting down motion
        if i in [1, 2, 4, 6, 7, 9]:  # E.g., legs, arms, torso
            delta_y = -0.01 * frame  # Move down slowly
            positions[i][1] += delta_y
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create initial positions for 15 points: head, arms, torso, and legs
positions = np.array([
    [0, 1.5],  # Head
    [-0.5, 1], [0.5, 1],  # Shoulders
    [-0.4, 0.5], [0.4, 0.5],  # Elbows
    [0, 0],  # Torso
    [-0.5, -0.5], [0.5, -0.5],  # Knees
    [-0.3, -1], [0.3, -1],  # Feet
    [-0.5, -1.2], [0.5, -1.2],  # Lower legs
    [-0.5, -1.4], [0.5, -1.4]   # Toes
])

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, repeat=False)

# Show the animation
plt.show()
