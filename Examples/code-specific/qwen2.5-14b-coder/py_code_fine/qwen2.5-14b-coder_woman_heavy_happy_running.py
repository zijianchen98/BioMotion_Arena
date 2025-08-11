
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are placeholders and should be replaced with actual keyframe data
initial_positions = np.random.rand(num_lights, 2)

# Define the keyframes for the happy woman running with heavy weight
# These keyframes should be generated based on a realistic motion capture or manually designed
keyframes = [
    # Keyframe 1
    np.array([[0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
              [0.6, 0.5], [0.7, 0.4], [0.8, 0.3], [0.9, 0.2], [0.8, 0.1],
              [0.7, 0.2], [0.6, 0.3], [0.5, 0.4], [0.4, 0.5], [0.3, 0.6]]),
    # Keyframe 2
    np.array([[0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6], [0.6, 0.7],
              [0.7, 0.6], [0.8, 0.5], [0.9, 0.4], [0.8, 0.3], [0.7, 0.2],
              [0.6, 0.3], [0.5, 0.4], [0.4, 0.5], [0.3, 0.6], [0.2, 0.7]]),
    # Add more keyframes as needed to create a smooth animation
]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
point_lights, = ax.plot([], [], 'o', color='white')

# Initialize the frame index
frame_index = 0

def update(frame):
    global frame_index
    
    # Interpolate between keyframes to create smooth motion
    if frame_index + 1 < len(keyframes):
        t = (frame % 10) / 10  # Interpolate between current and next keyframe
        positions = (1 - t) * keyframes[frame_index] + t * keyframes[frame_index + 1]
    else:
        positions = keyframes[-1]  # Stay at the last keyframe if we've reached the end
    
    # Update the positions of the point lights
    point_lights.set_data(positions[:, 0], positions[:, 1])
    
    # Increment the frame index
    frame_index += 1
    if frame_index >= len(keyframes):
        frame_index = 0  # Reset the frame index to loop the animation
    
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(100), interval=50, blit=True)

# Show the animation
plt.show()
