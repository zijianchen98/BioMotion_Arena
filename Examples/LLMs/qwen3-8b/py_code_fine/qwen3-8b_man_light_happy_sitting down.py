
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of points and the action
NUM_POINTS = 15
ACTION = "sitting down"
BACKGROUND_COLOR = "black"
POINT_COLOR = "white"
FRAME_RATE = 30
TOTAL_FRAMES = 100

# Define the positions of the body parts (simplified)
# These are approximate coordinates for a human body with 15 points
# Points: 0 (head), 1 (neck), 2 (shoulder left), 3 (elbow left), 4 (wrist left), 5 (hand left)
# 6 (shoulder right), 7 (elbow right), 8 (wrist right), 9 (hand right)
# 10 (hip left), 11 (knee left), 12 (ankle left), 13 (hip right), 14 (knee right), 15 (ankle right)
# We will use 15 points, so we'll omit one (e.g., ankle right)
BODY_POINTS = np.array([
    [0, 0],   # head
    [0, -5],  # neck
    [-10, -10],  # shoulder left
    [-15, -20],  # elbow left
    [-18, -30],  # wrist left
    [-18, -40],  # hand left
    [10, -10],  # shoulder right
    [15, -20],  # elbow right
    [18, -30],  # wrist right
    [18, -40],  # hand right
    [-5, -50],  # hip left
    [-10, -60],  # knee left
    [-10, -70],  # ankle left
    [5, -50],  # hip right
    [10, -60],  # knee right
])

# Normalize the body points to be within a certain range
BODY_POINTS = BODY_POINTS / 10

# Define the animation function
def animate(frame):
    # Simulate a sitting down motion
    # We'll move the body parts in a realistic way
    # We'll use a sine wave to simulate smooth motion
    # We'll also add a slight acceleration to simulate realistic movement

    # Create a copy of the body points
    points = BODY_POINTS.copy()

    # Apply a sine wave to simulate motion
    # The motion will be more pronounced for the lower body
    # and less for the upper body
    motion = np.sin(2 * np.pi * frame / TOTAL_FRAMES) * 0.5
    points[5:] += motion  # apply more motion to the lower body

    # Add a slight acceleration to simulate realistic movement
    acceleration = 0.01 * (frame / TOTAL_FRAMES)
    points[5:] += acceleration

    # Clear the plot
    ax.clear()
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

    # Plot each point
    for i, (x, y) in enumerate(points):
        circle = Circle((x, y), 0.03, color=POINT_COLOR)
        ax.add_patch(circle)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000/FRAME_RATE, blit=False)

# Show the animation
plt.show()
