
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Point locations of a sad man
# Define initial positions of the point-lights
def get_point_light_positions(jump_height):
    # Should simulate 15 points (e.g., head, shoulders, elbows, hips, knees, and feet)
    # Define the vertical position based on jump height
    head = np.array([0, 3 + jump_height])
    arms = np.array([[-1, 2 + jump_height], [1, 2 + jump_height], [-1, 2 + jump_height]])
    elbows = np.array([[-1, 1 + jump_height], [1, 1 + jump_height]])
    torso = np.array([[0, 2 + jump_height]])
    hips = np.array([[0, 1 + jump_height], [-0.5, 0 + jump_height], [0.5, 0 + jump_height]])
    knees = np.array([[-0.5, -1 + jump_height], [0.5, -1 + jump_height]])
    feet = np.array([[-0.5, -2 + jump_height], [0.5, -2 + jump_height]])

    points = np.concatenate([head.reshape(1, 2), arms, elbows, torso, hips, knees, feet])
    return points

# Function to animate jumping
def animate(i):
    plt.clf()
    jump_height = np.sin(i / 10.0)  # Simulating a jumping motion
    points = get_point_light_positions(jump_height)
    plt.scatter(points[:, 0], points[:, 1], color='white')
    plt.xlim([-5, 5])
    plt.ylim([-3, 5])
    plt.gca().set_facecolor('black')
    plt.axis('off')  # Turn off the axis

# Set up the figure and animation
fig = plt.figure(figsize=(5, 5))
anim = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
