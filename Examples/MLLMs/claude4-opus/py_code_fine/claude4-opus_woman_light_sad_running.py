
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
N_LIGHTS = 15  # Number of point-lights
DURATION = 10  # seconds of animation
FPS = 30  # Frames per second
TOTAL_FRAMES = DURATION * FPS

# Initialize positions of point-lights for a running motion
def update_positions(frame):
    # Time normalized to range [0, 1]
    t = frame / TOTAL_FRAMES

    # Calculate position for each point-light
    # This example uses a simple sinusoidal motion to simulate running
    positions = []
    for i in range(N_LIGHTS):
        # Y position oscillates to represent the leg movement
        y = 2.0 * np.sin(2 * np.pi * (t + i * 0.1))  # Leg movement
        # X position moves to represent forward motion
        x = t * 4.0  # Forward motion
        positions.append((x, y))
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 4)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create point-lights
lights, = ax.plot([], [], 'o', color='white', markersize=8)

# Animation function
def animate(frame):
    positions = update_positions(frame)
    x_data, y_data = zip(*positions)
    lights.set_data(x_data, y_data)
    return lights,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

# Show the animation
plt.show()
