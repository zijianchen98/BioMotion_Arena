
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define a function to create point-light positions
def get_bowing_positions(num_points, t):
    # Define positions of 15 points for the bowing action
    # y positions of the points will represent bowing from upright to a lower position
    positions = [
        (0, 1),  # head
        (-0.2, 0.6), (0.2, 0.6),  # shoulders
        (-0.3, 0.4), (0.3, 0.4),  # elbows
        (-0.4, 0.2), (0.4, 0.2),  # wrists
        (-0.4, 0), (0.4, 0),      # hips
        (-0.2, -0.4), (0.2, -0.4), # knees
        (-0.1, -0.6), (0.1, -0.6), # ankles
        (-0.05, -0.8), (0.05, -0.8),# feet
    ]
    
    # Animate bowing action
    for i, (x, y) in enumerate(positions):
        positions[i] = (x, y * (1 - 0.5 * (1 - np.cos(np.pi * t))))
    
    return np.array(positions)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color="white")

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    t = frame / 30  # Normalize frame count for time
    positions = get_bowing_positions(15, t)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=100, blit=True)

# Show animation
plt.show()
