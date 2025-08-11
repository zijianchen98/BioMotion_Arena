
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights for the sadwoman waving her hand
# These coordinates are hypothetical and would need to be adjusted for realism
initial_positions = np.array([
    [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4], # shoulder to elbow
    [0.9, 0.3], [1.0, 0.2], [1.1, 0.3], [1.0, 0.4], # hand and fingers
    [0.2, 0.6], [0.4, 0.6], [0.6, 0.6], [0.8, 0.6], # other arm
    [0.5, 0.7], [0.5, 0.8], [0.5, 0.9]             # head and neck
])

# Function to update the positions of the points for each frame
def update(frame):
    # Update the hand position to simulate waving
    if frame % 20 < 10:
        initial_positions[5] += [0, -0.1]
    else:
        initial_positions[5] += [0, 0.1]
    
    scat.set_offsets(initial_positions)

fig, ax = plt.subplots()
ax.set_xlim([0, 1.2])
ax.set_ylim([0, 1.2])
ax.axis('off')  # Hide axes

scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
