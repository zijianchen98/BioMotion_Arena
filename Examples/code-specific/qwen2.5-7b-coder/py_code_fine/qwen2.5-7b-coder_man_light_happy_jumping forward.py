
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frame_rate = 30
total_frames = 60
happyman_height = 0.5
light_radius = 0.05

# Initialize positions
positions = np.random.rand(num_lights, 2)
velocities = np.zeros((num_lights, 2))
accelerations = np.zeros((num_lights, 2))

# Happyman parameters
happyman_width = 0.2
happyman_y = 0.4

# Acceleration due to gravity
g = -9.81

def update(frame):
    global positions, velocities, accelerations
    
    # Apply gravity to all lights
    accelerations[:, 1] += g
    
    # Update velocities and positions
    velocities += accelerations * (1 / frame_rate)
    positions += velocities * (1 / frame_rate)
    
    # Reset positions when they go off-screen
    positions[positions[:, 1] > 1] -= 2
    positions[positions[:, 1] < 0] += 2
    
    # Clear previous plot
    ax.clear()
    
    # Draw black background
    ax.set_facecolor('black')
    
    # Draw point-lights
    ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white', edgecolors='none')
    
    # Draw happyman
    ax.add_patch(plt.Rectangle((0.45, happyman_y), happyman_width, happyman_height, color='yellow'))
    
    # Set axis limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=int(1000 / frame_rate), blit=False)
plt.show()
