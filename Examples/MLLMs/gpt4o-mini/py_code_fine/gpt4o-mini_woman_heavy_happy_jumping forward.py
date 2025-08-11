
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 8)
ax.set_facecolor('black')
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Define the positions of the point-lights to mimic a jumping action
def get_positions(frame):
    # Define a jumping path
    t = frame / 10
    y_up = np.sin(t) * 5 + 3  # up-down motion
    y_forward = frame / 10 - 5  # forward motion
    
    # Configure positions of the 15 points as a human figure
    positions = [
        (0, y_up + 4),   # Head
        (-0.5, y_up + 3), (0.5, y_up + 3),  # Shoulders
        (-1, y_up + 2), (0, y_up + 2), (1, y_up + 2),  # Arms
        (-0.5, y_up + 1), (0.5, y_up + 1),  # Elbows
        (-0.5, y_up), (0.5, y_up),  # Hands
        (0, y_up - 2),  # Torso
        (-0.5, y_up - 4), (0.5, y_up - 4),  # Hips
        (-1, y_up - 6), (0, y_up - 6), (1, y_up - 6)  # Legs
    ]
    # Update forward motion
    positions = [(x + y_forward, y) for (x, y) in positions]
    return positions

# Animation update function
def update(frame):
    positions = get_positions(frame)
    for point, pos in zip(points, positions):
        point.set_data(pos[0], pos[1])
    return points

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100, blit=True)

# Show the animation
plt.show()
