
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Define the number of point lights and the background
NUM_LIGHTS = 15
BACKGROUND_COLOR = 'black'
LIGHT_COLOR = 'white'

# Define a realistic human walking motion (simplified 2D joint positions)
# This is a basic approximation of a human body with joints and limbs
# We'll simulate a simple bipedal gait with 15 points representing body parts

# Define body segments and their positions
# Each segment is represented as a list of (x, y) positions for the joints
# This is a simplified model of a human body with 15 points

# Define a function to generate a realistic walking motion
def generate_walking_motion(num_frames=100):
    # Define the body segments (15 points)
    body_segments = [
        # Head
        (0, 0),
        # Shoulders
        (-0.5, 0.5), (0.5, 0.5),
        # Upper arms
        (-0.5, 0.5), (0, 0.5), (0.5, 0.5),
        # Forearms
        (0, 0.5), (0.25, 0.3), (0.5, 0.5),
        # Hands
        (0.25, 0.3), (0.5, 0.5),
        # Torso
        (0, 0.5), (0, 0), (0, -0.5),
        # Upper legs
        (0, -0.5), (-0.5, -0.5), (0.5, -0.5),
        # Lower legs
        (-0.5, -0.5), (-0.75, -0.75), (0.5, -0.5), (0.75, -0.75),
        # Feet
        (-0.75, -0.75), (0.75, -0.75)
    ]

    # Define the motion parameters
    walk_speed = 0.05
    step_length = 0.2
    step_height = 0.1
    body_angle = 0.0
    body_angle_speed = 0.01

    # Generate the motion
    motion = []
    for frame in range(num_frames):
        # Simulate walking
        x_offset = frame * walk_speed
        y_offset = step_height * np.sin(frame * 0.1)

        # Apply body angle
        body_angle += body_angle_speed
        rotation_matrix = np.array([
            [np.cos(body_angle), -np.sin(body_angle)],
            [np.sin(body_angle), np.cos(body_angle)]
        ])

        # Apply motion to each point
        frame_points = []
        for x, y in body_segments:
            x_rot = x * np.cos(body_angle) - y * np.sin(body_angle)
            y_rot = x * np.sin(body_angle) + y * np.cos(body_angle)
            x_total = x_rot + x_offset
            y_total = y_rot + y_offset
            frame_points.append((x_total, y_total))
        motion.append(frame_points)

    return motion

# Generate the motion data
motion_data = generate_walking_motion(num_frames=100)

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the point lights
lights = [Circle((0, 0), 0.05, color=LIGHT_COLOR) for _ in range(NUM_LIGHTS)]
for light in lights:
    ax.add_patch(light)

# Function to update the animation
def update(frame):
    for i, light in enumerate(lights):
        x, y = motion_data[frame][i]
        light.center = (x, y)

# Create the animation
ani = FuncAnimation(fig, update, frames=len(motion_data), interval=50, blit=False)

# Show the animation
plt.show()
