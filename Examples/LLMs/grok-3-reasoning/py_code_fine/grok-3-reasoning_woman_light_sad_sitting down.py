
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions for standing and seated poses
standing_positions = [
    (0, 7),    # head
    (0, 6),    # neck
    (-0.3, 6), # left shoulder
    (0.3, 6),  # right shoulder
    (0, 5),    # torso center
    (-0.7, 5.5), # left elbow
    (0.7, 5.5),  # right elbow
    (-0.9, 5),   # left wrist
    (0.9, 5),    # right wrist
    (-0.2, 4),   # left hip
    (0.2, 4),    # right hip
    (-0.5, 2.5), # left knee
    (0.5, 2.5),  # right knee
    (-0.5, 0.5), # left ankle
    (0.5, 0.5)   # right ankle
]

seated_positions = [
    (0, 4.5),    # head
    (0, 4),      # neck
    (-0.3, 4.5), # left shoulder
    (0.3, 4.5),  # right shoulder
    (0, 3.5),    # torso center
    (-0.4, 3.5), # left elbow
    (0.4, 3.5),  # right elbow
    (-0.5, 2.5), # left wrist
    (0.5, 2.5),  # right wrist
    (-0.2, 3),   # left hip
    (0.2, 3),    # right hip
    (-0.5, 3),   # left knee
    (0.5, 3),    # right knee
    (-0.5, 0),   # left ankle
    (0.5, 0)     # right ankle
]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(t):
    alpha = t / 30.0
    x = [standing[0] * (1 - alpha) + seated[0] * alpha for standing, seated in zip(standing_positions, seated_positions)]
    y = [standing[1] * (1 - alpha) + seated[1] * alpha for standing, seated in zip(standing_positions, seated_positions)]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=30, init_func=init, blit=True, interval=50)

# Show the plot
plt.show()
