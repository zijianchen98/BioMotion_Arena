
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
NUM_LIGHTS = 15
LIGHT_RADIUS = 2
BACKGROUND_COLOR = 'black'
LIGHT_COLOR = 'white'

# Define the sad woman's body parts
BODY_PARTS = {
    'head': (0, 0),
    'left_shoulder': (-40, -20),
    'left_elbow': (-40, -40),
    'left_wrist': (-50, -60),
    'left_hand': (-50, -70),
    'right_shoulder': (40, -20),
    'right_elbow': (40, -40),
    'right_wrist': (50, -60),
    'right_hand': (50, -70),
    'left_hip': (-30, 20),
    'left_knee': (-30, 40),
    'left_ankle': (-30, 60),
    'left_foot': (-30, 70),
    'right_hip': (30, 20),
    'right_knee': (30, 40),
    'right_ankle': (30, 60),
    'right_foot': (30, 70)
}

# Define the light positions for the running motion
LIGHT_POSITIONS = [
    (0, 0),  # head
    (-40, -20),  # left shoulder
    (-40, -40),  # left elbow
    (-50, -60),  # left wrist
    (-50, -70),  # left hand
    (40, -20),  # right shoulder
    (40, -40),  # right elbow
    (50, -60),  # right wrist
    (50, -70),  # right hand
    (-30, 20),  # left hip
    (-30, 40),  # left knee
    (-30, 60),  # left ankle
    (-30, 70),  # left foot
    (30, 20),  # right hip
    (30, 40),  # right knee
    (30, 60)  # right ankle
]

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color
    ax.set_facecolor(BACKGROUND_COLOR)

    # Plot the body parts
    for body_part, position in BODY_PARTS.items():
        ax.plot(position[0], position[1], 'o', color='gray', markersize=10)

    # Plot the lights
    for j, position in enumerate(LIGHT_POSITIONS):
        # Calculate the light's new position based on the running motion
        x = position[0] + 2 * np.sin(np.radians(i))
        y = position[1] + 2 * np.cos(np.radians(i))

        # Plot the light
        ax.plot(x, y, 'o', color=LIGHT_COLOR, markersize=LIGHT_RADIUS)

# Create the figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(-60, 60)
ax.set_ylim(-80, 80)

# Set the axis aspect ratio
ax.set_aspect('equal')

# Animate the figure
ani = animation.FuncAnimation(fig, animate, frames=range(0, 360, 2), interval=20)

# Show the animation
plt.show()
