
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the positions of the 15 point-lights to represent a waving hand
def update_frame(t):
    theta = np.linspace(0, 2 * np.pi, 100)
    alpha = 1.5 * np.sin(t)
    beta = 1.5 * np.cos(t)
    positions = [
        (0, 0),  # Head
        (alpha / 2, beta / 2 + 1),  # Shoulder 1
        (alpha / 2, beta / 2 - 1),  # Shoulder 2
        (alpha / 2 + 1, beta / 2 + 1.5),  # Arm 1
        (alpha / 2 + 1.5 * np.cos(theta[20]), beta / 2 + 1.5 * np.sin(theta[20])),  # Hand 1
        (alpha / 2 - 1, beta / 2 + 1.5),  # Arm 2
        (alpha / 2 - 1.5 * np.cos(theta[20]), beta / 2 + 1.5 * np.sin(theta[20])),  # Hand 2
        (alpha / 2 + 1, beta / 2 - 1.5),  # Arm 3
        (alpha / 2 + 1.5 * np.cos(theta[40]), beta / 2 - 1.5 * np.sin(theta[40])),  # Hand 3
        (alpha / 2 - 1, beta / 2 - 1.5),  # Arm 4
        (alpha / 2 - 1.5 * np.cos(theta[40]), beta / 2 - 1.5 * np.sin(theta[40])),  # Hand 4
        (alpha / 2 + 1.5 * np.cos(theta[60]), beta / 2 + 1.5 * np.sin(theta[60])),  # Fingers 1
        (alpha / 2 + 1.5 * np.cos(theta[80]), beta / 2 + 1.5 * np.sin(theta[80])),  # Fingers 2
        (alpha / 2 + 1.5 * np.cos(theta[100]), beta / 2 + 1.5 * np.sin(theta[100])),  # Fingers 3
        (alpha / 2 + 1.5 * np.cos(theta[120]), beta / 2 + 1.5 * np.sin(theta[120]))  # Fingers 4
    ]
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')
scat = ax.scatter([], [], s=100, c='white')

def animate(i):
    positions = update_frame(i / 10.0)
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.show()
