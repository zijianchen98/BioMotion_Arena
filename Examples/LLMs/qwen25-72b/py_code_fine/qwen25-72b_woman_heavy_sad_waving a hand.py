
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and frames
num_points = 15
num_frames = 100

# Define the initial positions of the points
np.random.seed(42)
positions = np.random.rand(num_points, 2) * 0.5 + 0.25  # Start in the middle of the screen

# Define the velocities of the points
velocities = np.zeros((num_points, 2))

# Define the gravity and damping factors
gravity = 0.005
damping = 0.995

# Define the hand waving parameters
hand_index = 0  # Index of the point representing the hand
hand_amplitude = 0.1
hand_frequency = 0.05

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the point lights
points = [plt.Circle((positions[i, 0], positions[i, 1]), 0.01, color='white') for i in range(num_points)]
for point in points:
    ax.add_patch(point)

# Update function for the animation
def update(frame):
    global positions, velocities
    
    # Update the positions and velocities
    for i in range(num_points):
        if i == hand_index:
            # Hand waving motion
            positions[i, 0] += hand_amplitude * np.sin(hand_frequency * frame)
        else:
            # Apply gravity and damping
            velocities[i, 1] += gravity
            velocities[i] *= damping
            positions[i] += velocities[i]
        
        # Keep points within the bounds
        if positions[i, 0] < 0 or positions[i, 0] > 1:
            velocities[i, 0] *= -1
            positions[i, 0] = np.clip(positions[i, 0], 0, 1)
        if positions[i, 1] < 0 or positions[i, 1] > 1:
            velocities[i, 1] *= -1
            positions[i, 1] = np.clip(positions[i, 1], 0, 1)
    
    # Update the positions of the points
    for i, point in enumerate(points):
        point.center = (positions[i, 0], positions[i, 1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Show the animation
plt.show()
