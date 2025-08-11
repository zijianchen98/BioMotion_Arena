
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define colors
background_color = 'black'
dot_color = 'white'

# Number of points
num_points = 15

# Time step for the animation
dt = 0.1

# Define positions for each dot
dot_positions = np.zeros((num_points, 2))

def update(frame):
    for i in range(num_points):
        x, y = dot_positions[i]
        if i < num_points // 2:
            x += np.sin(frame * 2 * np.pi * 0.5 - np.pi / 4) * dt * 2.5
        else:
            x += np.sin(frame * 2 * np.pi * 0.5 - np.pi / 4) * dt * 2.5
        
        y = np.sin(frame * 2 * np.pi * 0.5) * dt * 5
        
        dot_positions[i] = (x, y)

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(6, 6))

# Set the background to black
ax.set_facecolor(background_color)

# Create a scatter plot with white points at initial positions
scatter = ax.scatter(dot_positions[:, 0], dot_positions[:, 1], c=dot_color, s=100)

# Set the title and aspect ratio
ax.set_title('Jumping Forward')
ax.set_aspect('equal', 'box')
ax.axis('off')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 80, dt), interval=10, blit=True)

# Display the animation
plt.show()
