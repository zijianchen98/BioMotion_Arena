
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 points
initial_positions = np.array([
    [0, 4],  # Head top
    [-1, 3], [1, 3],  # Shoulders
    [-1, 2], [1, 2],  # Elbows
    [-2, 1], [2, 1],  # Hands
    [0, 2],  # Mid-torso
    [-0.5, 1], [0.5, 1],  # Waist
    [-0.5, 0], [0.5, 0],  # Hip
    [-1, -1], [1, -1],  # Knees
    [-1, -2], [1, -2]   # Feet
])

# Number of frames in the animation
num_frames = 50

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)  # Adjust limits if needed
ax.set_ylim(-3, 5)  # Adjust limits if needed
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)

# Function to update the positions of the points for each frame
def animate(frame):
    # Calculate the bowing motion based on sine wave. More complex bowing movements can be implemented here using splines or motion capture data for realistic human movement.
    angle = np.sin(frame / num_frames * 2 * np.pi) * 0.5  # Bowing angle

    # Update positions based on bowing angle
    current_positions = initial_positions.copy()
    
    # Head and Torso Lean
    current_positions[:8, 0] += angle * (initial_positions[:8, 1]-1)  # Apply lean based on y-coordinate
    current_positions[0, 1] -= abs(angle) # Head drops slightly
    # Legs stay relatively straight.
    
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=20, blit=True)

# To save the animation (uncomment the following line)
# ani.save('bowing_sadman.gif', writer='pillow', fps=30)


plt.show()
