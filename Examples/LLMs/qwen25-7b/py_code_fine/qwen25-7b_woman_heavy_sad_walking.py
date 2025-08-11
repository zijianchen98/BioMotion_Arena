
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the point-lights representing the sad woman
def init_positions():
    # Positions are defined in a 2D space where each point-light corresponds to a body part
    positions = np.array([
        [50, 50), (6, 4.5), (7, 4.5), (8, 4.5), (9, 4.5),  # Legs
        (5, 5),     (6, 5),   (7, 5),   (8, 5),   (9, 5),   # Body
        (5, 6),   (6, 6),   (7, 6),   (8, 6),   (9, 6),   # Upper legs
        (5, 7),   (6, 7),   (7, 7),   (8, 7),   (9, 7),   # Hips
        (5, 8),   (6, 8),   (7, 8),   (8, 8),   (9, 8)    # Lower back
    ])
    return positions

# Update the positions to simulate walking
def update_positions(frame, positions):
    step_size = 0.1  # Adjust the step size for more or less speed
    step_direction = -1 if frame % 2 == 0 else 1  # Alternating direction for a smoother walk
    
    new_positions = positions + step_size * step_direction
    new_positions[:, 0] = np.clip(new_positions[:, 0], 1, 10)  # Limit x to within the plot bounds
    new_positions[:,  1] = np.clip(new_positions[:,  1], 1, 10)  # Limit 1 to within the plot bounds
    return new_positions

# Create the animation
def create_animation():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 11)
    ax.set_ylim(1, 11)
    ax.set_aspect('equal')
    ax.set_facecolor('k')  # Black background
    ax.axis('off')

    positions = init_positions()
    points, = ax.plot(positions[:,  0], positions[:,  1], 'w.', ms=10)

    def animate(frame):
        new_positions = update_positions(frame, positions)
        points.set_data(new_positions[:,  1], new_positions[:,  1])
        return points,

    ani = FuncAnimation(fig, animate, frames=np.arange(000, 2000),, interval=30, blit=True, repeat=True)
    plt.show()

create_animation()
