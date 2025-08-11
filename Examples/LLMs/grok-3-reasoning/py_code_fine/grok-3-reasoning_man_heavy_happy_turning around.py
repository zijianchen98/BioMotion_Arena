
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define the initial 3D positions of the 15 points
points = [
    (0, 1.8, 0),      # head
    (0.2, 1.5, -0.05), # left shoulder
    (-0.2, 1.5, -0.05),# right shoulder
    (0.25, 1.3, 0.05), # left elbow
    (-0.25, 1.3, 0.05),# right elbow
    (0.3, 1.1, 0.1),   # left wrist
    (-0.3, 1.1, 0.1),  # right wrist
    (0.15, 0.9, -0.05),# left hip
    (-0.15, 0.9, -0.05),# right hip
    (0.15, 0.6, 0.05), # left knee
    (-0.15, 0.6, 0.05),# right knee
    (0.15, 0.3, 0.1),  # left ankle
    (-0.15, 0.3, 0.1), # right ankle
    (0.15, 0, 0.15),   # left foot
    (-0.15, 0, 0.15)   # right foot
]

def get_screen_positions(theta):
    """
    Calculate the 2D screen positions of the points after rotation.
    
    Parameters:
    theta (float): The rotation angle in radians.
    
    Returns:
    list of tuples: The 2D positions (x, y) for each point.
    """
    screen_positions = []
    for x, y, z in points:
        x_screen = x * math.cos(theta) + z * math.sin(theta)
        y_screen = y
        screen_positions.append((x_screen, y_screen))
    return screen_positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize scatter plot for the points
scat = ax.scatter([], [], s=50, color='white')

def update(frame):
    """
    Update the positions of the points for each frame.
    
    Parameters:
    frame (int): The current frame number.
    
    Returns:
    tuple: The updated scatter plot.
    """
    theta = 2 * math.pi * frame / 150  # Calculate theta for the current frame
    positions = get_screen_positions(theta)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=150, interval=33, blit=True)

plt.show()
