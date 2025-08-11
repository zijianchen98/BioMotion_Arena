
import numpy as np
import matplotlib.pyplot as plt
from blaster import Frame, Animation

# Define positions for each point over time
positions = [
    # Example values, update as per actual movement
    [(frame * 0.1, frame * 0.05) for frame in range(0, 100)],  # Example for point 1
    [(frame * 0.05, frame * 0.1) for frame in range(0, 100)],  # Example for point 2
    # Add more sets for other points
]

# Define a function to update positions at each frame
def update_positions(frame):
    for i, pos in enumerate(positions):
        plt.plot([p[0] for p in pos[:frame+1]], [p[1] for p in pos[:frame+1]], 'o--')
    plt.xlim(-0.5, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.gca().invert_yaxis()


# Create the animation
animation = Animation(update_positions)
animation.show()
