
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point light source
class PointLight:
    def __init__(self, x, y, z, intensity=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.intensity = intensity

    def __str__(self):
        return f"PointLight({self.x}, {self.y}, {self.z}, {self.intensity})"

# Define the happyman's hand
class Hand:
    def __init__(self, x, y, z, width, height, intensity=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.intensity = intensity

    def __str__(self):
        return f"Hand({self.x}, {self.y}, {self.z}, {self.width}, {self.height}, {self.intensity})"

# Create the point light sources
point_lights = [
    PointLight(0, 0, 0, 1.0),
    PointLight(2, 2, 0, 1.0),
    PointLight(4, 4, 0, 1.0),
    PointLight(6, 6, 0, 1.0),
    PointLight(8, 8, 0, 1.0),
    PointLight(10, 10, 0, 1.0),
    PointLight(12, 12, 0, 1.0),
    PointLight(14, 14, 0, 1.0),
    PointLight(16, 16, 0, 1.0),
    PointLight(18, 18, 0, 1.0),
    PointLight(20, 20, 0, 1.0),
    PointLight(22, 22, 0, 1.0),
    PointLight(24, 24, 0, 1.0),
    PointLight(26, 26, 0, 1.0),
    PointLight(28, 28, 0, 1.0),
    PointLight(30, 30, 0, 1.0),
    PointLight(32, 32, 0, 1.0),
]

# Create the happyman's hand
hand = Hand(10, 10, 10, 2, 2, 1.0)

# Create the figure and axis
fig, ax = plt.subplots()

# Function to update the plot
def update(frame):
    global ax, hand, point_lights
    ax.clear()
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_aspect('equal')
    
    # Draw the point light sources
    for light in point_lights:
        ax.add_patch(plt.Rectangle((light.x, light.y), light.width, light.height, fill=False, color='black'))
    
    # Draw the hand
    ax.add_patch(plt.Rectangle((hand.x, hand.y), hand.width, hand.height, fill=True, color='white'))
    
    # Update the plot
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_aspect('equal')
    ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(15), interval=50)

# Show the animation
plt.show()
