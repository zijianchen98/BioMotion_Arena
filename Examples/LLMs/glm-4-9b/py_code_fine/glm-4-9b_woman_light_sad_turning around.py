
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')  # Set background to black
ax.axis('off')  # Hide the axis

# Parameters for the animation
n_points = 15  # Number of point-lights
timeperiod = 2  # Time period for a full cycle (seconds)
n_frames = 120  # Total number of frames for the animation

# Generate random starting positions within a circle for point-lights
angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
radii = np.random.uniform(5, 8, n_points)
init_positions = np.array([radius * np.cos(angle) for radius, angle in zip(radii, angles)])

def update(frame):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')
    ax.axis('off')

    # Calculate the rotation angle based on time
    angle = 2 * np.pi * frame / n_frames * timeperiod
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    # Rotate the initial positions by the calculated angle
    rotated_positions = np.dot(init_positions, rotation_matrix)
    
    # Animate the point-lights around a circle
    scatter = ax.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white', s=50)
    
    # Additional animation parameters
    # For example, we can make some points closer to the origin (as if they are more closer to the head)
    # Modify this list according to your 3D model of 'sad woman'
    close_to_origin = np.random.choice(range(n_points), 5, replace=False)
    close_radii = np.random.uniform(2, 4, len(close_to_origin))
    close_positions = np.array([radius * np.cos(angle + np.random.uniform(-0.2, 0.2))
                               for radius, angle in zip(close_radii, [angles[i] for i in close_to_origin])])
    rotated_close = np.dot(close_positions, rotation_matrix)
    ax.scatter(rotated_close[:, 0], rotated_close[:, 1], color='white', s=70)
    
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, blit=True)
plt.show()
