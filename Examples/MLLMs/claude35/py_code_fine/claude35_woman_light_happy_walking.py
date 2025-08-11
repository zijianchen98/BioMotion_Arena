
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the walking motion for the points
def walking_motion(frame):
    # Update the coordinates for the points to simulate walking
    y_offsets = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    x_positions = np.array([0, 0, 0, 0, 0])
    
    # Simulated motion based on frame number
    for i in range(len(y_offsets)):
        x_positions[i] = np.sin(frame / 10 + np.pi * i / 5)  # sinusoidal motion for smooth walking
        points[i].set_data(x_positions[i], y_offsets[i])
    
    return points

# Create figure and set up the axes
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.axis('off')

# Create 15 point lights
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Add additional point lights for details (legs, arms, head)
body_parts_pos = [
    (0, -1), (0.5, -0.5), (-0.5, -0.5), # legs
    (0.4, 0), (-0.4, 0), # arms
    (0, 1) # head
]

for part in body_parts_pos:
    points.append(ax.plot(part[0], part[1], 'o', color='white')[0])

# Create the animation
ani = animation.FuncAnimation(fig, walking_motion, frames=100, interval=100, blit=True)

# Show the animation
plt.show()
