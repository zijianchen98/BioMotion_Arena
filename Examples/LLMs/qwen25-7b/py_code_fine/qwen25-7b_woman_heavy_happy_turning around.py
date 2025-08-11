
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the points
def initial_positions():
    # Define the positions of the 15 points
    positions = np.array([
        [0, 50 ],
        [ 20, 75 ],
        ( 35, 60 ),
        ( 45, 80 ),
        ( 55, 95 ),
        ( 65, 85 ),
        ( 75, 75 ),
        ( 85, 65 ),
        ( 95, 55 ),
        ( 105, 45 ),
        ( 125, 35 ),
        ( 135, 25 ),
        ( 145, 15 ),
        ( 155, 5 ),
        ( 165, -5 )
    ])
    return positions

# Update the positions for each frame
def update_positions(frame, positions):
    angle = np.radians(frame * 2)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        (np.sin(angle), np.cos(angle))
    ])
    positions[:, :2] = np.dot(positions[:, :2], rotation_matrix.T)
    return positions

# Create the animation
fig, ax = plt.subplots(figsize=(8, 8))
axset(ax, 'aspect', 'equal')
axset(ax, 'xlim', (-20, 180))
axset(ax, 'ylim', (-100, 1100))
axset(ax, 'autoscale_on', False)
axet(ax, 'xaxis', 'off')
axet(ax, 'yaxis', 'off')

positions = initial_positions()
points, = ax.plot(positions[:, 0], positions[:, 1], 'w.')

def animate(frame):
    update_positions(frame, positions)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = FuncAnimation(fig, animate, frames=np.arange(00, 1800), interval=20, blit=True)

plt.show()
