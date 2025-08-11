
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights and frames
num_lights = 15
frames = 100

# Setup figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Create point lights' initial positions (Y-coordinates vary for a 'running' action)
# Starting positions resembling a 'running' motion
point_lights = np.array([[0, 1], [-0.5, 0.5], [0.5, 0.5], [0, 0],
                          [-0.5, -0.5], [0.5, -0.5], [0, -1],
                          [-0.3, -1.5], [0.3, -1.5], [0, -2],
                          [-0.2, -1], [0.2, -1], [-0.4, -2],
                          [0.4, -2], [0, -1.5], [0, -0.5]])

# Create scatter plot for the point lights
scat = ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white')

def update(frame):
    # Update the positions of point lights to simulate running motion
    # Simple sinusoidal motion to simulate running
    phase_shift = frame * 0.1
    y_offsets = 0.1 * np.sin(np.linspace(0, 2 * np.pi, num_lights) + phase_shift)
    updated_points = point_lights.copy()
    updated_points[:, 1] += y_offsets  # Apply the vertical oscillation
    
    # Update scatter plot with new positions
    scat.set_offsets(updated_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True)

# Show the animation
plt.axis('off')  # Hide axes
plt.show()
