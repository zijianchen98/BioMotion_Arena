
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 points representing the human body (simplified)
# Points are based on a simplified skeleton of a human figure
points = np.array([
    [0.0, 0.0],         # Torso center
    [0.3, 0.0],         # Right shoulder
    [0.5, 0.1],         # Right upper arm
    [0.5, -0.1],        # Right lower arm
    [0.6, -0.2],        # Right hand
    [-0.3, 0.0],        # Left shoulder
    [-0.5, 0.1],        # Left upper arm
    [-0.5, -0.1],       # Left lower arm
    [-0.6, -0.2],       # Left hand
    [0.0, 0.3],         # Head
    [0.0, 0.2],         # Neck
    [0.0, 0.1],         # Upper torso
    [0.0, -0.1],        # Lower torso
    [0.0, -0.3],        # Hip
    [0.0, -0.4]         # Leg
])

# Define a function to simulate the motion of the points
def update(frame):
    # Base motion for the torso and head (up and down)
    torso_y = 0.0 + 0.1 * np.sin(0.05 * frame)
    head_y = 0.3 + 0.05 * np.sin(0.05 * frame)
    
    # Right arm waving motion
    right_upper_arm_y = 0.1 + 0.05 * np.sin(0.08 * frame + 1)
    right_lower_arm_y = -0.1 + 0.05 * np.sin(0.08 * frame + 2)
    right_hand_x = 0.6 + 0.05 * np.sin(0.1 * frame + 3)
    
    # Left arm waving motion
    left_upper_arm_y = 0.1 + 0.05 * np.sin(0.08 * frame + 1)
    left_lower_arm_y = -0.1 + 0.05 * np.sin(0.08 * frame + 2)
    left_hand_x = -0.6 + 0.05 * np.sin(0.1 * frame + 4)
    
    # Update the points
    points[0][1] = torso_y
    points[1][1] = torso_y
    points[2][1] = right_upper_arm_y
    points[3][1] = right_lower_arm_y
    points[4][0] = right_hand_x
    points[5][1] = torso_y
    points[6][1] = right_upper_arm_y
    points[7][1] = right_lower_arm_y
    points[8][0] = left_hand_x
    points[9][1] = head_y
    points[10][1] = head_y
    points[11][1] = torso_y
    points[12][1] = torso_y
    points[13][1] = torso_y
    points[14][1] = torso_y
    
    # Clear the previous points
    for patch in circles:
        patch.set_visible(False)
    
    # Draw new points
    for i, (x, y) in enumerate(points):
        circles[i].center = (x, y)
        circles[i].set_visible(True)
    
    return circles

# Create circles for each point
circles = [Circle((0, 0), 0.01, color='white') for _ in range(15)]
for circle in circles:
    ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
