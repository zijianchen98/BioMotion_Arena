
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60
jump_height = 2
jump_distance = 3

# Initialize point light positions
points = np.zeros((num_points, 2))

# Set initial positions for point lights
for i in range(num_points):
    if i < 5:  # Head
        points[i] = [0, 1.5]  # Y position for head
    elif i < 10:  # Body
        points[i] = [0, 0.5 * (10 - i) * 0.1]  # Y position for upper body
    else:  # Legs
        points[i] = [0, 0.5 * (15 - i) * 0.1]  # Y position for legs

# Animation function
def update(frame):
    plt.clf()  # Clear the current figure
    plt.xlim(-5, 5)  # X limit
    plt.ylim(-1, 3)  # Y limit
    plt.gca().set_facecolor('black')  # Black background

    # Calculate the new positions for jumping motion
    jump_progress = frame / frames
    height = jump_height * np.sin(np.pi * jump_progress)  # Jump arc
    distance = jump_distance * jump_progress  # Forward distance

    # Update points based on jump action
    for i in range(num_points):
        if i < 5:  # Head
            points[i] = [distance, height + 1.5]
        elif i < 10:  # Body
            points[i] = [distance, height + 0.5 * (10 - i) * 0.1]
        else:  # Legs
            points[i] = [distance, height + 0.5 * (15 - i) * 0.1]

    # Plot points
    plt.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# Show the animation
plt.show()
