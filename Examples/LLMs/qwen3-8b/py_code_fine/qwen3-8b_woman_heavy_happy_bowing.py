
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights and the action
NUM_LIGHTS = 15
ACTION = "bowing"
BACKGROUND_COLOR = "black"
LIGHT_COLOR = "white"

# Define a biomechanically plausible motion for a happy woman bowing
# We'll use a simplified model with a skeleton-like structure
# Coordinates are relative to a central point (origin)

# Define the body parts and their positions
body_parts = {
    "hips": (0, 0),
    "torso": (0, -0.5),
    "shoulders": (0, -0.75),
    "upper_left_arm": (-0.3, -0.75),
    "upper_right_arm": (0.3, -0.75),
    "lower_left_arm": (-0.5, -0.9),
    "lower_right_arm": (0.5, -0.9),
    "left_hand": (-0.6, -1.0),
    "right_hand": (0.6, -1.0),
    "left_knee": (-0.2, -0.9),
    "right_knee": (0.2, -0.9),
    "left_foot": (-0.3, -1.1),
    "right_foot": (0.3, -1.1),
    "head": (0, -0.3)
}

# Define a function to animate the motion
def animate(frame):
    # Create a smooth bowing motion
    # We'll simulate a bow by lowering the torso and arms, then returning
    # We'll use a sine wave to create smooth motion
    t = frame / 100.0
    bowing_angle = 0.2 * np.sin(2 * np.pi * t)
    bowing_speed = 0.05 * np.sin(2 * np.pi * t)

    # Define the positions of the point lights
    positions = []
    for part in body_parts:
        x, y = body_parts[part]
        # Apply bowing to torso and arms
        if part in ["torso", "shoulders", "upper_left_arm", "upper_right_arm",
                    "lower_left_arm", "lower_right_arm", "head"]:
            y += bowing_angle
        # Apply some subtle movement to simulate natural motion
        if part in ["left_hand", "right_hand", "left_foot", "right_foot"]:
            y += bowing_speed
        positions.append((x, y))

    # Clear the plot
    plt.cla()
    plt.axis('off')
    plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
    plt.gca().set_facecolor(BACKGROUND_COLOR)

    # Draw point lights
    for i, (x, y) in enumerate(positions):
        circle = Circle((x, y), 0.02, color=LIGHT_COLOR)
        plt.gca().add_patch(circle)

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
