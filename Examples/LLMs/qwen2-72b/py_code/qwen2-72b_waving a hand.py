
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
n_points = 15
frame_rate = 30
duration = 3  # seconds
frames = frame_rate * duration

# Generate initial positions for the points in a stick figure configuration
positions = np.zeros((frames, n_points, 2))
positions[0] = [
    [0, 0],   # Head
    [-0.2, -0.2], [0.2, -0.2],  # Shoulders
    [-0.4, -0.6], [0.4, -0.6],  # Elbows
    [-0.6, -0.8], [0.6, -0.8],  # Wrists
    [-0.7, -1], [0.7, -1],      # Hands
]

# Define the motion for waving a hand
def wave_hand(positions):
    for i in range(1, frames):
        # Update the position of the waving hand
        angle = np.sin(i / (frame_rate / 2)) * np.pi / 8
        positions[i, 10, 0] = positions[0, 10, 0] + np.cos(angle)
        positions[i, 10, 1] = positions[0, 10, 1] + np.sin(angle)
        
        # Update other parts of the body to maintain balance
        positions[i, 5, 0] += 0.1 * np.sin(i / (frame_rate / 4))
        positions[i, 5, 1] -= 0.1 * np.sin(i / (frame_rate / 4))
        
        # Keep the rest of the body relatively static
        for j in range(n_points):
            if j not in [5, 10]:
                positions[i, j] = positions[0, j]
                
    return positions

# Apply the motion to the point lights
positions = wave_hand(positions)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

def animate(i):
    points.set_data(positions[i, :, 0], positions[i, :, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/frame_rate, blit=True)

plt.show()
