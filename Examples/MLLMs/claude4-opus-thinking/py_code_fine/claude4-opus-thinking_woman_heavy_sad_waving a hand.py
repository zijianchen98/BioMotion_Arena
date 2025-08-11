
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters for the animation
num_points = 15
duration = 200  # Frames at 30 FPS will take approximately 7 seconds
frames_per_wave = 30
wave_up_duration = 15
wave_down_duration = 15

# Create a black background
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 1)
ax.axis('off')  # Hide the axes

# Initialize the positions of point-lights (representing a sad woman with heavy weight)
# Using a simple heuristic for a 'sad woman' pose
points = np.array([
    [0, 0],  # Center (head)
    [-0.1, -0.1], [0.1, -0.1],  # Shoulders
    [-0.3, -0.5], [0.3, -0.5],  # Elbows
    [-0.4, -1], [0.4, -1],      # Hands
    [-0.2, -1.5], [0.2, -1.5],  # Hips
    [-0.5, -2], [0.5, -2],      # Knees
    [-0.7, -2.5], [0.7, -2.5],  # Feet
], dtype=float)

# Initialize point-lights on the plot
point_lights, = ax.plot([], [], 'wo', markersize=10)

def init():
    point_lights.set_data([], [])
    return point_lights,

def animate(frame):
    # Calculate hand movement in a waving motion for the left arm
    if frame < wave_up_duration:
        points[3, 1] += 0.05  # Move elbow up
        points[4, 1] += 0.05  # Move hand up
    elif frame < wave_up_duration + wave_down_duration:
        points[3, 1] -= 0.05  # Move elbow down
        points[4, 1] -= 0.05  # Move hand down

    # Assign the point-lights to updated positions
    point_lights.set_data(points[:, 0], points[:, 1])
    
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, init_func=init,
                              blit=True, repeat=False)

# Display the animation in a window
plt.show()
