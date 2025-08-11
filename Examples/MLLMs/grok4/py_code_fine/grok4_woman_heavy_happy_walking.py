
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.axis('off')

# Number of point lights
num_lights = 15
# Initial positions of point lights
# These need to be designed to represent a "walking" motion
positions = np.zeros((num_lights, 2))

# Define the offsets for the point lights to mimic walking motion
# Light centers (head, arms, legs)
offsets = np.array([
    [0, 2],   # Head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.7, 1], [0.7, 1],      # Elbows
    [-0.5, 0], [0.5, 0],      # Hands
    [-0.5, -2], [0.5, -2],    # Knees
    [-1, -3], [1, -3],        # Feet
    [-1, -4], [1, -4],        # Toes
    [-1.5, 0], [1.5, 0],      # Hands (lowered)
    [0, -5]                    # Weight center
])

# Create point light objects
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(num_lights)]

# Update function for the animation
def update(frame):
    # Simulate walking motion
    # A simple sine wave can act as a helper for smooth walking motion
    walking_variation = 0.2 * np.sin(np.linspace(0, 2 * np.pi, num_lights) + frame * 0.1)
    
    # Update positions for the walking motion
    for i in range(num_lights):
        positions[i] = offsets[i] + [frame * 0.1, walking_variation[i]]
        points[i].set_data(positions[i, 0], positions[i, 1])

    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
