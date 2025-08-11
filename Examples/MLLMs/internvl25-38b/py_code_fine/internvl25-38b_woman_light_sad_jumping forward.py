
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Set the background and light colors
bg_color = 'black'
light_color = 'white'

# Set the figure size and background color
fig, ax = plt.subplots()
fig.set_size_inches(6, 8)
ax.set_facecolor(bg_color)

# Hide the axes
ax.axis('off')

# Initialize the light positions (head, shoulders, elbows, wrists, hips, knees, ankles)
positions = np.array([
    (0, 4), (1, 3), (-1, 3), (0, 2), (1, 1), (-1, 1), (0, 0),
    (0, -1), (1, -2), (-1, -2), (0, -3), (1, -4), (-1, -4), (0, -5)
])

# Initialize the scatter plot
lights = ax.scatter(positions[:, 0], positions[:, 1], color=light_color, s=100)

# Define the frame update function
def update(frame):
    global positions
    
    # Define the jumping motion for the light points
    t = 2 * np.pi * frame / 100
    amplitude = 0.5 * np.sin(t)
    positions[:, 1] += amplitude
    
    # Update the lights' positions
    lights.set_offsets(positions)
    
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
