
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)

# Define the subject and action
SUBJECT = "Man"
ACTION = "Walking"

# Define the parameters for the animation
N_POINTS = 1000
TIME_STEP = 0.02
TOTAL_TIME = 2

# Create a figure and axis object
fig, ax = plt.subplots()

# Initialize the points array
points = np.zeros((N_POINTS, 2))

# Define the movement parameters
x_offset = 0
y_offset = 0
x_speed = 0
y_speed = 0

# Function to update the points array
def update(frame):
    global points, x_offset, y_offset, x_speed, y_speed
    
    # Update the x and y offsets
    x_offset += x_speed * TIME_STEP
    y_offset += y_speed * TIME_STEP
    
    # Generate points based on the x and y offsets
    points = np.vstack((points, [x_offset, y_offset]))
    
    # Add white point-lights to the points array
    for i in range(N_POINTS):
        x = points[i, 0]
        y = points[i, 1]
        ax.add_patch(plt.Rectangle((x - 50, y - 50), 1, 1, edgecolor='white', facecolor='none'))
        ax.text(x + 25, y - 25, '1', ha='center', va='center', size=24)
    
    # Set the axis limits
    ax.set_xlim(-WIDTH / 2, WIDTH / 2)
    ax.set_ylim(-HEIGHT / 2, HEIGHT / 2)
    
    # Clear the axis
    ax.clear()
    
    # Return the updated points array
    return points

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=TOTAL_TIME, interval=100)

# Show the animation
plt.show()
