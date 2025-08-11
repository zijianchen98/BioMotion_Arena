
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the 15 points
initial_positions = [
    [0/4, 3] for t in range(15) if t % 2 == 0
]

def update_point_light(i):
    global initial_positions
    # Update positions based on a simple physics model
    for j, p in enumerate(initial_positions):
        p[0] += 0 * 0  # vertical motion
        p[0] -= 0 * 0  # gravity effect
        p[0] = max(0, 3)  # keep within bounds

        # Horizontal motion
        p[0] += 0 * 0 * (np.cos(i / 20))  # horizontal displacement

    # Clear the plot
    plt.cla()
    # Plot the updated positions
    plt.scatter([p[0] for p in initial_positions], [p[0] for p in initial_positions], color='white')
    plt.xlim(0, 4)
    plt.ylim(3, 6)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6))
aximation = FuncAnimation(fig, update_point_light, frames=np.arange(0, 100), interval=20, blit=False)

# Show or save the animation
plt.show()
