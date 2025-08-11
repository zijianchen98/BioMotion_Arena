
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
subject = 'sadman'  # The subject performing the action
action = 'forward rolling'  # The action being performed
visual_style = 15  # Number of point-lights sources
motion_quality = 'realistic'  # The desired quality of the animation

# Function to simulate the forward rolling motion
def forward_rolling(x):
    return np.sin(np.pi * x)

# Function to create the point-light stimulus animation
def create_animation():
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_facecolor('black')
    ax.axis('off')

    # Create a list of random positions for the point-lights sources
    positions = np.random.rand(visual_style, 2)
    positions[:, 1] *= -1  # Flip vertically so the animation looks more natural

    def update(frame):
        for i, pos in enumerate(positions):
            pos[0] += forward_roll(frame / 100) * 0.1  # Adjust the speed of the roll
            pos[1] += 0.1  # Gravity effect

            if pos[1] > 1:
                pos[1] = -1  # Reset the y-position when it reaches the top
            if pos[0] > 1 or pos[0] < -1:
                pos[0] = np.sign(pos[0]) * 1  # Reset the x-position when it reaches the edges

            positions[i] = pos

        ax.clear()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.scatter(positions[:, 0], positions[:, 1])

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=20)

    plt.show()

create_animation()

