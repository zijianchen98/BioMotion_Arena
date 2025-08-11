
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the positions of the point-lights for the sitting down action
# These positions are arbitrarily chosen for demonstration purposes
# In a real scenario, you would use data from motion capture or similar technology
point_light_positions = [
    np.array([np.sin(2 * np.pi * i / num_frames), np.cos(2 * np.pi * i / num_frames)]) * 0.5 + np.array([0.5, 0.5])
    for i in range(num_frames)
]

# Ensure there are exactly 15 point-lights by repeating or truncating the list
point_light_positions *= 15 // len(point_light_positions)
point_light_positions = point_light_positions[:15]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_facecolor('black')

# Initialize the point-lights as scatter plot points
point_lights = ax.scatter([], [], color='white')

def animate(frame):
    # Update the positions of the point-lights based on the frame number
    new_positions = [pos * (1 - frame / num_frames) for pos in point_light_positions]
    point_lights.set_offsets(new_positions)

ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=False)

plt.show()
