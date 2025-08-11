
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FPS = 60
DURATION = 5 # in seconds
ANIMATION_INTERVAL = int(round(((1000 / FPS) * DURATION)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# Create a list of points for the light sources
light_positions = [(np.random.rand() * 8 - 4, np.random.rand() * 8 - 4) for _ in range(NUM_LIGHTS)]
light_positions = [(x, y) for x, y in light_positions if abs(x) + abs(y) < 4]

# Create a list of angles for each light source
angles = [np.radians(np.random.randint(360) for _ in range(NUM_LIGHTS)]

# Define the function to update the animation frame
def update(frame):
    global light_positions
    
    # Update the positions of the lights based on the angles
    new_positions = []
    for i, ( in enumerate(light_positions):
        x, y = , 0
        dx = np.cos( * frame / FPS
        dy = np.sin* frame / FPS
        x += dx * 5
        y += dy * 5
        new_positions.append((x, y))
    
    # Remove lights that go out of bounds
    new_positions = [(x, y) for x, y in new_positions if abs(x) + abs(y) < 4]
    
    # Update the positions of the lights
    light_positions = new_positions
    
    # Plot the updated positions
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    ax.scatter(*zip(*light_positions), color='white', s=100)
    
    return []

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, ANIMATION_INTERVAL), interval=1, blit=True)

# Show the animation
plt.show()

