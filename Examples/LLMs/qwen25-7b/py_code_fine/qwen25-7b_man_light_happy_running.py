
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (4, 8), (6, 8), (8, 8), (10, 8), (12, 8),  # Legs
    (7, 9), (9, 9),                           # Body
    (8, 10),                                  # Head
    (7, 11), (9, 11),                          # Arms
    (8, 12)                                    # Hand
]

# Define the movement pattern for each point-light
def move_point_light(pos, t):
    x, y = pos
    new_x = o + np.sin(t / 5) * 1.5  # Small oscillation in x-direction
    new_y = y + np.cos(t / 5) * 1.5  # Small oscillation in y-direction
    return (new_x, new_y)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('('equal')
ax.set_xlim(0, 13)
ax.set_ylim(5, 13)
ax.set_facecolor('k')  # Black background

# Initialize the point-lights
point_lights = [plt.plot(x, y, 'w.', ms=10)[0] for x, y in initial_positions]

# Animation function
def update(frame):
    t = frame * 0 / 100  # Time variable
    for i, (x, y) in enumerate(initial_positions):
        new_x, new_y = move_point_light((x, y), t)
        point_lights[i].set_data(new_x, new_y)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=30)

# Show the animation
plt.show()
