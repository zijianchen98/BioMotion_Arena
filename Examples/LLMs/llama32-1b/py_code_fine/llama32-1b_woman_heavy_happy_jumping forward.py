
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the parameters
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)
SUBJECT_SIZE = 10
ACTION_SIZE = 10
STRIPE_SIZE = 5

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to generate the point light stimulus
def generate_point_light_stimulus(x, y, z):
    # Define the color of the point light
    color = WHITE_COLOR
    
    # Define the position of the point light
    light_position = np.array([x, y, z])
    
    # Calculate the direction of the point light
    direction = np.array([1, 0, 0])
    
    # Calculate the light intensity
    light_intensity = 1
    
    # Create a new point light at the calculated position and direction
    ax.scatter(light_position[0], light_position[1], light_position[2], c=color, s=10, alpha=0.5, edgecolor='none')
    
    # Animate the point light
    def animate(i):
        light_position += np.array([1, 0, 0])
        light_position[2] += 1
        ax.scatter(light_position[0], light_position[1], light_position[2], c=color, s=10, alpha=0.5, edgecolor='none')
        return light_position
    
    ani = animation.FuncAnimation(fig, animate, frames=10, interval=50, repeat=False)
    
    return light_position, ani

# Generate the point light stimulus for the happywoman with heavy weight jumping forward
happywoman_position = np.array([WIDTH/2, HEIGHT/2, 0])
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(121, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(122, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(123, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(124, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(125, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(126, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(127, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()

# Animate the action
happywoman_light_position, happywoman_anime = generate_point_light_stimulus(happywoman_position, 0, 0)

# Create a new axis for the action
action_axis = fig.add_subplot(128, projection='3d')
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)

# Draw the action axis
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)

# Draw the point light stimulus
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Draw the action
action_axis.plot3D([], [], [], color=BLACK_COLOR, lw=2)
action_axis.scatter(action_axis.get_xaxis().get_left(), action_axis.get_yaxis().get_top(), action_axis.get_zaxis().get_top(), c=BLACK_COLOR, s=10, alpha=0.5, edgecolor='none')

# Set the axis limits and labels
action_axis.set_xlim(-10, 10)
action_axis.set_ylim(-10, 10)
action_axis.set_zlim(-10, 10)
action_axis.set_xlabel('X')
action_axis.set_ylabel('Y')
action_axis.set_zlabel('Z')

# Display the figure
plt.show()
