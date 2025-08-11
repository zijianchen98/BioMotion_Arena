
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate coordinates for a man lying down
def get_laying_person_state(t):
    # Define baseline position of joints
    base_x = np.array([-0.5, 0, 0.5, -0.5, 0.5, -0.3, 0.3, -0.5, 0.5])
    base_y = np.array([0, 0.2, 0, -0.3, -0.3, -0.4, -0.4, -0.6, -0.6])
    
    # Update y-coordinates for motion (slight wave effect for realism)
    motion_wave = 0.05 * np.sin(t + np.linspace(0, 2 * np.pi, len(base_y)))
    
    # Combine base position with motion wave
    y = base_y + motion_wave
    
    return base_x, y

# Create figure and set up plot limits
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Animation update function
def update(frame):
    # Get new coordinates for the current frame
    x, y = get_laying_person_state(frame * 0.1)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
