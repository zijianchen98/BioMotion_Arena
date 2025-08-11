
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the parameters
num_points = 15
background_color = 'black'
point_color = 'white'
sitting_down_duration = 5  # seconds

# Define the points
points = np.random.rand(num_points, 2)

# Define the figure size
fig.set_size_inches(8, 8)

# Set the background color
ax.set_facecolor(background_color)

# Create a circle for the body
body = patches.Circle((0.5, 0.5), 0.4, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(body)

# Create a circle for the head
head = patches.Circle((0.5, 0.6), 0.1, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(head)

# Create a circle for the left and right arms
left_arm = patches.Circle((0.3, 0.5), 0.05, edgecolor='white', facecolor='none', lw=2)
right_arm = patches.Circle((0.7, 0.5), 0.05, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(left_arm)
ax.add_patch(right_arm)

# Create a circle for the left and right legs
left_leg = patches.Circle((0.3, 0.4), 0.05, edgecolor='white', facecolor='none', lw=2)
right_leg = patches.Circle((0.7, 0.4), 0.05, edgecolor='white', facecolor='none', lw=2)
ax.add_patch(left_leg)
ax.add_patch(right_leg)

# Set the axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Initialize the point positions
point_positions = np.zeros((num_points, 2))
for i in range(num_points):
    point_positions[i] = np.random.rand(2)

# Define the animation function
def animate(i):
    # Update the point positions
    for j in range(num_points):
        point_positions[j] = np.array([0.5 + 0.1 * np.cos(2 * np.pi * i / sitting_down_duration + j * np.pi / num_points),
                                       0.5 + 0.1 * np.sin(2 * np.pi * i / sitting_down_duration + j * np.pi / num_points)])

    # Clear the previous frame
    ax.clear()

    # Set the background color
    ax.set_facecolor(background_color)

    # Draw the body, head, arms, and legs
    body.center = (0.5, 0.5)
    ax.add_patch(body)
    head.center = (0.5, 0.6)
    ax.add_patch(head)
    left_arm.center = (0.3, 0.5)
    ax.add_patch(left_arm)
    right_arm.center = (0.7, 0.5)
    ax.add_patch(right_arm)
    left_leg.center = (0.3, 0.4)
    ax.add_patch(left_leg)
    right_leg.center = (0.7, 0.4)
    ax.add_patch(right_leg)

    # Draw the points
    ax.scatter(point_positions[:, 0], point_positions[:, 1], color=point_color)

    # Set the axis limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(sitting_down_duration * 30), interval=20, blit=False)

# Show the animation
plt.show()
