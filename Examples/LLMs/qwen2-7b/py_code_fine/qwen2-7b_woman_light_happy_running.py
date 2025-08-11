
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject and action
subject = 'woman'
action = 'running'

# Define the number of points in the light stimulus
num_points = 15

# Define the parameters for the animation
frame_duration = 0.05  # Duration of each frame in seconds
total_frames = 60  # Total number of frames in the animation

# Create the figure and axes for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim((-10, 10)
ax.set_ylim((-10, 10))
ax.set_aspect('equal')
ax.axis('off')

# Generate the initial positions of the point lights
initial_positions = np.random.uniform(-5ax.get_xlim()[1], ax.get_xlim()[1], size=(num_points, 2))

# Define the function to update the animation
def update(frame):
    global initial_positions
    
    # Update the positions of the point lights
    for i, pos in enumerate(initial_positions):
        x, y = pos
        dx, dy = np.sin(x), np.cos(y)
        initial_positions[1][i] += dx
        initial_positions[1][i] += dy
        
    # Clear the previous frame and plot the updated positions
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Plot the point lights as white circles
    for i, pos in enumerate(initial_positions):
        x, y = pos
        ax.add_patch(plt.Circle((x, y), radius=0.2, color='white', fill=True)
        
    # Set the title of the animation to match the subject and action
    ax.set_title(f'{subject} {action}')
    
    return ax.collections

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=int(frame_duration*1000), blit=False)

# Display the animation
plt.show()

