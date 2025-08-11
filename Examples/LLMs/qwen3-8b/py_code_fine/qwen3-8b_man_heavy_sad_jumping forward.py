
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions (representing body joints)
# Positions are based on a simplified human body with a weighted object
# The positions are relative to a central point (e.g., the pelvis)
# We'll use a list of coordinates for the 15 points

# Initial positions (simplified human body with a weighted object)
# Points are: head, shoulders, arms, torso, pelvis, legs, weighted object
# These are approximate positions for a human figure
initial_positions = np.array([
    [0, 3],     # head
    [-1, 1],    # left shoulder
    [1, 1],     # right shoulder
    [0, 0],     # torso
    [0, -2],    # pelvis
    [-1, -4],   # left foot
    [1, -4],    # right foot
    [-2, -6],   # left hand (weighted object)
    [2, -6],    # right hand (weighted object)
    [-1, -3],   # left knee
    [1, -3],    # right knee
    [-1, -1],   # left hip
    [1, -1],    # right hip
    [-1, -2],   # left elbow
    [1, -2],    # right elbow
])

# Normalize positions to fit in the plot area
positions = initial_positions / 3

# Create circles for the point-lights
points = [Circle((x, y), 0.1, color='white') for x, y in positions]
for point in points:
    ax.add_patch(point)

# Define a function to update the animation
def update(frame):
    # Define a smooth jumping motion using sine and cosine functions
    # We'll simulate the jump forward by moving the body forward and up
    # and then back down, with the weighted object moving in a natural way

    # Time parameter for the animation
    t = frame / 100.0

    # Define the motion for the body
    # We'll move the pelvis forward and up during the jump
    pelvis_y = -2 + 4 * np.sin(t * 2 * np.pi)
    pelvis_x = 0 + 2 * np.sin(t * 2 * np.pi)

    # Move torso up and forward
    torso_y = -2 + 4 * np.sin(t * 2 * np.pi)
    torso_x = 0 + 2 * np.sin(t * 2 * np.pi)

    # Move head up and forward
    head_y = 3 + 4 * np.sin(t * 2 * np.pi)
    head_x = 0 + 2 * np.sin(t * 2 * np.pi)

    # Move shoulders up and forward
    shoulder_y = 1 + 4 * np.sin(t * 2 * np.pi)
    shoulder_x = -1 + 2 * np.sin(t * 2 * np.pi)
    shoulder_y_right = 1 + 4 * np.sin(t * 2 * np.pi)
    shoulder_x_right = 1 + 2 * np.sin(t * 2 * np.pi)

    # Move hips forward
    hip_y_left = -1 + 4 * np.sin(t * 2 * np.pi)
    hip_x_left = -1 + 2 * np.sin(t * 2 * np.pi)
    hip_y_right = -1 + 4 * np.sin(t * 2 * np.pi)
    hip_x_right = 1 + 2 * np.sin(t * 2 * np.pi)

    # Move knees forward
    knee_y_left = -3 + 4 * np.sin(t * 2 * np.pi)
    knee_x_left = -1 + 2 * np.sin(t * 2 * np.pi)
    knee_y_right = -3 + 4 * np.sin(t * 2 * np.pi)
    knee_x_right = 1 + 2 * np.sin(t * 2 * np.pi)

    # Move feet forward
    foot_y_left = -4 + 4 * np.sin(t * 2 * np.pi)
    foot_x_left = -1 + 2 * np.sin(t * 2 * np.pi)
    foot_y_right = -4 + 4 * np.sin(t * 2 * np.pi)
    foot_x_right = 1 + 2 * np.sin(t * 2 * np.pi)

    # Move elbows forward
    elbow_y_left = -2 + 4 * np.sin(t * 2 * np.pi)
    elbow_x_left = -1 + 2 * np.sin(t * 2 * np.pi)
    elbow_y_right = -2 + 4 * np.sin(t * 2 * np.pi)
    elbow_x_right = 1 + 2 * np.sin(t * 2 * np.pi)

    # Move hands (weighted object) forward
    hand_y_left = -6 + 4 * np.sin(t * 2 * np.pi)
    hand_x_left = -2 + 2 * np.sin(t * 2 * np.pi)
    hand_y_right = -6 + 4 * np.sin(t * 2 * np.pi)
    hand_x_right = 2 + 2 * np.sin(t * 2 * np.pi)

    # Update the positions of the point-lights
    points[0].center = (head_x, head_y)  # head
    points[1].center = (shoulder_x, shoulder_y)  # left shoulder
    points[2].center = (shoulder_x_right, shoulder_y_right)  # right shoulder
    points[3].center = (torso_x, torso_y)  # torso
    points[4].center = (pelvis_x, pelvis_y)  # pelvis
    points[5].center = (foot_x_left, foot_y_left)  # left foot
    points[6].center = (foot_x_right, foot_y_right)  # right foot
    points[7].center = (hand_x_left, hand_y_left)  # left hand (weighted object)
    points[8].center = (hand_x_right, hand_y_right)  # right hand (weighted object)
    points[9].center = (knee_x_left, knee_y_left)  # left knee
    points[10].center = (knee_x_right, knee_y_right)  # right knee
    points[11].center = (hip_x_left, hip_y_left)  # left hip
    points[12].center = (hip_x_right, hip_y_right)  # right hip
    points[13].center = (elbow_x_left, elbow_y_left)  # left elbow
    points[14].center = (elbow_x_right, elbow_y_right)  # right elbow

    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
