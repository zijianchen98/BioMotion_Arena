
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Representing the sad man with heavy weight
lights = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.6], [0.6, 0.6],  # Shoulders
    [0.3, 0.7], [0.7, 0.7],  # Elbows
    [0.2, 0.8], [0.8, 0.8],  # Hands
    [0.5, 0.4], [0.5, 0.3],  # Spine
    [0.4, 0.2], [0.6, 0.2],  # Hips
    [0.3, 0.1], [0.7, 0.1],  # Knees
    [0.2, 0.0], [0.8, 0.0],  # Feet
    [0.5, 0.9]  # Weight
])

# Define the movement of each point-light
# Turning around
def animate(frame):
    global lights
    angle = np.radians(frame)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    new_lights = np.dot(lights - [0.5, 0.5], rotation_matrix) + [0.5, 0.5]
    
    # Add some noise to the movement to make it look more natural
    noise = np.random.normal(0, 0.01, (15, 2))
    new_lights += noise
    
    # Keep the weight close to the man
    new_lights[-1] = (new_lights[-1] + new_lights[0]) / 2
    
    return new_lights

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')

scatter = ax.scatter(lights[:, 0], lights[:, 1], c='white', s=10)

def update(frame):
    new_lights = animate(frame)
    scatter.set_offsets(new_lights)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=range(0, 360), interval=50)

plt.show()
