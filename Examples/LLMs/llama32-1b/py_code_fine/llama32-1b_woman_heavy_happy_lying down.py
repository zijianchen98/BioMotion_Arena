
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Define subject and action parameters
SUBJECT_X, SUBJECT_Y = 400, 300
SUBJECT_Z = 100

# Define action parameters
ACTION_X, ACTION_Y = 200, 200
ACTION_Z = 100

# Define movement parameters
MOVEMENT_SPEED = 0.01
MOVEMENT_STEPS = 10

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits and aspect ratio
ax.set_xlim(-WIDTH, WIDTH)
ax.set_ylim(-HEIGHT, HEIGHT)
ax.set_aspect('equal')

# Define point light positions
LIGHTS = []
for i in range(15):
    LIGHTS.append([WIDTH + i * (WIDTH // 15), HEIGHT])

# Define action points
ACTION_POINTS = []
for i in range(MOVEMENT_STEPS):
    ACTION_POINTS.append([ACTION_X + i * (ACTION_X // MOVEMENT_STEPS), ACTION_Y + i * (ACTION_Y // MOVEMENT_STEPS)])

# Function to update the plot
def update(frame):
    global LIGHTS, ACTION_POINTS
    
    # Clear the previous frame
    ax.clear()
    
    # Draw the background
    ax.set_facecolor(BLACK_COLOR)
    
    # Draw the point lights
    for light in LIGHTS:
        ax.add_patch(plt.Circle(light, 2, edgecolor='black', facecolor='white', alpha=0.5))
    
    # Draw the action points
    for point in ACTION_POINTS:
        ax.plot(point[0], point[1], 'ro')
    
    # Draw the subject
    ax.plot(SUBJECT_X, SUBJECT_Y, 'bo', markersize=10)
    ax.plot(SUBJECT_X, SUBJECT_Y + 10, 'bo', markersize=10, color='red')
    
    # Set axis limits and aspect ratio
    ax.set_xlim(-WIDTH, WIDTH)
    ax.set_ylim(-HEIGHT, HEIGHT)
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, update, interval=16, blit=True)

plt.show()
