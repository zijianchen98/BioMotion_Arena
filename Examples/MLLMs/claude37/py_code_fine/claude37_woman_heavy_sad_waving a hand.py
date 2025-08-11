
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of light points and their initial positions
num_points = 15
initial_positions = np.array([
    [0, 2],  # Head
    [-1, 1], [0, 1], [1, 1],  # Shoulders
    [-1, 0], [0, 0], [1, 0],  # Elbows
    [-1, -1], [0, -1], [1, -1],  # Hands
    [-0.5, -2], [0.5, -2],  # Legs
    [-0.5, -3], [0.5, -3],  # Feet
    [0, -4]  # Center of mass
])

# Waving hand motion parameters
wave_amplitude = 0.5  # Amplitude of hand motion
wave_frequency = 1  # Frequency
wave_speed = 0.1  # Speed of wave motion

# Animation function
def update(frame):
    plt.cla()  # Clear the previous frame
    plt.xlim(-3, 3)
    plt.ylim(-5, 2)
    plt.axis('off')  # Turn off the axis
    t = wave_speed * frame
    # Update positions for waving
    positions = initial_positions.copy()
    # Hand points (2nd row of hands)
    positions[7, 1] += wave_amplitude * np.sin(wave_frequency * t)  # Left hand
    positions[8, 1] += wave_amplitude * np.sin(wave_frequency * t + np.pi)  # Right hand
    # Plot the points
    plt.plot(positions[:, 0], positions[:, 1], 'o', color='white', markersize=15)

# Set up the figure
fig = plt.figure(figsize=(6, 10), facecolor='black')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=100)

# Display the animation
plt.show()
