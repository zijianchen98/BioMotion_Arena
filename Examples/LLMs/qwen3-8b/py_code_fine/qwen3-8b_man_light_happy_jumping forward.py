
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions (representing joints)
# These positions are relative to a simplified human body
# We'll simulate a jumping motion

# Define a function to generate a realistic jumping motion
def generate_jumping_motion(num_frames=100):
    # Generate a smooth jumping trajectory
    t = np.linspace(0, 1, num_frames)
    x = 0.5 * np.sin(2 * np.pi * t)  # Horizontal movement
    y = -0.5 * np.cos(2 * np.pi * t) + 0.5  # Vertical jump
    return x, y

# Generate the jumping motion
x, y = generate_jumping_motion()

# Create a list of point-light positions
point_lights = []
for i in range(15):
    # Simulate different joints with slight variations
    offset_x = np.random.uniform(-0.2, 0.2)
    offset_y = np.random.uniform(-0.2, 0.2)
    point_lights.append((x + offset_x, y + offset_y))

# Create a list of circles for the point-lights
circles = [patches.Circle((0, 0), 0.05, color='white') for _ in range(15)]

# Add circles to the plot
for circle in circles:
    ax.add_patch(circle)

# Animation function
def animate(frame):
    for i, circle in enumerate(circles):
        # Interpolate between current and next frame
        if frame < len(point_lights) - 1:
            next_pos = point_lights[frame + 1]
        else:
            next_pos = point_lights[-1]
        current_pos = point_lights[frame]
        # Linear interpolation
        alpha = frame / (len(point_lights) - 1)
        new_x = current_pos[0] + alpha * (next_pos[0] - current_pos[0])
        new_y = current_pos[1] + alpha * (next_pos[1] - current_pos[1])
        circle.center = (new_x, new_y)

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(point_lights), interval=30, blit=False)

# Show the animation
plt.show()
