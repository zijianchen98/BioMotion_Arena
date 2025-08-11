
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create points for the body parts (15 points)
body_parts = np.array([
    [0, 1],    # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.6, 0], [0.6, 0],      # Elbows
    [0, 0],   # Body
    [-0.5, -1], [0.5, -1],    # Hips
    [-1, -2], [1, -2],        # Knees
    [-0.5, -3], [0.5, -3],    # Feet
    [-1.5, -1.5], [1.5, -1.5], # Hands
    [-2, -2], [2, -2]          # Weight (the object being carried)
])

# Initialize scatters for each point
scatters = [ax.plot([], [], 'o', color='white')[0] for _ in range(len(body_parts))]

# Update function for animation
def update(frame):
    # Clear previous positions
    for scatter in scatters:
        scatter.set_data([], [])
    
    # Update positions for a running motion
    t = frame / 10  # Time factor for animation
    dx = 0.2 * np.sin(t)  # Horizontal running movement
    dy = -0.5 + 0.5 * np.sin(2 * t)  # Vertical movement for a sad stance

    # Update each body part position
    for i, part in enumerate(body_parts):
        scatter = scatters[i]
        scatter.set_data(part[0] + dx, part[1] + dy)

    return scatters

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
