
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(0, 20)
ax.set_facecolor('black')
points = []

# Initial positions for the point lights representing the body parts
initial_positions = np.array([
    [0, 18],   # Head
    [-2, 16], [2, 16],  # Shoulders
    [-3, 14], [0, 12], [3, 14],  # Elbows
    [-2, 10], [2, 10],  # Hands
    [-1, 8], [0, 6], [1, 8],  # Hips
    [-1, 4], [1, 4],  # Knees
    [0, 0],   # Feet
])

# Create the initial points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Animation update function
def update(frame):
    # Clear previous positions
    new_positions = initial_positions.copy()

    # Simulate the jumping motion
    jump_height = 5 * np.sin(frame / 10)
    
    # Update positions for the jumping effect
    new_positions[:, 1] += jump_height
    
    # Move forward
    new_positions[:, 0] += 0.5  # Forward motion as frames increase

    # Update the points
    scat.set_offsets(new_positions)

    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100, blit=True)

# Show the animation
plt.show()
