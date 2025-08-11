
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
N_LIGHTS = 15
LIGHT_RADIUS = 0.05
LIGHT_COLOR = 'white'
BACKGROUND_COLOR = 'black'

# Define the positions of the lights for the specified action (lying down)
# The positions are based on the anatomical locations of the joints in the human body
positions = np.array([
    [-0.15, -0.2],  # Left heel
    [-0.15, 0.2],   # Right heel
    [-0.1, -0.1],   # Left ankle
    [-0.1, 0.1],    # Right ankle
    [-0.05, -0.15], # Left knee
    [-0.05, 0.15],  # Right knee
    [0, -0.2],      # Left hip
    [0, 0.2],       # Right hip
    [-0.15, 0],     # Left thigh
    [-0.15, 0],     # Right thigh
    [-0.1, -0.05],  # Left shin
    [-0.1, 0.05],   # Right shin
    [-0.05, -0.1],  # Left foot
    [-0.05, 0.1],   # Right foot
    [0, 0]          # Head
])

# Define the animation function
def animate(frame):
    # Clear the previous frame
    ax.clear()
    
    # Set the background color
    ax.set_facecolor(BACKGROUND_COLOR)
    
    # Set the axis limits
    ax.set_xlim(-0.2, 0.2)
    ax.set_ylim(-0.2, 0.2)
    
    # Set the axis aspect ratio to be equal
    ax.set_aspect('equal')
    
    # Set the axis ticks to be invisible
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Calculate the light positions for the current frame
    if frame < 100:
        # Move the left and right heels towards the center
        positions[0] = [-0.1, -0.1]
        positions[1] = [-0.1, 0.1]
    elif frame < 200:
        # Move the left and right ankles towards the center
        positions[2] = [-0.05, -0.05]
        positions[3] = [-0.05, 0.05]
    elif frame < 300:
        # Move the left and right knees towards the center
        positions[4] = [0, -0.05]
        positions[5] = [0, 0.05]
    elif frame < 400:
        # Move the left and right hips towards the center
        positions[6] = [0, 0]
        positions[7] = [0, 0]
    elif frame < 500:
        # Move the left and right thighs towards the center
        positions[8] = [-0.05, 0]
        positions[9] = [-0.05, 0]
    elif frame < 600:
        # Move the left and right shins towards the center
        positions[10] = [-0.01, -0.025]
        positions[11] = [-0.01, 0.025]
    elif frame < 700:
        # Move the left and right feet towards the center
        positions[12] = [0, -0.01]
        positions[13] = [0, 0.01]
    else:
        # Move the head to the center
        positions[14] = [0, 0]
    
    # Plot the lights
    for position in positions:
        ax.plot(position[0], position[1], 'o', markersize=LIGHT_RADIUS, color=LIGHT_COLOR)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)

# Show the animation
plt.show()
