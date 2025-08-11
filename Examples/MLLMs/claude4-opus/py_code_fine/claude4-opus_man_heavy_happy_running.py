
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100
speed = 0.1

# Initialize positions for the 15 point lights to represent body parts
# For simplification, we will keep these positions in a fixed array centered around the "happyman"
initial_positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.3, 0], [0.3, 0],  # Elbows
    [-0.5, -0.5], [0.5, -0.5],  # Hips
    [0, -1],  # Feet
    [-0.4, -1.5], [0.4, -1.5],  # Knees
    [-0.4, -2], [0.4, -2],  # Ankles
    [-0.3, -2.5], [0.3, -2.5],  # Toes
])

# Function to update position for animation
def update_positions(frame):
    plt.clf()  # Clear the current frame
    plt.xlim(-3, 3)  # Set limits for x-axis
    plt.ylim(-3, 1)  # Set limits for y-axis
    plt.axis('off')  # Turn off the axis

    # Calculate new positions simulating running motion
    vertical_movement = np.sin(frame * speed) * 0.1  # Simulate up/down motion
    horizontal_movement = frame * speed * 0.05  # Forward motion

    # Update positions based on frame count to simulate running
    positions = initial_positions + np.array([horizontal_movement, vertical_movement]).T
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)  # Draw point lights

# Create figure for the animation
fig = plt.figure(figsize=(6, 8), facecolor='black')

# Create animation
ani = animation.FuncAnimation(fig, update_positions, frames=frames, interval=50)

# Show the animation
plt.show()
