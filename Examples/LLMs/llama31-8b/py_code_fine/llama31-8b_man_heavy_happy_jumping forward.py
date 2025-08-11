
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the point-lights
lights = [
    {'x': 0, 'y': 0.5, 'radius': 0.05},  # head
    {'x': 0.2, 'y': 0.3, 'radius': 0.03},  # left shoulder
    {'x': 0.4, 'y': 0.3, 'radius': 0.03},  # right shoulder
    {'x': 0.2, 'y': 0.1, 'radius': 0.03},  # left elbow
    {'x': 0.4, 'y': 0.1, 'radius': 0.03},  # right elbow
    {'x': 0.2, 'y': 0.05, 'radius': 0.02},  # left wrist
    {'x': 0.4, 'y': 0.05, 'radius': 0.02},  # right wrist
    {'x': 0.2, 'y': 0.2, 'radius': 0.02},  # left hip
    {'x': 0.4, 'y': 0.2, 'radius': 0.02},  # right hip
    {'x': 0.3, 'y': 0.1, 'radius': 0.02},  # left knee
    {'x': 0.3, 'y': 0.05, 'radius': 0.01},  # left ankle
    {'x': 0.5, 'y': 0.1, 'radius': 0.02},  # right knee
    {'x': 0.5, 'y': 0.05, 'radius': 0.01},  # right ankle
    {'x': 0.6, 'y': 0.3, 'radius': 0.03},  # left foot
    {'x': 0.4, 'y': 0.3, 'radius': 0.03},  # right foot
]

# Define the animation parameters
num_frames = 100
frame_rate = 30

# Initialize the light positions
light_positions = [[light['x'], light['y']] for light in lights]

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    # Update the light positions
    for j in range(len(lights)):
        light_positions[j][0] = lights[j]['x'] + np.sin(i * np.pi / 10) * 0.1
        light_positions[j][1] = lights[j]['y'] + np.cos(i * np.pi / 10) * 0.1
        
        # Draw the light
        ax.plot(light_positions[j][0], light_positions[j][1], 'o', markersize=lights[j]['radius'] * 20, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000 // frame_rate, repeat=True)

# Show the animation
plt.show()
