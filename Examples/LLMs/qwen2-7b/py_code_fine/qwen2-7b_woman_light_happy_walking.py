
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the animation frames
def animate(frame):
    global theta, radius, x, y
    
    # Update the position of the points based on the sine and cosine functions
    x = radius * np.cos(theta + frame * speed)
    y = radius * np.sin(theta + frame * speed)
    
    # Clear the previous frame and plot the new points
    ax.clear()
    ax.plot(x, y, 'w.', markersize=20)

# Initial setup
theta = 0
radius = 0.75
speed = 0.01
fig, ax = plt.subplots(figsize=(5, p))
ax.set_xlim(-1, 1), ax.set_xticks([])
ax.set_ylim(-1, 1), ax.set_yticks([])
ax.set_aspect('equal')

# Create the points representing (15 white points in total
points = []
for i in range(15):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    points.append(ax.plot(x, y, 'wo', markersize=20)[0])

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100, interval=20, blit=False)

plt.show()
