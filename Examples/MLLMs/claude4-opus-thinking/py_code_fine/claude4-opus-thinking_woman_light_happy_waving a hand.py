
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_points = 15
frames = 100
wave_height = 0.5  # Maximum height of the wave
movement_speed = 0.1  # Speed of the hand movement

# Initial positions of the points (15 points representing joints)
# The points are arranged to represent upper body configuration
positions = np.array([
    [0, 1],  # Head
    [-0.4, 0.8], [0.4, 0.8],  # Shoulders
    [-0.5, 0.6], [0.5, 0.6],  # Elbows
    [-0.6, 0.4], [0.6, 0.4],  # Wrists
    [0, 0],  # Center of body
    [-0.3, -0.6], [0.3, -0.6],  # Hips
    [-0.6, -1], [0.6, -1],  # Knees
    [-0.4, -1.5], [0.4, -1.5],  # Feet
])

# Create a function to update the animation frame
def update(frame):
    plt.clf()  # Clear previous frame
    plt.xlim(-1, 1)
    plt.ylim(-2, 1)
    plt.gca().set_facecolor('black')  # Set background to black
    plt.axis('off')  # Turn off the axis

    # Calculate hand wave motion
    wave = wave_height * np.sin(np.pi * frame / (frames / 2)) if frame < frames / 2 else wave_height * np.sin(np.pi * (frames - frame) / (frames / 2))
    
    # Update positions for wave motion
    positions[5, 1] += wave  # Move the wrist of waving hand
    positions[6, 1] += wave  # Move the center point of the body
    positions[0, 1] += wave / 2  # Slight movement of the head
    
    # Plot each point as a white dot
    for pos in positions:
        plt.scatter(pos[0], pos[1], color='white', s=100)

# Create an animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# Show the animation
plt.show()
