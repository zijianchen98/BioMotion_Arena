
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
background_color = 'black'
light_color = 'white'
fig_size = (8, 8)

# Initial positions of the lights (approximate)
initial_positions = np.array([
    [0, 1],  # Head
    [-0.4, 0.6], [0.4, 0.6],  # Shoulders
    [-0.6, 0.2], [0.6, 0.2],  # Elbows
    [-0.4, -0.2], [0.4, -0.2],  # Hands
    [0, -0.4],  # Torso
    [-0.4, -0.8], [0.4, -0.8],  # Hips
    [-0.6, -1.2], [0.6, -1.2],  # Knees
    [-0.4, -1.6], [0.4, -1.6],  # Ankles
    [0, -1.8]  # Feet
])

# Function to calculate the bowing motion
def bowing_motion(t):
    # Define the key points of the bowing motion
    head = initial_positions[0]
    torso = initial_positions[6]
    hips = initial_positions[7:9]
    
    # Calculate the new positions
    head_new = head + np.array([0, -0.2 * np.sin(2 * np.pi * t / frames)])
    torso_new = torso + np.array([0, -0.2 * np.sin(2 * np.pi * t / frames)])
    hips_new = hips + np.array([[0, 0.2 * np.sin(2 * np.pi * t / frames)], [0, 0.2 * np.sin(2 * np.pi * t / frames)]])
    
    # Update the positions array
    positions = initial_positions.copy()
    positions[0] = head_new
    positions[6] = torso_new
    positions[7:9] = hips_new
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots(figsize=fig_size)
ax.set_facecolor(background_color)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter([], [], s=100, c=light_color)

# Update function for the animation
def update(frame):
    positions = bowing_motion(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
