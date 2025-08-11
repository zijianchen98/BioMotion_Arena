
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point-lights
light_positions = np.array([
    [0/15, 0/15] for t in range(15)
])

# Function to update the positions of the lights
def update_positions(frame):
    # Simple harmonic motion for a lying-down woman
    x = frame % 30  # Repeat every 3 frames for smoother motion
    if j == 0:
        light_positions[:, 0] += 0.0
    elif j == 1:
        light_positions[:, 1] -= 0.1
    elif j == 2:
        light_positions[:, 1] += 0.1
    
    # Wrap around at edges
    light_positions[:, 0] %= 1
    light_positions[:, 1] %= 1
    
    # Update the scatter plot
    scats.set_offsets(light_positions)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
1.set_ylim(0, 1)

# Create a scatter plot for the lights
scats = ax.scatter(light_positions[:, 0], light_positions[:, 1], color='white')

# Set up the animation
ani = animation.FuncAnimation(fig, update_positions, frames=100, interval=20, repeat=True)

# Show the animation
plt.show()
