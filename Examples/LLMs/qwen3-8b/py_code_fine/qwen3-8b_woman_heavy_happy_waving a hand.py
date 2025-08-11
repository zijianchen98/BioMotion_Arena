
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Define the 15 points representing the light sources on the body
# These are approximate positions for a human figure (simplified)
points = np.array([
    [0.3, 0.3],   # Head
    [0.2, 0.1],   # Neck
    [0.1, -0.1],  # Shoulder
    [-0.1, -0.1], # Shoulder
    [-0.2, 0.1],  # Neck
    [-0.3, 0.3],  # Head
    [0.1, -0.3],  # Elbow (right)
    [0.3, -0.4],  # Wrist (right)
    [0.4, -0.6],  # Hand (right)
    [-0.1, -0.3], # Elbow (left)
    [-0.3, -0.4], # Wrist (left)
    [-0.4, -0.6], # Hand (left)
    [0.0, -0.7],  # Hip
    [0.1, -0.9],  # Knee (right)
    [0.0, -1.1],  # Ankle (right)
    [-0.1, -0.9], # Knee (left)
    [-0.0, -1.1], # Ankle (left)
])

# Select only the first 15 points
points = points[:15]

# Create circles for the point lights
circles = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for circle in circles:
    ax.add_patch(circle)

# Define a function to animate the points
def animate(frame):
    # Define a simple motion pattern for waving a hand
    # Right hand moves in an arc, left hand follows
    t = frame / 20
    angle = 0.5 * np.sin(t)
    x_offset = 0.05 * np.sin(t * 3)
    y_offset = 0.05 * np.cos(t * 3)

    # Move the right hand
    points[7][0] += x_offset
    points[7][1] += y_offset
    points[8][0] += x_offset * 0.8
    points[8][1] += y_offset * 0.8
    points[9][0] += x_offset * 0.6
    points[9][1] += y_offset * 0.6

    # Move the left hand
    points[10][0] += -x_offset
    points[10][1] += y_offset
    points[11][0] += -x_offset * 0.8
    points[11][1] += y_offset * 0.8
    points[12][0] += -x_offset * 0.6
    points[12][1] += y_offset * 0.6

    # Move the body
    points[13][1] += 0.02 * np.sin(t * 2)
    points[14][1] += 0.02 * np.sin(t * 2)
    points[15][1] += 0.02 * np.sin(t * 2)

    # Update positions of the circles
    for i in range(15):
        circles[i].center = points[i]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
