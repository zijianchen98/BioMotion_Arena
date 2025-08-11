
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the update interval
num_frames = 200
interval = 50  # Delay between frames in milliseconds

# Define the initial positions of the 15 points
points_initial = np.array([
    [0.0, 2.2],  # head
    [-0.2, 1.8], [0.2, 1.8],  # shoulders
    [-0.3, 1.4], [0.3, 1.4],  # elbows
    [-0.4, 1.0], [0.4, 1.0],  # wrists
    [-0.1, 1.2], [0.1, 1.2],  # hips
    [-0.2, 0.6], [0.2, 0.6],  # knees
    [-0.3, 0.2], [0.3, 0.2],  # ankles
    [-0.1, -0.2], [0.1, -0.2]   # feet
])

# Define functions for sine wave motion of the points
def sine_wave(amplitude, frequency, phase, t):
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Define animation function
def update(frame):
    plt.clf()  # Clear the current figure
    
    # Apply sine wave motion to point positions
    points = points_initial.copy()
    
    # Head motion (small up/down movement)
    points[0, 1] += sine_wave(0.02, 0.2, 0, frame / 20)
    
    # Shoulder and elbow movements (coordinated)
    points[1:3, 0] += sine_wave(0.01, 0.1, 0, frame / 20)
    points[3:5, 0] += sine_wave(0.02, 0.15, np.pi/2, frame / 20)
    
    # Wrist movements
    points[5:7, 0] += sine_wave(0.01, 0.2, 0, frame / 20)
    
    # Hip movement
    points[7:9, 0] += sine_wave(0.005, 0.1, 0, frame / 20)
    
    # Knee and ankle movements
    points[9:11, 0] += sine_wave(0.005, 0.1, np.pi/2, frame / 20)
    points[11:13, 0] += sine_wave(0.01, 0.15, 0, frame / 20)
    
    # Feet movement
    points[13:15, 0] += sine_wave(0.005, 0.1, 0, frame / 20)

    # Plot the points on the cleared figure
    plt.scatter(points[:, 0], points[:, 1], color='white', s=50)
    
    # Set plot limits and appearance
    plt.xlim([-0.6, 0.6])
    plt.ylim([-0.4, 2.4])
    plt.gca().set_facecolor('black')  # Set background color to black
    plt.gca().set_aspect('equal')  # Ensure equal aspect ratio
    plt.axis('off')  # Hide the axis

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=num_frames, repeat=True)

# Display the animation
plt.show()
