
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for a person
# We will use 15 points to represent the major joints of the body
# The points are: head, neck, right shoulder, right elbow, right wrist, 
# left shoulder, left elbow, left wrist, right hip, right knee, right ankle, 
# left hip, left knee, left ankle, and torso
point_light_locations = np.array([
    [0, 10],  # head
    [0, 8],   # neck
    [-3, 6],  # right shoulder
    [-5, 4],  # right elbow
    [-7, 2],  # right wrist
    [3, 6],   # left shoulder
    [5, 4],   # left elbow
    [7, 2],   # left wrist
    [-2, 0],  # right hip
    [-3, -2], # right knee
    [-4, -4], # right ankle
    [2, 0],   # left hip
    [3, -2],  # left knee
    [4, -4],  # left ankle
    [0, 4]    # torso
])

# Define the bowing action
# We will use a simple sinusoidal motion to simulate the bowing action
def bowing_action(t):
    # Define the amplitude and frequency of the motion
    amplitude = 2
    frequency = 0.5
    
    # Calculate the new point-light locations based on the bowing action
    new_locations = point_light_locations.copy()
    
    # Move the head and neck down
    new_locations[0, 1] = 10 - amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[1, 1] = 8 - amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Move the shoulders and elbows forward
    new_locations[2, 0] = -3 + amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[3, 0] = -5 + amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[5, 0] = 3 - amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[6, 0] = 5 - amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Move the hips and knees down
    new_locations[8, 1] = 0 - amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[9, 1] = -2 - amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[11, 1] = 0 - amplitude * np.sin(2 * np.pi * frequency * t)
    new_locations[12, 1] = -2 - amplitude * np.sin(2 * np.pi * frequency * t)
    
    return new_locations

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Initialize the point-lights
point_lights = ax.scatter(point_light_locations[:, 0], point_light_locations[:, 1], c='white', s=10)

# Set the limits of the axis
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 15)

# Hide the axis
ax.axis('off')

# Define the animation function
def animate(t):
    # Clear the current point-lights
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Get the new point-light locations based on the bowing action
    new_locations = bowing_action(t)
    
    # Plot the new point-lights
    ax.scatter(new_locations[:, 0], new_locations[:, 1], c='white', s=10)
    
    # Set the limits of the axis
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 15)
    
    # Hide the axis
    ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 1, 100), interval=50)

plt.show()
