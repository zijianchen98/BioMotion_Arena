
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create a lying down animation for a sad man using point lights
def update(frame):
    # Clear the previous frame
    ax.cla()
    
    # Set the limits and background color
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')
    
    # Define point light positions representing the body of the sad man in a lying down position
    point_lights_positions = [
        (0, 0.5 - 0.02 * frame),
        (-0.3, 0),
        (0.3, 0),
        (-0.15, -0.3),
        (0.15, -0.3),
        (-0.3, -0.5),
        (0.3, -0.5),
        (-0.2, -0.6),
        (0.2, -0.6),
        (0, -0.8),
        (0, -0.9),
        (-0.1, -0.4),
        (0.1, -0.4),
        (0, -0.7),
        (0.1, -0.3),
        (-0.1, -0.3)
    ]

    # Calculate new positions to simulate slight movements over time
    for i in range(len(point_lights_positions)):
        x, y = point_lights_positions[i]
        new_y = y + 0.01 * np.sin(frame / 10 + i)  # Smooth oscillation
        point_lights_positions[i] = (x, new_y)

    # Plot the point lights
    for x, y in point_lights_positions:
        ax.plot(x, y, 'wo', markersize=10)  # 'wo' means white color, circle marker

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_facecolor('black')

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

# Display the animation
plt.axis('off')  # Turn off the axis
plt.show()
