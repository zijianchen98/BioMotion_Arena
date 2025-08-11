
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of point lights and the action
NUM_LIGHTS = 15
ACTION = 'walking'

# Define biomechanically plausible joint angles for a walking human (simplified)
# These are approximate angles for a bipedal human walking
# Positions are relative to the body's center of mass
# We'll use a simple 2D model for demonstration

# Define body parts and their relative positions (simplified)
# This is a 2D skeletal model with joints and limbs
# We'll use a simplified bipedal model with 15 points (lights)

# Define the skeleton as a list of points (x, y) representing joints
# This is a simplified bipedal model with 15 points (lights)
skeleton = np.array([
    [0, 0],        # Hip
    [0, 1],        # Left knee
    [0, 2],        # Left ankle
    [0, 3],        # Left foot
    [0, 4],        # Right knee
    [0, 5],        # Right ankle
    [0, 6],        # Right foot
    [0, 7],        # Spine
    [0, 8],        # Left shoulder
    [0, 9],        # Left elbow
    [0, 10],       # Left hand
    [0, 11],       # Right shoulder
    [0, 12],       # Right elbow
    [0, 13],       # Right hand
    [0, 14]        # Head
])

# Define a function to animate the walking motion
def animate(frame):
    # Define a simple walking cycle with sine wave-like motion for joints
    # This is a simplified biomechanical model for demonstration
    # We'll use a sine wave to simulate the up-and-down motion of the legs and arms

    # Define a time variable based on the frame number
    t = frame / 60.0  # 60 frames per second

    # Define the motion of the skeleton
    # Simulate a walking cycle with a period of 60 frames
    # This is a simplified model for demonstration

    # Create a copy of the skeleton
    new_skeleton = skeleton.copy()

    # Simulate leg motion (left and right)
    # Knees and ankles will move up and down
    new_skeleton[1, 1] = 1 + 0.5 * np.sin(t * 2 * np.pi / 60)
    new_skeleton[2, 1] = 2 + 0.5 * np.sin(t * 2 * np.pi / 60 + np.pi)
    new_skeleton[4, 1] = 5 + 0.5 * np.sin(t * 2 * np.pi / 60)
    new_skeleton[5, 1] = 6 + 0.5 * np.sin(t * 2 * np.pi / 60 + np.pi)

    # Simulate arm motion (left and right)
    # Elbows and hands will move up and down
    new_skeleton[8, 1] = 8 + 0.5 * np.sin(t * 2 * np.pi / 60)
    new_skeleton[9, 1] = 9 + 0.5 * np.sin(t * 2 * np.pi / 60 + np.pi)
    new_skeleton[11, 1] = 12 + 0.5 * np.sin(t * 2 * np.pi / 60)
    new_skeleton[12, 1] = 13 + 0.5 * np.sin(t * 2 * np.pi / 60 + np.pi)

    # Simulate head motion
    new_skeleton[14, 1] = 14 + 0.2 * np.sin(t * 2 * np.pi / 60)

    # Update the positions of the point lights
    for i in range(NUM_LIGHTS):
        # Assign each light to a joint (simplified)
        if i == 0:
            x, y = new_skeleton[0]
        elif i == 1:
            x, y = new_skeleton[1]
        elif i == 2:
            x, y = new_skeleton[2]
        elif i == 3:
            x, y = new_skeleton[3]
        elif i == 4:
            x, y = new_skeleton[4]
        elif i == 5:
            x, y = new_skeleton[5]
        elif i == 6:
            x, y = new_skeleton[6]
        elif i == 7:
            x, y = new_skeleton[7]
        elif i == 8:
            x, y = new_skeleton[8]
        elif i == 9:
            x, y = new_skeleton[9]
        elif i == 10:
            x, y = new_skeleton[10]
        elif i == 11:
            x, y = new_skeleton[11]
        elif i == 12:
            x, y = new_skeleton[12]
        elif i == 13:
            x, y = new_skeleton[13]
        elif i == 14:
            x, y = new_skeleton[14]

        # Update the position of the light
        light_positions[i, 0] = x
        light_positions[i, 1] = y

    # Clear the previous frame
    ax.clear()

    # Set background to black
    ax.set_facecolor('black')

    # Plot the point lights
    for x, y in light_positions:
        ax.scatter(x, y, color='white', s=20)

    # Set limits
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 15)
    ax.set_aspect('equal')
    ax.axis('off')

# Initialize the light positions
light_positions = np.zeros((NUM_LIGHTS, 2))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create the animation
ani = FuncAnimation(fig, animate, frames=120, interval=50, blit=False)

# Show the animation
plt.show()
