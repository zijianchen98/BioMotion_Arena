
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
frames = 100
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Ellipse representing the hand
hand = plt.Circle((0.5, 0.5), 0.05, color='white')
ax.add_patch(hand)

# Function to update the hand position
def update(frame):
    x = 0.5 + np.sin(frame / frames * 8 * np.pi) * 0.3
    y = 0.5
    hand.center = (x, y)
    return hand,

# Animation setup
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True)

# Display the animation
plt.axis('off')
plt.show()
