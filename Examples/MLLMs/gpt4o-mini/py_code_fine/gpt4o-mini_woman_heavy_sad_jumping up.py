
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Define the points of the "sad woman" jumping
# The y-coordinates will oscillate to simulate jumping
def get_jumping_points(frame):
    # Base positions (static points)
    static_points = np.array([
        [0, 0.5],    # Head
        [-0.1, 0.4], [0.1, 0.4],  # Shoulders
        [-0.2, 0.3], [0.2, 0.3],  # Elbows
        [-0.3, 0.2], [0.3, 0.2],  # Hands
        [0, 0],      # Central body point
        [-0.4, -0.5], [0.4, -0.5],  # Hips
        [-0.3, -0.9], [0.3, -0.9],  # Knees
        [-0.2, -1.2], [0.2, -1.2],  # Ankles
        [-0.1, -1.5], [0.1, -1.5]   # Feet
    ])
    
    # The jumping motion (y positions oscillate)
    jump_height = 0.2 * np.sin(frame * 0.1)
    jumping_points = static_points.copy()
    jumping_points[:, 1] += jump_height
    
    return jumping_points

# Create scatter plot for points
points, = ax.plot([], [], 'wo', markersize=10)  # 'wo' means white circle

# Animation function
def animate(frame):
    jumping_points = get_jumping_points(frame)
    points.set_data(jumping_points[:, 0], jumping_points[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
