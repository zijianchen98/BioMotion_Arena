
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sadman
point_lights = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.4, 0.6],  # Left elbow
    [0.6, 0.6],  # Right elbow
    [0.4, 0.4],  # Left hand
    [0.6, 0.4],  # Right hand
    [0.5, 0.7],  # Chest
    [0.5, 0.5],  # Abdomen
    [0.5, 0.3],  # Hip
    [0.4, 0.2],  # Left knee
    [0.6, 0.2],  # Right knee
    [0.4, 0.1],  # Left ankle
    [0.6, 0.1],  # Right ankle
    [0.5, 0.2],  # Weight
])

# Define the motion of the point-lights
def animate(frame):
    global point_lights
    # Sitting down motion
    if frame < 30:
        point_lights[10, 1] -= 0.01  # Left knee bends
        point_lights[11, 1] -= 0.01  # Right knee bends
        point_lights[12, 1] -= 0.01  # Left ankle moves down
        point_lights[13, 1] -= 0.01  # Right ankle moves down
        point_lights[14, 1] -= 0.01  # Weight moves down
    elif frame < 60:
        point_lights[8, 1] -= 0.01  # Hip moves down
        point_lights[9, 1] -= 0.01  # Abdomen moves down
    elif frame < 90:
        point_lights[6, 1] -= 0.01  # Left hand moves down
        point_lights[7, 1] -= 0.01  # Right hand moves down
    elif frame < 120:
        point_lights[2, 1] -= 0.01  # Left shoulder moves down
        point_lights[3, 1] -= 0.01  # Right shoulder moves down
    elif frame < 150:
        point_lights[0, 1] -= 0.01  # Head moves down
    # Update the plot
    plt.cla()
    plt.scatter(point_lights[:, 0], point_lights[:, 1], color='white')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_facecolor('black')
    plt.axis('off')

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), animate, frames=180, interval=50)

# Show the animation
plt.show()
