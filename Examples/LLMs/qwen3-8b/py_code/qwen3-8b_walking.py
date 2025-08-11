
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of points and the action (walking)
NUM_POINTS = 15
ACTION = "walking"

# Define biomechanically plausible joint angles for a walking human (in radians)
# This is a simplified model of a bipedal human with 15 points representing body parts
# The points are: head, shoulders, upper arms, elbows, lower arms, hands, torso, hips, thighs, knees, calves, ankles, feet, pelvis, spine
# We simulate a walking cycle with periodic joint angles

def generate_joint_angles(t, cycle_length=2.0):
    # Simplified joint angle functions for a walking human
    # These are approximate and can be adjusted for more realism
    shoulder_angle = 0.5 * np.sin(2 * np.pi * t / cycle_length)
    elbow_angle = 0.3 * np.sin(2 * np.pi * t / cycle_length + np.pi / 2)
    knee_angle = 0.4 * np.sin(2 * np.pi * t / cycle_length + np.pi / 3)
    hip_angle = 0.2 * np.sin(2 * np.pi * t / cycle_length + np.pi / 4)
    spine_angle = 0.1 * np.sin(2 * np.pi * t / cycle_length + np.pi / 6)
    
    # Create a list of positions for each joint
    positions = [
        # Head
        np.array([0, 0.5]),
        # Shoulders
        np.array([0.3 * (1 + shoulder_angle), 0.3]),
        np.array([-0.3 * (1 + shoulder_angle), 0.3]),
        # Elbows
        np.array([0.3 * (1 + elbow_angle), 0.1]),
        np.array([-0.3 * (1 + elbow_angle), 0.1]),
        # Hands
        np.array([0.5 * (1 + elbow_angle), -0.1]),
        np.array([-0.5 * (1 + elbow_angle), -0.1]),
        # Torso
        np.array([0, 0]),
        # Hips
        np.array([0.2 * (1 + hip_angle), -0.2]),
        np.array([-0.2 * (1 + hip_angle), -0.2]),
        # Knees
        np.array([0.3 * (1 + knee_angle), -0.4]),
        np.array([-0.3 * (1 + knee_angle), -0.4]),
        # Calves
        np.array([0.3 * (1 + knee_angle), -0.6]),
        np.array([-0.3 * (1 + knee_angle), -0.6]),
        # Feet
        np.array([0.5 * (1 + knee_angle), -0.8]),
        np.array([-0.5 * (1 + knee_angle), -0.8]),
        # Pelvis
        np.array([0, -0.9]),
        # Spine
        np.array([0, -0.5]),
    ]
    return positions

# Initialize the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Create circles for the point lights
points = [Circle((0, 0), 0.05, color='white') for _ in range(NUM_POINTS)]
for point in points:
    ax.add_patch(point)

# Animation function
def animate(t):
    positions = generate_joint_angles(t)
    for i, point in enumerate(points):
        point.center = positions[i]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
